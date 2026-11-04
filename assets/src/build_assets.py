"""Builds the profile README images (dark + light variants).

    python assets/src/build_assets.py      # needs Pillow

Outputs into assets/: banner-*.svg, esco-stats-*.svg, esco-pipeline-*.svg,
avatar.png, app-*.png.
"""

from __future__ import annotations

import base64
import io
import math
from pathlib import Path

from PIL import Image, ImageDraw

SRC = Path(__file__).resolve().parent
OUT = SRC.parent
ACCENT = "#F26B1D"
FONT = "font-family=\"-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif\""
MONO = "font-family=\"ui-monospace, SFMono-Regular, Menlo, Consolas, monospace\""

THEMES = {
    "dark": dict(bg="#0d1117", card="#161b22", line="#30363d", fg="#e6edf3", mute="#8b949e", grid="#21262d"),
    "light": dict(bg="#ffffff", card="#f6f8fa", line="#d0d7de", fg="#1f2328", mute="#59636e", grid="#e6e9ec"),
}


def svg(w: int, h: int, body: str, label: str) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" '
            f'height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">\n{body}\n</svg>\n')


def photo_data_uri(size: int = 360) -> str:
    im = Image.open(SRC / "photo.png").convert("RGB").resize((size, size), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=86, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


# -- banner -----------------------------------------------------------------------------

def banner(t: dict) -> str:
    W, H = 1200, 320
    cx, cy, r = 150, 160, 92
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="1.3" fill="{t["grid"]}"/>'
                   for x in range(900, 1200, 26) for y in range(22, 320, 26))
    tx, ty = 1088, 150
    ring = (f'<circle cx="{tx}" cy="{ty}" r="18" fill="none" stroke="{t["mute"]}" stroke-width="1.5"/>'
            f'<circle cx="{tx}" cy="{ty}" r="2.5" fill="{t["mute"]}"/>')
    for a in (0, 90, 180, 270):
        c, s = math.cos(math.radians(a)), math.sin(math.radians(a))
        ring += (f'<line x1="{tx + 24 * c:.1f}" y1="{ty + 24 * s:.1f}" x2="{tx + 32 * c:.1f}" '
                 f'y2="{ty + 32 * s:.1f}" stroke="{t["mute"]}" stroke-width="1.5"/>')
    flight = (f'<rect x="916" y="52" width="250" height="216" fill="none" stroke="{t["mute"]}" '
              f'stroke-width="1" stroke-dasharray="2 5" opacity="0.6"/>'
              f'<path d="M940 248 C 960 110, 1010 70, 1052 122" fill="none" stroke="{ACCENT}" stroke-width="2" '
              f'stroke-dasharray="6 7" stroke-linecap="round"/>'
              f'<g transform="translate(1056,128) rotate(52)"><path d="M12 0 L-8 -8 L-3 0 L-8 8 Z" fill="{ACCENT}"/></g>')
    photo = (f'<defs><clipPath id="pc"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath></defs>'
             f'<circle cx="{cx}" cy="{cy}" r="{r + 5}" fill="none" stroke="{ACCENT}" stroke-width="3"/>'
             f'<image href="{photo_data_uri()}" x="{cx - r}" y="{cy - r}" width="{2 * r}" height="{2 * r}" '
             f'clip-path="url(#pc)" preserveAspectRatio="xMidYMid slice"/>')
    x = 290
    text = (f'<text x="{x}" y="128" {FONT} font-size="50" font-weight="700" fill="{t["fg"]}" '
            f'letter-spacing="-0.5">Gencay Coşkun</text>'
            f'<text x="{x}" y="172" {FONT} font-size="21" fill="{t["mute"]}">Computer Engineering @ Sakarya University</text>'
            f'<text x="{x}" y="204" {FONT} font-size="21" fill="{t["mute"]}">Platform Analyst @ Duosis · Captain @ ESCO-UAV</text>'
            f'<rect x="{x}" y="232" width="28" height="3" fill="{ACCENT}"/>'
            f'<text x="{x + 40}" y="238" {FONT} font-size="13.5" font-weight="600" fill="{ACCENT}" '
            f'letter-spacing="1.6">AUTONOMOUS UAVS · COMPUTER VISION · PRODUCT ENGINEERING</text>')
    body = f'<rect width="{W}" height="{H}" rx="16" fill="{t["bg"]}"/>{dots}{flight}{ring}{photo}{text}'
    return svg(W, H, body, "Gencay Coşkun — Computer Engineering, Platform Analyst at Duosis, Captain of ESCO-UAV")


