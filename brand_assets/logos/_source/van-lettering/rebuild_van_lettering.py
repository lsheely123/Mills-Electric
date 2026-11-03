#!/usr/bin/env python3
"""Rebuild the Mills van's side lettering as a clean logo.

Traced against reference-van-lettering.png (a crop of assets/mills-van.jpg):
every line and rule is placed by its measured left/right edge, baseline and cap
height in that crop, then set in Helvetica Bold stretched to fit. The van's
"Masters LIC. #11245A" line is left off on purpose (the site uses #A-12245).

Outputs (next to this script):
  van-lettering.svg                  flat vector master: brand gold over a merged red-800 shadow
  van-lettering-on-black.png         engine-turned gold leaf, black background
  van-lettering-transparent.png      same, transparent background
  van-lettering-check.png            reference vs rebuild, side by side
  van-name.svg / van-name-*.png      just "Mills Electric Inc." (no rules, town, phone or alarm line)
  van-name-web.png                   van-name at 960px (was the masthead logo, Nov 2026)


Needs numpy, Pillow, fontTools and shapely (pip install shapely).
Run: python3 rebuild_van_lettering.py
"""
import os

import numpy as np
from fontTools.pens.basePen import BasePen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTCollection
from PIL import Image, ImageDraw, ImageFont
from shapely import Polygon, box, unary_union
from shapely.affinity import translate

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = "/System/Library/Fonts/Helvetica.ttc"
FACE = 1  # Helvetica Bold

GOLD = "#DFAD37"       # brand gold-500, also the flat fill in the SVG
SHADOW = "#7E0103"     # brand red-800, the van's dark red back shadow
S = 4                  # raster scale over reference pixels
TILE = 34              # engine-turning swirl pitch, in reference pixels

# Measured from the reference crop: (text, left, right, baseline, cap height, shadow offset)
LINES = [
    ("Mills",          303,  717, 197, 132, 9),
    ("Electric",       403, 1128, 385, 145, 9),
    ("Brockton, MA",   175,  765, 500,  65, 6),
    ("586-2955",       855, 1280, 498,  68, 6),
    ("ALARM SYSTEMS",  380, 1122, 607,  66, 6),
]
# The stacked "Inc.": (text, centre x, baseline, cap height)
# The "I" is a serifed capital on the van, so it is drawn as three bars in RULES.
STACK = [("n", 1194, 340, 60), ("c.", 1206, 393, 60)]
# Rules and the serifed I: (x0, x1, y0, y1)
RULES = [(62, 262, 183, 201), (757, 1250, 177, 195),
         (145, 347, 577, 595), (1155, 1355, 567, 585)]
I_BARS = [(1179, 1207, 225, 231), (1187, 1199, 225, 287), (1179, 1207, 281, 287)]
RULE_SHADOW = 6
CROP = (40, 45, 1380, 625)  # x0, y0, x1, y1 in reference pixels

# The name only, cropped tight (briefly the masthead logo, Nov 2026)
NAME_CROP = (284, 55, 1247, 409)
WEB_LOGO = os.path.join(HERE, "van-name-web.png")
WEB_LOGO_W = 240       # the display width it was designed for; exported at 4x

tt = TTCollection(FONT).fonts[FACE]
UPEM = tt["head"].unitsPerEm
CAP = tt["OS/2"].sCapHeight
glyphs = tt.getGlyphSet()
cmap = tt.getBestCmap()
hmtx = tt["hmtx"]


def layout(text):
    """Pen x (font units) for each glyph, plus ink left/right of the whole run."""
    x, out, ink_l, ink_r = 0, [], None, None
    for ch in text:
        g = cmap[ord(ch)]
        adv, lsb = hmtx[g]
        bounds = None
        if ch != " ":
            bp = BoundsPen(glyphs)
            glyphs[g].draw(bp)
            bounds = bp.bounds
        if bounds:
            ink_l = x + bounds[0] if ink_l is None else ink_l
            ink_r = x + bounds[2]
        out.append((ch, g, x))
        x += adv
    return out, ink_l, ink_r


def placements(lines):
    """Every glyph as (char, glyph, font-unit scale k, x-stretch, ox, baseline, shadow)."""
    items = []
    for text, left, right, base, cap, sh in lines:
        run, il, ir = layout(text)
        k = cap / CAP
        sx = (right - left) / ((ir - il) * k)
        ox = left - il * k * sx
        for ch, g, px in run:
            items.append((ch, g, k, sx, ox + px * k * sx, base, sh))
    for text, cx, base, cap in STACK:
        run, il, ir = layout(text)
        k = cap / CAP
        ox = cx - (il + ir) / 2 * k
        for ch, g, px in run:
            items.append((ch, g, k, 1.0, ox + px * k, base, 6))
    return items


