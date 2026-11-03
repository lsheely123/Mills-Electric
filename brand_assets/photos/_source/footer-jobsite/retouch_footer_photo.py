#!/usr/bin/env python3
"""Fix the AI lettering in "Mills Truck 2" (the footer photo) and export it.

  1. Paint out the garbled licence line ("MASTER LIC. A-13805"); the real number is #A-12245
     and the line shows beside the footer glass on wide screens.
  2. Replace the squiggle after "Electric" with "Inc." in stacked letters, as on the real van
     (see the hero photo, brand_assets/photos/_source/hero/mills-site-home.png).

Reads mills-truck-2.png (as delivered), writes mills-truck-2-retouched.png and
assets/footer-jobsite.jpg. Run: python3 retouch_footer_photo.py
"""
import os

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(HERE, "../../../..")
FILL = (250, 228, 181)       # the lettering's cream gold, sampled from "Electric"
SS = 8                       # supersample for the new letters


def lettering_mask(box):
    r, b = box[..., 0], box[..., 2]
    m = Image.fromarray((((r > 70) & (r - b > 25)) * 255).astype(np.uint8))
    return np.asarray(m.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(1.2)),
                      np.float32)[..., None] / 255


def erase(a, x0, x1, y0, y1, left=True, rng=np.random.default_rng(0)):
    """Fill the lettering in a box from the clean paint either side, row by row: the
    reflections on the van's side run in horizontal bands."""
    box = a[y0:y1, x0:x1]
    R = a[y0:y1, x1:x1 + 3].mean(1)
    L = a[y0:y1, x0 - 3:x0].mean(1) if left else R
    t = (np.arange(x1 - x0) / max(1, x1 - x0 - 1))[None, :, None]
    fill = L[:, None] * (1 - t) + R[:, None] * t + rng.normal(0, 1.5, box.shape)
    soft = lettering_mask(box)
    box[:] = box * (1 - soft) + fill * soft


def stacked_inc(a, cx, top, bottom):
    """Draw I / n / c. stacked and centred on cx, spanning top..bottom like the real van."""
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 12 * SS, index=1)
    h = (bottom - top) * SS
    w = 16 * SS
    layer = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(layer)
    cap = font.getbbox("I")[3] - font.getbbox("I")[1]
    xh = font.getbbox("n")[3] - font.getbbox("n")[1]
    gap = (h - cap - 2 * xh) / 2
    for text, base in (("I", cap), ("n", cap + gap + xh), ("c.", h)):
        d.text((w / 2, base), text, font=font, fill=255, anchor="ms",
               stroke_width=SS // 3, stroke_fill=255)   # a touch heavier, like the van
    layer = layer.resize((w // SS, (bottom - top)), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.35))
    alpha = np.asarray(layer, np.float32)[..., None] / 255
    x0 = round(cx - w / SS / 2)
    reg = a[top:bottom, x0:x0 + w // SS]
    reg[:] = reg * (1 - alpha) + np.array(FILL, np.float32) * alpha


def main():
    a = np.asarray(Image.open(os.path.join(HERE, "mills-truck-2.png")).convert("RGB")).astype(np.float32)
    erase(a, 1146, 1240, 417, 438)                 # "MASTER LIC. A-13805"
    erase(a, 1273, 1288, 333, 364, left=False)     # the squiggle; its left edge is the "c"
    stacked_inc(a, 1280, 334, 361)                 # the I starts just under the rule; c. sits on the baseline
    out = Image.fromarray(a.clip(0, 255).astype(np.uint8))
    out.save(os.path.join(HERE, "mills-truck-2-retouched.png"), optimize=True)
    out.save(os.path.join(SITE, "assets/footer-jobsite.jpg"), quality=82, optimize=True, progressive=True)
    print("wrote mills-truck-2-retouched.png and assets/footer-jobsite.jpg")


if __name__ == "__main__":
    main()