# -- ESCO stats --------------------------------------------------------------------------

STATS = [
    ("41,891", "images in the", "detector training set"),
    ("96.5 %", "detection rate", "(YOLO11)"),
    ("0", "false locks", "in validation"),
    ("SITL", "lock-on guidance", "validated end to end"),
]


def stats(t: dict) -> str:
    W, H, gap = 1200, 150, 16
    w = (W - gap * 3) / 4
    body = ""
    for i, (big, l1, l2) in enumerate(STATS):
        x = i * (w + gap)
        body += (f'<rect x="{x + 1:.1f}" y="1" width="{w - 2:.1f}" height="{H - 2}" rx="12" fill="{t["card"]}" '
                 f'stroke="{t["line"]}"/>'
                 f'<rect x="{x + 24:.1f}" y="26" width="22" height="3" fill="{ACCENT}"/>'
                 f'<text x="{x + 24:.1f}" y="78" {FONT} font-size="40" font-weight="700" fill="{t["fg"]}">{big}</text>'
                 f'<text x="{x + 24:.1f}" y="108" {FONT} font-size="16" fill="{t["mute"]}">{l1}</text>'
                 f'<text x="{x + 24:.1f}" y="129" {FONT} font-size="16" fill="{t["mute"]}">{l2}</text>')
    return svg(W, H, body, "41,891 training images, 96.5% detection, 0 false locks in validation, guidance validated in SITL")


# -- ESCO pipeline -----------------------------------------------------------------------

def pipeline(t: dict) -> str:
    W, H = 1200, 312
    bw, bh = 150, 56

    def box(x, y, title, sub, hot=False):
        stroke = ACCENT if hot else t["line"]
        return (f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="10" fill="{t["card"]}" stroke="{stroke}" '
                f'stroke-width="{1.6 if hot else 1}"/>'
                f'<text x="{x + bw / 2}" y="{y + 25}" text-anchor="middle" {FONT} font-size="15" font-weight="600" '
                f'fill="{t["fg"]}">{title}</text>'
                f'<text x="{x + bw / 2}" y="{y + 44}" text-anchor="middle" {MONO} font-size="11.5" '
                f'fill="{t["mute"]}">{sub}</text>')

    def arrow(x1, y1, x2, y2):
        return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{t["mute"]}" stroke-width="1.5" '
                f'marker-end="url(#ah)"/>')

    defs = (f'<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{t["mute"]}"/></marker></defs>')
    # row 1: on board, the lock-on loop
    xs = [20 + i * (bw + 46) for i in range(6)]
    y1, y2 = 58, 206
    row1 = [("Camera", "video"), ("Detector", "YOLO11 · ONNX"), ("Tracker", "target select"),
            ("Guidance", "pursuit · gates"), ("MAVLink", "attitude cmds"), ("ArduPilot", "flight control")]
    body = defs
    body += (f'<text x="20" y="36" {FONT} font-size="13" font-weight="600" letter-spacing="1.4" fill="{ACCENT}">'
             f'ON BOARD · LOCK-ON LOOP</text>')
    for i, (a, b) in enumerate(row1):
        body += box(xs[i], y1, a, b, hot=a in ("Detector", "Guidance"))
        if i:
            body += arrow(xs[i - 1] + bw + 4, y1 + bh / 2, xs[i] - 4, y1 + bh / 2)
    # row 2: telemetry to the ground
    body += (f'<text x="20" y="184" {FONT} font-size="13" font-weight="600" letter-spacing="1.4" fill="{ACCENT}">'
             f'TELEMETRY · GROUND</text>')
    body += box(xs[5], y2, "Companion", "Python agent")
    body += box(xs[3] + (bw + 46) / 2, y2, "Telemetry API", "FastAPI")
    body += box(xs[1] + (bw + 46) / 2, y2, "Ground station", "Next.js · live map")
    # ArduPilot -> companion (down), companion -> API, API -> GS
    body += arrow(xs[5] + bw / 2, y1 + bh + 4, xs[5] + bw / 2, y2 - 4)
    api_x = xs[3] + (bw + 46) / 2
    gs_x = xs[1] + (bw + 46) / 2
    body += arrow(xs[5] - 4, y2 + bh / 2, api_x + bw + 4, y2 + bh / 2)
    body += arrow(api_x - 4, y2 + bh / 2, gs_x + bw + 4, y2 + bh / 2)
    # API -> competition server (small tag under API)
    body += (f'<line x1="{api_x + bw / 2}" y1="{y2 + bh + 4}" x2="{api_x + bw / 2}" y2="{y2 + bh + 22}" '
             f'stroke="{t["mute"]}" stroke-width="1.5" marker-end="url(#ah)"/>'
             f'<text x="{api_x + bw / 2 + 10}" y="{y2 + bh + 30}" {FONT} font-size="12.5" fill="{t["mute"]}">'
             f'competition server (spec-compliant link)</text>')
    # GS -> permits back to guidance (dashed, operator in the loop)
    body += (f'<path d="M{gs_x + bw / 2} {y2 - 4} L{gs_x + bw / 2} {y2 - 34} L{xs[3] + bw / 2} {y2 - 34} '
             f'L{xs[3] + bw / 2} {y1 + bh + 6}" fill="none" stroke="{ACCENT}" stroke-width="1.4" '
             f'stroke-dasharray="5 5" marker-end="url(#ah)"/>'
             f'<text x="{gs_x + bw / 2 + 10}" y="{y2 - 42}" {FONT} font-size="12.5" fill="{ACCENT}">'
             f'operator permits · tasks</text>')
    return svg(W, H, f'<rect width="{W}" height="{H}" rx="16" fill="{t["bg"]}"/>' + body,
               "ESCO-UAV system: camera, YOLO11 detector, tracker, guidance, MAVLink, ArduPilot; "
               "telemetry via companion, FastAPI and a Next.js ground station")


