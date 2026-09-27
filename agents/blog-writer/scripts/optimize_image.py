"""Squoosh-equivalent image optimizer: resize + WebP (libwebp) or progressive JPEG.

Squoosh (installed as a Chrome PWA) has no CLI; its WebP encoder is libwebp, the same
library Pillow uses, so quality 75 / method 6 here matches Squoosh's WebP defaults.

Output format follows the extension. Use .jpg for the featured image: Instagram
(via Jetpack Social) only accepts JPEG.

Usage: python optimize_image.py in.png out.webp|out.jpg [--max-width 1200] [--quality 75]
"""
import argparse
import os
import sys

from PIL import Image


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--max-width", type=int, default=1200)
    ap.add_argument("--quality", type=int, default=75)
    ap.add_argument("--max-kb", type=int, default=150, help="lower quality stepwise until under this size")
    a = ap.parse_args()

    img = Image.open(a.src).convert("RGB")  # drops alpha + all metadata
    if img.width > a.max_width:
        img = img.resize((a.max_width, round(img.height * a.max_width / img.width)), Image.LANCZOS)

    q = a.quality
    while True:
        if a.dst.lower().endswith((".jpg", ".jpeg")):
            img.save(a.dst, "JPEG", quality=q + 7, optimize=True, progressive=True)
        else:
            img.save(a.dst, "WEBP", quality=q, method=6)
        kb = os.path.getsize(a.dst) / 1024
        if kb <= a.max_kb or q <= 55:
            break
        q -= 5

    before = os.path.getsize(a.src) / 1024
    print(f"{os.path.basename(a.dst)}: {img.width}x{img.height} q={q} "
          f"{before:.0f}KB -> {kb:.0f}KB (-{100 - kb / before * 100:.0f}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
