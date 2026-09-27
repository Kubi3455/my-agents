"""WordPress REST client for the blog-writer agent (stdlib only).

Commands:
  python wp_client.py check                      # auth + Rank Math meta check
  python wp_client.py inventory                  # -> data/post-inventory.json (public, no auth)
  python wp_client.py publish <post.json>        # upload images + create DRAFT post
  python wp_client.py diff <post_id> <pkg_dir>   # how much the human edited our draft

Env: WP_USER, WP_APP_PASSWORD (WordPress Application Password)
"""
import base64
import difflib
import html
import json
import mimetypes
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

# Always www: the bare domain 301-redirects and the redirect drops Authorization.
SITE = "https://www.firstevolvenextscale.com"
API = SITE + "/wp-json/wp/v2"
AGENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INVENTORY = os.path.join(AGENT_DIR, "data", "post-inventory.json")
MAX_TAGS = 10
SOCIAL_MESSAGE_KEY = "jetpack_publicize_message"  # Jetpack Social: shared caption
RANK_MATH_KEYS = ("rank_math_title", "rank_math_description", "rank_math_focus_keyword")


class WPError(Exception):
    pass


def _auth_header():
    user, pw = os.environ.get("WP_USER"), os.environ.get("WP_APP_PASSWORD")
    if not user or not pw:
        raise WPError("WP_USER / WP_APP_PASSWORD not set")
    token = base64.b64encode(f"{user}:{pw}".encode()).decode()
    return {"Authorization": f"Basic {token}"}