class FlattenPen(BasePen):
    """Collects a glyph's contours as point lists, curves sampled finely."""

    def __init__(self, glyphset, steps=24):
        super().__init__(glyphset)
        self.contours, self.cur, self.steps = [], [], steps

    def _moveTo(self, p):
        self.cur = [p]

    def _lineTo(self, p):
        self.cur.append(p)

    def _curveToOne(self, p1, p2, p3):
        p0 = self.cur[-1]
        for i in range(1, self.steps + 1):
            t = i / self.steps
            u = 1 - t
            self.cur.append(tuple(u**3 * a + 3 * u * u * t * b + 3 * u * t * t * c + t**3 * d
                                  for a, b, c, d in zip(p0, p1, p2, p3)))

    def _closePath(self):
        if len(self.cur) > 2:
            self.contours.append(self.cur)
        self.cur = []

    _endPath = _closePath


def extrude(shape, d):
    """The solid swept by `shape` moving along vector d (an exact Minkowski sum with a segment)."""
    parts = [shape, translate(shape, *d)]
    polys = getattr(shape, "geoms", [shape])
    for poly in polys:
        for ring in [poly.exterior, *poly.interiors]:
            c = list(ring.coords)
            parts += [Polygon([a, b, (b[0] + d[0], b[1] + d[1]), (a[0] + d[0], a[1] + d[1])]).buffer(0)
                      for a, b in zip(c, c[1:])]
    return unary_union(parts)


def svg_path(geom):
    """Shapely geometry to an SVG path (each ring closed; draw with fill-rule evenodd)."""
    out = []
    for poly in getattr(geom, "geoms", [geom]):
        for ring in [poly.exterior, *poly.interiors]:
            pts = list(ring.coords)[:-1]
            out.append("M" + " L".join(f"{x:.2f} {y:.2f}" for x, y in pts) + "Z")
    return "".join(out)


def write_svg(items, rules, crop, name):
    """Gold faces keep the font's real curves; the shadow is one merged extruded outline."""
    x0, y0, x1, y1 = crop
    w, h = x1 - x0, y1 - y0
    fronts, shadows = [], []
    for ch, g, k, sx, ox, base, sh in items:
        if ch == " ":
            continue
        xf = (k * sx, 0, 0, -k, ox - x0, base - y0)
        pen = SVGPathPen(glyphs)
        glyphs[g].draw(TransformPen(pen, xf))
        fronts.append(pen.getCommands())
        flat = FlattenPen(glyphs)
        glyphs[g].draw(TransformPen(flat, xf))
        shape = Polygon()
        for c in flat.contours:  # outer contours and counters alternate, so XOR builds the glyph
            shape = shape.symmetric_difference(Polygon(c).buffer(0))
        shadows.append(extrude(shape, (-sh, sh)))
    rects = []
    for r in rules:
        b = box(r[0] - x0, r[2] - y0, r[1] - x0, r[3] - y0)
        rects.append(f'<rect x="{r[0]-x0}" y="{r[2]-y0}" width="{r[1]-r[0]}" height="{r[3]-r[2]}"/>')
        shadows.append(extrude(b, (-RULE_SHADOW, RULE_SHADOW)))
    shadow = unary_union(shadows).simplify(0.02)
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w*2}" height="{h*2}">',
        "<title>Mills Electric Inc. van lettering</title>",
        f'<path id="shadow" fill="{SHADOW}" fill-rule="evenodd" d="{svg_path(shadow)}"/>',
        f'<g id="gold" fill="{GOLD}">',
        *[f'<path d="{d}"/>' for d in fronts],
        *rects,
        "</g>",
        "</svg>",
    ]
    with open(os.path.join(HERE, f"{name}.svg"), "w") as f:
        f.write("\n".join(svg) + "\n")


