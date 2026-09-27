"""Human-voice linter for a Gutenberg content.html file.

Usage: python voice_check.py outputs/YYYY-MM-DD_slug/content.html
Exit code 1 if banned phrases are found or rhythm is too uniform.
Rules mirror data/STYLE_GUIDE.md -> "Insan Sesi".
"""
import html
import re
import statistics
import sys

BANNED = [
    "delve", "tapestry", "landscape", "realm", "robust", "seamless", "seamlessly",
    "leverage", "harness", "elevate", "empower", "ever-evolving", "crucial", "pivotal",
    "game-changer", "game changer", "revolutionize", "unlock the power",
    "in today's fast-paced", "let's dive in", "dive into", "buckle up",
    "in this article we will", "whether you're a beginner", "navigate the complexities",
    "moreover", "furthermore", "additionally", "in conclusion",
    "it's worth noting", "it is worth noting", "it's important to remember",
    "may potentially", "can help to",
]
# "It's not X, it's Y" / "isn't about X. It's about Y"
CONTRAST = re.compile(r"\b(it'?s|this is|that'?s) not (just |only |about )?[^.?!]{1,60}[,;.] (it'?s|but)\b", re.I)
MAX_EM_DASH = 3


def prose(raw: str) -> str:
    raw = re.sub(r"<pre.*?</pre>", " ", raw, flags=re.S)  # code is not prose
    raw = re.sub(r"<!--.*?-->", " ", raw, flags=re.S)
    raw = re.sub(r"</(p|h\d|li|td|th|figcaption)>", ".\n", raw)
    return html.unescape(re.sub(r"<[^>]+>", " ", raw))


def main(path: str) -> int:
    text = prose(open(path, encoding="utf-8").read())
    low = text.lower()
    problems = []

    for word in BANNED:
        n = len(re.findall(r"\b" + re.escape(word) + r"\b", low))
        if n:
            problems.append(f"banned '{word}' x{n}")
    for m in CONTRAST.finditer(text):
        problems.append(f"contrast pattern: '{m.group(0)[:70]}'")

    dashes = text.count("—")
    if dashes > MAX_EM_DASH:
        problems.append(f"em dash x{dashes} (max {MAX_EM_DASH})")

    # Rhythm is measured on paragraph prose only; headings/list items would skew it.
    raw = open(path, encoding="utf-8").read()
    paras = " ".join(prose(p) for p in re.findall(r"<p[ >].*?</p>", raw, flags=re.S))
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", paras) if len(s.split()) >= 2]
    lengths = [len(s.split()) for s in sentences]
    flat_runs = sum(
        1 for i in range(len(lengths) - 2)
        if max(lengths[i:i + 3]) - min(lengths[i:i + 3]) <= 2
    )
    stdev = statistics.pstdev(lengths) if lengths else 0
    short = sum(1 for n in lengths if n <= 6)

    print(f"sentences={len(lengths)} mean_len={statistics.mean(lengths):.1f} "
          f"stdev={stdev:.1f} short(<=6w)={short} flat_triplets={flat_runs} em_dash={dashes}")
    if stdev < 6:
        problems.append(f"rhythm too uniform (stdev {stdev:.1f} < 6)")
    if lengths and short / len(lengths) < 0.08:
        problems.append("too few short punchy sentences (<8%)")
    if lengths and flat_runs / len(lengths) > 0.15:
        problems.append(f"too many same-length sentence triplets ({flat_runs})")

    for p in problems:
        print("FAIL:", p)
    print("PASS" if not problems else f"{len(problems)} issue(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