def call(method, path, payload=None, raw=None, headers=None, auth=True, full=False):
    url = path if path.startswith("http") else API + path
    h = {"User-Agent": "blog-writer-agent/1.0", "Accept": "application/json"}
    if auth:
        h.update(_auth_header())
    data = raw
    if payload is not None:
        data = json.dumps(payload).encode()
        h["Content-Type"] = "application/json"
    h.update(headers or {})
    req = urllib.request.Request(url, data=data, method=method, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            body = json.load(r)
            return (body, r.headers) if full else body
    except urllib.error.HTTPError as e:
        # Never echo request headers (they contain the credential).
        raise WPError(f"{method} {path} -> {e.code}: {e.read().decode(errors='replace')[:400]}")


def get_all(path, auth=False):
    items, page = [], 1
    while True:
        sep = "&" if "?" in path else "?"
        batch, hdr = call("GET", f"{path}{sep}per_page=100&page={page}", auth=auth, full=True)
        items += batch
        if page >= int(hdr.get("X-WP-TotalPages", 1)):
            return items
        page += 1


# ---------- commands ----------

def cmd_check():
    me = call("GET", "/users/me?context=edit")
    caps = me.get("capabilities", {})
    print(f"auth OK: {me.get('name')} (can publish_posts={caps.get('publish_posts')}, "
          f"upload_files={caps.get('upload_files')})")
    # Rank Math meta must be registered for REST (see data/imports/HOW_TO_SETUP.md)
    probe = call("GET", "/posts?per_page=1&context=edit&status=any")
    meta = probe[0].get("meta", {}) if probe else {}
    missing = [k for k in RANK_MATH_KEYS if k not in meta]
    if missing:
        print("WARN: Rank Math meta not exposed in REST:", ", ".join(missing))
        return 1
    print("rank math meta: OK")
    if SOCIAL_MESSAGE_KEY in meta:
        print("jetpack social message: OK")
    else:
        print(f"WARN: {SOCIAL_MESSAGE_KEY} not in REST meta (Jetpack Social not active?)")
    return 0


def cmd_inventory():
    cats = {c["id"]: c["name"] for c in get_all("/categories?_fields=id,name,count")}
    tags_full = get_all("/tags?_fields=id,name,count")
    tags = {t["id"]: t["name"] for t in tags_full}
    posts = get_all("/posts?_fields=id,date,slug,link,title,excerpt,categories,tags")
    out = {
        "site": SITE,
        "posts": [{
            "id": p["id"],
            "date": p["date"][:10],
            "title": html.unescape(p["title"]["rendered"]),
            "slug": p["slug"],
            "link": p["link"].replace("://firstevolvenextscale", "://www.firstevolvenextscale"),
            "categories": [cats.get(c, c) for c in p["categories"]],
            "tags": [tags.get(t, t) for t in p["tags"]],
            "excerpt": html.unescape(re.sub(r"<[^>]+>", "", p["excerpt"]["rendered"])).strip()[:300],
        } for p in posts],
        "categories": [{"id": k, "name": v} for k, v in cats.items()],
        "tags": sorted(tags_full, key=lambda t: -t["count"]),
    }
    os.makedirs(os.path.dirname(INVENTORY), exist_ok=True)
    with open(INVENTORY, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"inventory: {len(out['posts'])} posts, {len(tags)} tags -> {INVENTORY}")
    return 0


def resolve_tags(proposed, existing):
    """Decide which tags the new post gets.

    proposed: list[str]            tag names the agent suggested for this post
    existing: list[dict]           site tags: {"id": int, "name": str, "count": int}, sorted by count desc
    returns:  (reuse_ids: list[int], create_names: list[str])

    Policy (owner decision 2026-09-28): every post gets MAX_TAGS post-specific tags.
    Existing tags are reused on a case-insensitive name match so duplicates like
    "AI Agents" / "ai agents" never appear; everything else is created.
    """
    by_name = {t["name"].strip().lower(): t["id"] for t in existing}
    reuse, create, seen = [], [], set()
    for name in proposed:
        clean = " ".join(name.split())
        key = clean.lower()
        if not clean or key in seen:
            continue
        seen.add(key)
        if key in by_name:
            reuse.append(by_name[key])
        else:
            create.append(clean)
        if len(seen) == MAX_TAGS:
            break
    return reuse, create


def upload_image(pkg_dir, img):
    path = os.path.join(pkg_dir, img["file"])
    with open(path, "rb") as f:
        raw = f.read()
    ctype = mimetypes.guess_type(path)[0] or "image/png"
    media = call("POST", "/media", raw=raw, headers={
        "Content-Type": ctype,
        "Content-Disposition": f'attachment; filename="{os.path.basename(path)}"',
    })
    call("POST", f"/media/{media['id']}", payload={
        "alt_text": img["alt"],
        "caption": img.get("caption", ""),
        "title": img.get("title") or img["alt"][:80],
        "description": img.get("description", ""),
    })
    return media


def image_block(media, img):
    alt = html.escape(img["alt"], quote=True)
    cap = img.get("caption")
    figcap = f'<figcaption class="wp-element-caption">{html.escape(cap)}</figcaption>' if cap else ""
    return (f'<!-- wp:image {{"id":{media["id"]},"sizeSlug":"large","linkDestination":"none"}} -->'
            f'<figure class="wp-block-image size-large"><img src="{media["source_url"]}" alt="{alt}" '
            f'class="wp-image-{media["id"]}"/>{figcap}</figure><!-- /wp:image -->')


def cmd_publish(post_json):
    pkg_dir = os.path.dirname(os.path.abspath(post_json))
    with open(post_json, encoding="utf-8") as f:
        pkg = json.load(f)
    with open(os.path.join(pkg_dir, pkg.get("content_file", "content.html")), encoding="utf-8") as f:
        content = f.read()

    cats = {c["name"].lower(): c["id"] for c in get_all("/categories?_fields=id,name", auth=True)}
    cat_id = cats.get(pkg["category"].lower())
    if not cat_id:
        raise WPError(f"unknown category '{pkg['category']}' (agent may not create categories)")

    existing = get_all("/tags?_fields=id,name,count", auth=True)
    existing.sort(key=lambda t: -t["count"])
    tag_ids, to_create = resolve_tags(pkg.get("tags", []), existing)
    for name in to_create:
        try:
            tag_ids.append(call("POST", "/tags", payload={"name": name})["id"])
        except WPError as e:
            # Same slug, different spelling (e.g. "AI-Agents"): WP returns the existing id.
            m = re.search(r'"term_id":\s*(\d+)', str(e))
            if not m:
                raise
            tag_ids.append(int(m.group(1)))

    featured_id, media_ids = None, []
    for img in pkg.get("images", []):
        media = upload_image(pkg_dir, img)
        media_ids.append(media["id"])
        if img["key"] == "featured":
            featured_id = media["id"]
        else:
            content = content.replace("{{IMG:%s}}" % img["key"], image_block(media, img))
    leftover = re.findall(r"\{\{IMG:[^}]+\}\}", content)
    if leftover:
        raise WPError(f"unreplaced image placeholders: {leftover}")

    meta = {
        "rank_math_title": pkg.get("seo_title", ""),
        "rank_math_description": pkg.get("meta_description", ""),
        "rank_math_focus_keyword": pkg.get("focus_keyword", ""),
    }
    if pkg.get("social_message"):
        meta[SOCIAL_MESSAGE_KEY] = pkg["social_message"]
    post = call("POST", "/posts", payload={
        "title": pkg["title"],
        "slug": pkg["slug"],
        "content": content,
        "excerpt": pkg.get("excerpt", ""),
        "status": "draft",  # hard rule: this agent never publishes
        "categories": [cat_id],
        "tags": tag_ids,
        "featured_media": featured_id or 0,
        "meta": meta,
    })

    for mid in media_ids:  # attach to the post so Media Library shows "Uploaded to"
        call("POST", f"/media/{mid}", payload={"post": post["id"]})

    saved = call("GET", f"/posts/{post['id']}?context=edit").get("meta", {})
    meta_ok = all(saved.get(k) == v for k, v in meta.items())
    result = {
        "post_id": post["id"],
        "status": post["status"],
        "edit_link": f"{SITE}/wp-admin/post.php?post={post['id']}&action=edit",
        "preview_link": post.get("link"),
        "featured_media": featured_id,
        "tag_ids": tag_ids,
        "rank_math_meta_saved": meta_ok,
    }
    with open(os.path.join(pkg_dir, "publish-result.json"), "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(json.dumps(result, indent=2))
    if not meta_ok:
        print("WARN: rank math meta was not saved; enter SEO fields manually (see REPORT.md)")
    return 0


def cmd_diff(post_id, pkg_dir):
    live = call("GET", f"/posts/{post_id}?context=edit")
    strip = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()
    with open(os.path.join(pkg_dir, "content.html"), encoding="utf-8") as f:
        ours = strip(f.read())
    theirs = strip(live["content"]["raw"])
    ratio = difflib.SequenceMatcher(None, ours.split(), theirs.split()).ratio()
    print(f"status={live['status']} similarity={ratio:.2%} (>=90% means light edits)")
    return 0


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    cmd, args = argv[0], argv[1:]
    try:
        return {
            "check": lambda: cmd_check(),
            "inventory": lambda: cmd_inventory(),
            "publish": lambda: cmd_publish(*args),
            "diff": lambda: cmd_diff(*args),
        }[cmd]()
    except WPError as e:
        print("ERROR:", e, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
