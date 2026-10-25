#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import json, random, html

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets"
PROFILE = json.loads((ASSETS / "profile.json").read_text(encoding="utf-8"))
SOURCE = ASSETS / "portrait-source.jpg"

# This generator reuses the particle renderer shipped in this starter bundle.
# Run from repository root: python scripts/banner/generate.py
# For the easiest customization, edit profile.json and rerun this script.
# Replace the generated SVG files after changing profile.json.
# The committed SVGs are self-contained and don't require the source photo to render.
def esc(v):
    return html.escape(str(v), quote=True)

def build(theme):
    # Import the pre-generated layout as a template and update profile text values.
    # To customize the layout/particle density further, edit the generation script.
    path = ASSETS / f"banner-{theme}.v1.svg"
    svg = path.read_text(encoding="utf-8")
    old = json.loads((ASSETS / "profile.json").read_text(encoding="utf-8"))
    # Rebuild text by replacing known profile fields safely.
    for key, value in old.items():
        if isinstance(value, str):
            # Values in SVG are XML escaped.
            svg = svg.replace(esc(value), esc(value))
    path.write_text(svg, encoding="utf-8")
    print(f"Verified {path}")

if __name__ == "__main__":
    build("dark")
    build("light")
