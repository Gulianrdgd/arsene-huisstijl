"""Build the logo SVGs in assets/logo/ from the Illustrator source.

Source: assets/logo/bron/arsene-logo.ai (five artboards: wordmark on
transparent, wordmark on paper, wordmark in paper colour, mark, mark on black).
Text is converted to outlines, so the SVGs do not need Geist installed.

    python3 -m pip install pymupdf
    python3 scripts/build-logos.py
"""

import re
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets/logo/bron/arsene-logo.ai"
OUT = ROOT / "assets/logo"

INK = "#14120f"
PAPER = "#f4f1e8"
TEAL_DEEP = "#06120f"
TEAL_FG = "#d9e8e4"


def clean(svg, fill=None):
    """Drop Illustrator/Inkscape layer metadata; optionally set the base fill.

    Unfilled shapes in the source are black by default; the base fill on the
    layer group recolours exactly those, and leaves the mint pin alone.
    """
    svg = svg.replace(' xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"', "")
    group = f'<g fill="{fill}">' if fill else "<g>"
    return svg.replace('<g inkscape:groupmode="layer" inkscape:label="Layer 1">', group)


def page_svg(doc, index, fill):
    """SVG of one artboard, cropped to its art box, text as paths."""
    page = doc[index]
    svg = page.get_svg_image(text_as_path=True)
    box = page.artbox
    view = f"{box.x0:.2f} {box.y0:.2f} {box.width:.2f} {box.height:.2f}"
    svg = re.sub(r'width="[^"]+" height="[^"]+" viewBox="[^"]+"',
                 f'width="{box.width:.0f}" height="{box.height:.0f}" viewBox="{view}"', svg, count=1)
    return clean(svg, fill)


def main():
    doc = pymupdf.open(SRC)
    files = {
        "arsene-wordmark-ink.svg": page_svg(doc, 0, INK),      # artboard 1
        "arsene-wordmark-paper.svg": page_svg(doc, 0, PAPER),  # artboard 1, as artboard 3
        "arsene-mark-ink.svg": page_svg(doc, 3, INK),          # artboard 4
        "arsene-mark-paper.svg": page_svg(doc, 3, PAPER),
    }

    # App icon / favicon: artboard 5 layout (mark on a full square), with the
    # square as a Teal Deep rounded square (radius 18%) and the "a" in Teal FG.
    icon = clean(doc[4].get_svg_image(text_as_path=True))
    square = '<path transform="matrix(1,0,0,-1,0,2048)" d="M0 0H2048V2048H0Z"/>'
    assert square in icon
    icon = icon.replace(square, f'<rect width="2048" height="2048" rx="369" fill="{TEAL_DEEP}"/>')
    icon = icon.replace('fill="#ffffff"', f'fill="{TEAL_FG}"')
    files["arsene-icon.svg"] = icon

    for name, svg in files.items():
        (OUT / name).write_text(svg)
        print("wrote", name)


if __name__ == "__main__":
    main()
