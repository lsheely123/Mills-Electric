#!/usr/bin/env python3
"""The two footer options that aren't AI photos, drawn locally (no credentials needed).

    line-drawing   a gold line drawing of a house's electrical service on graphite:
                   pole, service drop, meter, panel, branch circuits, standby generator
    engine-turned  the logos' engine-turned gold, pushed very dark, as a texture

Same slot rules as the photos (PROMPT.md): 21:9, subject centred in the upper third,
lower half calm and dark. Also writes preview-<name>.png, a rough mock of the footer
(clear top band, smoked-glass panel) for comparing options side by side.

Needs numpy, Pillow, shapely (for the shared texture). Run: python3 make_footer_art.py
"""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "../../../logos/_source/van-lettering"))
from rebuild_van_lettering import engine_turned  # noqa: E402

W, H = 2400, 1029            # 21:9
SS = 2                       # supersample for clean antialiased lines
# The drawing is laid out on a 2400-wide sheet, then scaled into the top band: in the
# footer only image y < ~290 clears the glass (cover-fit at 50% 45%, 200px band).
K, GY = 0.42, 280            # drawing scale, and where the ground line lands
GRAPHITE = (0x11, 0x11, 0x13)
GOLD = (0xDF, 0xAD, 0x37)
GOLD_300 = (0xEA, 0xC9, 0x7B)
GOLD_700 = (0x6E, 0x52, 0x12)


def line_drawing():
    img = Image.new("RGB", (W * SS, H * SS), GRAPHITE)
    d = ImageDraw.Draw(img)

    def P(*pts):
        return [(((x - W / 2) * K + W / 2) * SS, ((y - 760) * K + GY) * SS) for x, y in pts]

    def lw(w):
        return max(1, round(w * 0.7 * SS))

    def ln(pts, col=GOLD, w=3, dash=None):
        pts = P(*pts)
        if not dash:
            d.line(pts, fill=col, width=lw(w), joint="curve")
            return
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            n = max(1, int(np.hypot(x1 - x0, y1 - y0) / (dash * SS)))
            for k in range(0, n, 2):
                a, b = k / n, min(1, (k + 1) / n)
                d.line([(x0 + (x1 - x0) * a, y0 + (y1 - y0) * a),
                        (x0 + (x1 - x0) * b, y0 + (y1 - y0) * b)], fill=col, width=lw(w))

    def rect(x0, y0, x1, y1, col=GOLD, w=3):
        d.rectangle(P((x0, y0), (x1, y1)), outline=col, width=lw(w))

    def circ(x, y, r, col=GOLD, w=3, fill=None):
        d.ellipse(P((x - r, y - r), (x + r, y + r)), outline=col, width=lw(w), fill=fill)

    def dot(x, y, r=6, col=GOLD_300):
        d.ellipse(P((x - r, y - r), (x + r, y + r)), fill=col)

    # drafting grid
    for x in range(0, W, 32):
        d.line([(x * SS, 0), (x * SS, H * SS)], fill=(0x1B, 0x1A, 0x18), width=SS)
    for y in range(0, H, 32):
        d.line([(0, y * SS), (W * SS, y * SS)], fill=(0x1B, 0x1A, 0x18), width=SS)

    ground = 760
    ln([(-2400, ground), (W + 2400, ground)], GOLD_700, 2)

    # utility pole, crossarm, insulators, pole-top transformer
    px = 560
    ln([(px, 170), (px, ground)], GOLD, 4)
    ln([(px - 90, 215), (px + 90, 215)], GOLD, 4)
    for ix in (px - 75, px - 25, px + 25, px + 75):
        ln([(ix, 215), (ix, 196)], GOLD_300, 3)
        dot(ix, 192, 5)
    rect(px + 14, 250, px + 70, 330)
    ln([(px + 42, 250), (px + 42, 236)], GOLD, 3)
    ln([(px - 120, 196), (px - 75, 192)], GOLD_700, 2)     # primaries running off-frame
    ln([(px + 75, 192), (px + 900, 150)], GOLD_700, 2)

    # service drop: a sagging span from the pole to the house's mast head
    mx, my = 1010, 330
    t = np.linspace(0, 1, 60)
    sx = px + 42 + (mx - px - 42) * t
    sy = 300 + (my - 300) * t + 55 * np.sin(np.pi * t)
    ln(list(zip(sx, sy)), GOLD, 3)
    dot(mx, my)

    # the house: a centre-chimney colonial, gable roof in the upper third
    hx0, hx1, eave, peak = 980, 1420, 430, 250
    ln([(950, eave), (1200, peak), (1450, eave), (950, eave)], GOLD, 4)
    rect(hx0, eave, hx1, ground, GOLD, 4)
    rect(1180, 260, 1220, 330, GOLD, 3)                     # chimney (behind the ridge line)
    for wx in (1030, 1300):                                 # upstairs windows
        rect(wx, 470, wx + 70, 560, GOLD_300, 2)
        ln([(wx + 35, 470), (wx + 35, 560)], GOLD_700, 2)
    for wx in (1030, 1300):                                 # downstairs windows
        rect(wx, 620, wx + 70, 710, GOLD_300, 2)
        ln([(wx + 35, 620), (wx + 35, 710)], GOLD_700, 2)
    rect(1170, 630, 1230, ground, GOLD_300, 2)              # front door
    ln([(hx0, 590), (hx1, 590)], GOLD_700, 2)               # floor line
    ln([(hx0, ground), (hx0, 900), (hx1, 900), (hx1, ground)], GOLD_700, 2, dash=14)  # basement

    # mast, meter, conduit down to the panel in the basement
    ln([(mx, my), (mx, 500)], GOLD, 3)
    circ(mx, 522, 22)
    ln([(mx, 544), (mx, 810), (1050, 810)], GOLD, 3)
    rect(1050, 780, 1110, 880, GOLD, 3)
    for by in range(792, 872, 12):
        ln([(1062, by), (1098, by)], GOLD_300, 2)

    # branch circuits up through the walls to fixtures (ceiling light = circle with an X)
    def light(x, y):
        circ(x, y, 15, GOLD_300, 2)
        r = 10
        ln([(x - r, y - r), (x + r, y + r)], GOLD_300, 2)
        ln([(x - r, y + r), (x + r, y - r)], GOLD_300, 2)

    def outlet(x, y):
        circ(x, y, 11, GOLD_300, 2)
        ln([(x - 4, y - 5), (x - 4, y + 5)], GOLD_300, 2)
        ln([(x + 4, y - 5), (x + 4, y + 5)], GOLD_300, 2)

    run_col = (0xB9, 0x8A, 0x1E)
    ln([(1110, 800), (1140, 800), (1140, 600), (1260, 600)], run_col, 2)
    dot(1140, 600, 5)
    light(1105, 605)
    ln([(1140, 600), (1105, 605)], run_col, 2)
    light(1360, 605)
    ln([(1260, 600), (1345, 605)], run_col, 2)
    ln([(1110, 830), (1390, 830), (1390, 450), (1260, 450)], run_col, 2)
    dot(1390, 450, 5)
    light(1245, 452)
    ln([(1390, 450), (1395, 452)], run_col, 2)
    ln([(1140, 700), (1260, 700)], run_col, 2, dash=10)
    outlet(1275, 700)
    dot(1140, 700, 5)

    # standby generator on its pad, with the transfer feed underground to the panel
    rect(1620, 690, 1770, ground, GOLD, 3)
    for gx in range(1640, 1760, 16):
        ln([(gx, 705), (gx, 745)], GOLD_700, 2)
    ln([(1580, ground + 6), (1810, ground + 6)], GOLD_700, 3)
    ln([(1695, ground), (1695, 850), (1110, 850)], GOLD, 2, dash=14)
    dot(1695, 850, 5)

    # a dimension line over the house, drafting style
    ln([(980, 200), (1420, 200)], GOLD_700, 2)
    for x in (980, 1420):
        ln([(x, 188), (x, 212)], GOLD_700, 2)

    img = img.resize((W, H), Image.LANCZOS)
    a = np.asarray(img).astype(np.float32)
    # keep the lower half calm: fade the drawing back toward graphite under the glass
    fade = np.clip(1 - (np.arange(H) / H - 0.55) / 0.45 * 0.55, 0.45, 1)[:, None, None]
    bg = np.array(GRAPHITE, np.float32)
    a = bg + (a - bg) * fade
    return Image.fromarray(a.clip(0, 255).astype(np.uint8))