# -- raster helpers ----------------------------------------------------------------------

def rounded(im: Image.Image, size: int, radius: float = 0.225) -> Image.Image:
    im = im.convert("RGBA").resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size * 4, size * 4), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size * 4 - 1, size * 4 - 1), radius=int(size * 4 * radius), fill=255)
    im.putalpha(mask.resize((size, size), Image.LANCZOS))
    return im


def app_icons() -> None:
    for name, crop in (("olympus", None), ("ballrows", (0.16, 0.15, 0.84, 0.83)), ("assetflow", None)):
        im = Image.open(SRC / f"{name}.png").convert("RGBA")
        if name == "assetflow":  # transparent logo: give it the App Store white tile
            tile = Image.new("RGBA", im.size, "#ffffff")
            tile.alpha_composite(im)
            im = tile
        if crop:
            w, h = im.size
            im = im.crop((int(crop[0] * w), int(crop[1] * h), int(crop[2] * w), int(crop[3] * h)))
        rounded(im, 200).save(OUT / f"app-{name}.png", optimize=True)


def avatar() -> None:
    Image.open(SRC / "photo.png").convert("RGB").save(OUT / "avatar.jpg", quality=92)


BRANDS = {  # out name -> source in src/brands/ ("-dark" = drawn for a dark background)
    "duosis": "duosis-{t}.svg",
    "hermes": "hermes-logo-{t}.png",
    "logislot": "logislot-logo-{t}.png",
    "drake": "drake-wordmark-{t}.webp",
}


def brand_logos(max_h: int = 120) -> None:
    """Trim the transparent margin and cap the height; never upscale."""
    import subprocess

    (OUT / "brands").mkdir(exist_ok=True)
    for name, pattern in BRANDS.items():
        for theme in ("dark", "light"):
            src = SRC / "brands" / pattern.format(t=theme)
            if src.suffix == ".svg":
                png = subprocess.run(["rsvg-convert", "-h", str(max_h * 2), str(src)], check=True,
                                     capture_output=True).stdout
                im = Image.open(io.BytesIO(png))
            else:
                im = Image.open(src)
            im = im.convert("RGBA")
            im = im.crop(im.getchannel("A").getbbox())
            if im.height > max_h:
                im = im.resize((round(im.width * max_h / im.height), max_h), Image.LANCZOS)
            im.save(OUT / "brands" / f"{name}-{theme}.png", optimize=True)


if __name__ == "__main__":
    for theme, t in THEMES.items():
        (OUT / f"banner-{theme}.svg").write_text(banner(t))
        (OUT / f"esco-stats-{theme}.svg").write_text(stats(t))
        (OUT / f"esco-pipeline-{theme}.svg").write_text(pipeline(t))
    app_icons()
    avatar()
    brand_logos()
    print("ok")