def raster_masks(items, rules, crop):
    """Gold and shadow coverage masks (float 0..1) at S x reference resolution."""
    x0, y0, x1, y1 = crop
    W, H = (x1 - x0) * S, (y1 - y0) * S
    gold = Image.new("L", (W, H), 0)
    shadow = Image.new("L", (W, H), 0)
    fonts = {}
    for ch, g, k, sx, ox, base, sh in items:
        if ch == " ":
            continue
        size = round(k * UPEM * S)
        font = fonts.setdefault(size, ImageFont.truetype(FONT, size, index=FACE))
        # draw the glyph on its own canvas, stretch it, then stamp it in place
        pad = size
        tile = Image.new("L", (size * 2, size * 2), 0)
        ImageDraw.Draw(tile).text((pad // 2, pad + pad // 4), ch, font=font, fill=255, anchor="ls")
        if sx != 1.0:
            tile = tile.resize((round(tile.width * sx), tile.height), Image.LANCZOS)
        px = round((ox - x0) * S - (pad // 2) * sx)
        py = round((base - y0) * S - (pad + pad // 4))
        gold.paste(255, (px, py), tile)
        for t in range(1, sh * S + 1):
            shadow.paste(255, (px - t, py + t), tile)
    dg, ds = ImageDraw.Draw(gold), ImageDraw.Draw(shadow)
    for r in rules:
        box = [(r[0] - x0) * S, (r[2] - y0) * S, (r[1] - x0) * S, (r[3] - y0) * S]
        dg.rectangle(box, fill=255)
        d = RULE_SHADOW * S
        ds.polygon([(box[0], box[1]), (box[2], box[1]), (box[2], box[3]),
                    (box[2] - d, box[3] + d), (box[0] - d, box[3] + d), (box[0] - d, box[1] + d)],
                   fill=255)
    return np.asarray(gold, np.float32) / 255, np.asarray(shadow, np.float32) / 255


def engine_turned(h, w, tile=TILE * S):
    """Engine-turned gold leaf: overlapping rows of circular brushed swirls.

    Each swirl reflects as a bow-tie of light (anisotropic highlight across the
    circular brush marks) with fine concentric streaks. Later swirls overlap
    earlier ones, which gives the fish-scale look of real engine turning.
    `tile` is the swirl pitch in output pixels (engine_turn_logos.py reuses this).
    """
    T = tile
    R = 0.72 * T
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    rng = np.random.default_rng(1979)
    best_order = np.full((h, w), -1.0, np.float32)
    b = np.zeros((h, w), np.float32)
    ci, cj = np.floor(xx / T), np.floor(yy / T)
    for di in (0, 1):
        for dj in (0, 1):
            i, j = ci + di, cj + dj
            cx, cy = i * T, j * T
            dx, dy = xx - cx, yy - cy
            r = np.hypot(dx, dy)
            inside = r < R
            order = j * 10000 + i
            take = inside & (order > best_order)
            th = np.arctan2(dy, dx)
            phase = (np.sin(i * 12.9898 + j * 78.233) * 43758.5453) % 1 * 0.5
            lobe = np.abs(np.cos(th - 0.6 + phase))      # bow-tie highlight
            streak = 0.5 + 0.5 * np.sin(r * 2.3 + (i * 7 + j * 13))  # concentric brush marks
            val = 0.50 + 0.38 * lobe ** 1.4 + 0.08 * streak
            val *= 1.0 - 0.10 * np.clip(r / R, 0, 1) ** 3  # a touch darker at the rim of each cup
            b = np.where(take, val, b)
            best_order = np.where(take, order, best_order)
    b += rng.normal(0, 0.025, b.shape).astype(np.float32)
    # gold ramp from the brand book: 700, 600, 500, 300, and a warm highlight
    stops = np.array([0.0, 0.3, 0.55, 0.8, 1.0], np.float32)
    cols = np.array([[0x6E, 0x52, 0x12], [0xB9, 0x8A, 0x1E], [0xDF, 0xAD, 0x37],
                     [0xEA, 0xC9, 0x7B], [0xFF, 0xF1, 0xC6]], np.float32)
    b = np.clip(b, 0, 1)
    rgb = np.stack([np.interp(b, stops, cols[:, c]) for c in range(3)], -1)
    return rgb


def write_rasters(items, rules, crop, name):
    gold, shadow = raster_masks(items, rules, crop)
    h, w = gold.shape
    texture = engine_turned(h, w)
    red = np.array([int(SHADOW[i:i + 2], 16) for i in (1, 3, 5)], np.float32)
    shadow = shadow * (1 - gold)
    rgb = texture * gold[..., None] + red * shadow[..., None]
    alpha = np.clip(gold + shadow, 0, 1)

    # transparent: un-premultiply so edges stay clean
    straight = np.where(alpha[..., None] > 0, rgb / np.maximum(alpha[..., None], 1e-6), 0)
    rgba = np.dstack([np.clip(straight, 0, 255), alpha * 255]).astype(np.uint8)
    transparent = Image.fromarray(rgba)
    transparent.save(os.path.join(HERE, f"{name}-transparent.png"), optimize=True)

    black = np.array([0x0B, 0x0B, 0x0C], np.float32)
    on_black = rgb + black * (1 - alpha[..., None])
    Image.fromarray(np.clip(on_black, 0, 255).astype(np.uint8)).save(
        os.path.join(HERE, f"{name}-on-black.png"), optimize=True)

    # side-by-side check against the photo, same crop and scale
    ref = Image.open(os.path.join(HERE, "reference-van-lettering.png")).convert("RGB").crop(crop)
    ours = Image.fromarray(np.clip(on_black, 0, 255).astype(np.uint8)).resize(ref.size, Image.LANCZOS)
    check = Image.new("RGB", (ref.width, ref.height * 2 + 10), (60, 60, 60))
    check.paste(ref, (0, 0))
    check.paste(ours, (0, ref.height + 10))
    check.save(os.path.join(HERE, f"{name}-check.png"))
    return transparent


if __name__ == "__main__":
    full = placements(LINES)
    write_svg(full, RULES + I_BARS, CROP, "van-lettering")
    write_rasters(full, RULES + I_BARS, CROP, "van-lettering")

    name = placements(LINES[:2])  # Mills, Electric, and the stacked Inc.
    write_svg(name, I_BARS, NAME_CROP, "van-name")
    logo = write_rasters(name, I_BARS, NAME_CROP, "van-name")
    w = WEB_LOGO_W * 4
    logo.resize((w, round(logo.height * w / logo.width)), Image.LANCZOS).save(WEB_LOGO, optimize=True)
    print("wrote van-lettering.*, van-name.* and van-name-web.png")