def engine_turned_dark():
    tex = engine_turned(H, W, tile=120)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    # a raking light across the top band, falling away into the dark lower half
    light = 0.26 * np.exp(-((xx - W * 0.5) / (W * 0.45)) ** 2) * np.clip(1.15 - yy / H, 0.2, 1)
    a = tex * (0.07 + light[..., None])
    return Image.fromarray(a.clip(0, 255).astype(np.uint8))


def footer_preview(photo, vw=1440, vh=700, top=200):
    """Rough footer mock: photo cover-fit at 50% 45%, the CSS darkening gradient, the glass panel."""
    s = max(vw / photo.width, vh / photo.height)
    ph = photo.resize((round(photo.width * s), round(photo.height * s)), Image.LANCZOS)
    x0 = (ph.width - vw) // 2
    y0 = round((ph.height - vh) * 0.45)
    bg = np.asarray(ph.crop((x0, y0, x0 + vw, y0 + vh))).astype(np.float32)
    g = np.interp(np.arange(vh) / vh, [0, 0.3, 1], [0.10, 0.35, 0.70])[:, None, None]
    bg = bg * (1 - g)
    out = Image.fromarray(bg.astype(np.uint8))
    px0, px1 = (vw - 1200) // 2, (vw + 1200) // 2
    glass = out.crop((px0, top, px1, vh - 48)).filter(ImageFilter.GaussianBlur(18))
    ga = np.asarray(glass).astype(np.float32) * 0.28 + np.array([11, 11, 12]) * 0.72
    out.paste(Image.fromarray(ga.astype(np.uint8)), (px0, top))
    d = ImageDraw.Draw(out)
    d.rounded_rectangle((px0, top, px1, vh - 48), 16, outline=(60, 60, 62), width=1)
    d.rectangle((0, 0, vw, 3), fill=GOLD)                    # the 4px gold top border
    for i, cx in enumerate((px0 + 48, px0 + 420, px0 + 650, px0 + 880)):  # stand-in text rows
        for r in range(5 if i else 3):
            d.rectangle((cx, top + 70 + r * 34, cx + (150 if i else 260), top + 80 + r * 34),
                        fill=(0x8A, 0x8A, 0x90))
    return out


def main():
    for name, make in (("line-drawing", line_drawing), ("engine-turned", engine_turned_dark)):
        im = make()
        im.save(os.path.join(HERE, f"{name}.png"), optimize=True)
        footer_preview(im).save(os.path.join(HERE, f"preview-{name}.png"), optimize=True)
        print(f"wrote {name}.png and preview-{name}.png")
    current = Image.open(os.path.join(HERE, "../../../../assets/footer-jobsite.jpg")).convert("RGB")
    footer_preview(current).save(os.path.join(HERE, "preview-current.png"), optimize=True)
    print("wrote preview-current.png")


if __name__ == "__main__":
    main()
