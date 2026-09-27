"""Generate one blog image with the OpenAI Images API.

Usage: python generate_image.py --prompt "..." --out path/to/file.png [--size 1536x1024] [--quality medium]
Env: OPENAI_API_KEY (required), OPENAI_IMAGE_MODEL (default gpt-image-2)
"""
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--size", default="1536x1024")
    ap.add_argument("--quality", default="medium", choices=["low", "medium", "high"])
    a = ap.parse_args()

    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        print("ERROR: OPENAI_API_KEY is not set", file=sys.stderr)
        return 2

    body = json.dumps({
        "model": os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-2"),
        "prompt": a.prompt,
        "size": a.size,
        "quality": a.quality,
        "n": 1,
    }).encode()
    req = urllib.request.Request(
        "https://api.openai.com/v1/images/generations", data=body, method="POST",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        print(f"ERROR {e.code}: {e.read().decode(errors='replace')[:500]}", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with open(a.out, "wb") as f:
        f.write(base64.b64decode(data["data"][0]["b64_json"]))
    print(a.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
