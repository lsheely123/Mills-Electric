#!/usr/bin/env python3
"""Give the site's other logos the van's engine-turned gold.

Only the gold regions change (picked by hue and saturation); the white M and
wordmark, the red bolt and INC, and the alpha are left exactly as they were. The
flat brand-kit masters in brand_assets/logos/ are read, never written: the brand book
keeps brushed gold for print and signage, so the flat versions stay canonical.

Writes, in assets/logos/:
  reversed-logo-on-black.png   footer lockup + JSON-LD logo, 660x382 (4x the 165px display)
  favicon-32/180/192/512.png   the mark on #0B0B0C, same placement as before
  me-mark-gold.png             the mark alone, transparent: the masthead logo, 384px (4x the 96px display)

Needs numpy, Pillow (and the shapely import in rebuild_van_lettering.py).
Run: python3 engine_turn_logos.py
"""
import os

import numpy as np
from PIL import Image

from rebuild_van_lettering import engine_turned

HERE = os.path.dirname(os.path.abspath(__file__))
LOGOS = os.path.join(HERE, "..", "..")              # brand_assets/logos
SITE = os.path.join(HERE, "../../../../assets/logos")
TILE = 110         # swirl pitch in master pixels: about the masthead logo's density at display size
BLACK = (0x0B, 0x0B, 0x0C)
# favicon size -> side margin around the mark's ink, matching the flat icons they replace
FAVICONS = {32: 1, 180: 14, 192: 14, 512: 40}


def gold_weight(rgb):
    """0..1 per pixel: how much of it is the logo's gold (hue ~30-60deg, clearly saturated)."""
    r, g, b = (rgb[..., i] / 255 for i in range(3))
    mx, mn = np.maximum(np.maximum(r, g), b), np.minimum(np.minimum(r, g), b)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    hue = np.degrees(np.arctan2(np.sqrt(3) * (g - b), 2 * r - g - b)) % 360
    hue_w = np.clip((hue - 22) / 8, 0, 1) * np.clip((68 - hue) / 8, 0, 1)
    return hue_w * np.clip((sat - 0.25) / 0.15, 0, 1)


def retexture(path):
    im = np.asarray(Image.open(path).convert("RGBA")).astype(np.float32)
    rgb, alpha = im[..., :3], im[..., 3:]
    w = gold_weight(rgb)[..., None]
    out = rgb * (1 - w) + engine_turned(*rgb.shape[:2], tile=TILE) * w
    return Image.fromarray(np.dstack([np.clip(out, 0, 255), alpha]).astype(np.uint8))


def main():
    lockup = retexture(os.path.join(LOGOS, "me-primary-reversed.png"))
    lockup.resize((660, 382), Image.LANCZOS).save(
        os.path.join(SITE, "reversed-logo-on-black.png"), optimize=True)

    mark = retexture(os.path.join(LOGOS, "me-mark-reversed.png"))
    mark = mark.crop(mark.getchannel("A").getbbox())
    mark.resize((384, round(mark.height * 384 / mark.width)), Image.LANCZOS).save(
        os.path.join(SITE, "me-mark-gold.png"), optimize=True)
    for size, margin in FAVICONS.items():
        mw = size - 2 * margin
        mh = round(mark.height * mw / mark.width)
        icon = Image.new("RGBA", (size, size), BLACK + (255,))
        icon.alpha_composite(mark.resize((mw, mh), Image.LANCZOS), (margin, (size - mh) // 2))
        icon.convert("RGB").save(os.path.join(SITE, f"favicon-{size}.png"), optimize=True)
    print("wrote reversed-logo-on-black.png, me-mark-gold.png and favicon-32/180/192/512.png")


if __name__ == "__main__":
    main()
