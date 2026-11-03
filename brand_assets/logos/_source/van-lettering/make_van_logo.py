#!/usr/bin/env python3
"""Recreate the Mills Electric van lettering as a clean, flat logo with Higgsfield.

Credentials come from the environment only (never printed):
    HF_KEY="key-id:key-secret"            or
    HF_API_KEY="key-id"  HF_API_SECRET="key-secret"

Usage:
    pip install higgsfield-client  # once
    python3 make_van_logo.py [--n 2] [--model bytedance/seedream/v4/edit]
Outputs go to <site>/brand_assets/logos/_source/van-lettering/ (source art, never published).
"""
import argparse
import datetime
import os
import pathlib
import sys
import urllib.request

import higgsfield_client as hf

HERE = pathlib.Path(__file__).resolve().parent
SITE = pathlib.Path("/Users/logansheely/Mills Electric Site")
OUT = HERE
REF = HERE / "reference-van-lettering.png"   # tight, enlarged crop of assets/mills-van.jpg

PROMPT = (
    "Recreate the gold vehicle lettering in this reference photo as a clean, flat, "
    "perfectly front-facing logo on a plain solid black background. No van, no window, "
    "no reflections, no perspective, no photo texture. Keep the exact wording, layout "
    "and bold sans-serif type style of the reference: the word 'Mills' on the first line "
    "with a long gold horizontal rule to its left and right; 'Electric' large on the "
    "second line with a small vertically stacked 'Inc.' to its right; then "
    "'Brockton, MA' and '586-2955' on one line; then 'ALARM SYSTEMS' with a gold rule on "
    "each side. Do not include the 'Masters LIC.' line. Every letter and rule is radial "
    "brushed gold leaf (engine-turned gold: rows of small circular brushed swirls with a "
    "bright metallic sheen), with a solid dark red drop shadow offset down and to the "
    "left behind every letter and rule, exactly like the reference. Crisp, sharp edges, "
    "centred, high resolution, sign-painter quality, spelling exactly as given."
)

# Field names differ between hosted Seedream variants; try the common ones in order.
IMAGE_FIELDS = ("image_urls", "input_images", "images", "image_url")


def creds_present():
    return bool(os.environ.get("HF_KEY") or
                (os.environ.get("HF_API_KEY") and os.environ.get("HF_API_SECRET")))


def run(model, ref_url, n):
    last = None
    for field in IMAGE_FIELDS:
        value = ref_url if field == "image_url" else [ref_url]
        args = {"prompt": PROMPT, field: value, "resolution": "2K", "aspect_ratio": "16:9"}
        if n > 1:
            args["num_images"] = n
        try:
            print(f"submitting to {model} (reference field '{field}') ...", flush=True)
            return hf.subscribe(model, arguments=args), field
        except hf.HiggsfieldClientError as e:          # validation errors: try next field name
            last = e
            msg = str(e)
            print(f"  rejected: {msg[:300]}", flush=True)
            if "credit" in msg.lower() or "auth" in msg.lower() or "401" in msg or "403" in msg:
                break
    raise SystemExit(f"Higgsfield rejected every request shape; last error: {last}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="bytedance/seedream/v4/edit")
    ap.add_argument("--n", type=int, default=2)
    a = ap.parse_args()

    if not creds_present():
        sys.exit("No Higgsfield credentials in the environment. Set HF_KEY "
                 "(key-id:key-secret) or HF_API_KEY + HF_API_SECRET, then rerun.")
    if not REF.exists():
        sys.exit(f"missing reference image {REF}")

    OUT.mkdir(parents=True, exist_ok=True)
    print("uploading reference crop ...", flush=True)
    ref_url = hf.upload_file(str(REF))
    result, field = run(a.model, ref_url, a.n)

    images = result.get("images") or []
    if not images:
        sys.exit(f"finished but returned no images: {list(result)}")
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    for i, img in enumerate(images, 1):
        url = img["url"] if isinstance(img, dict) else img
        ext = os.path.splitext(url.split("?")[0])[1] or ".png"
        dest = OUT / f"van-lettering-{stamp}-{i}{ext}"
        urllib.request.urlretrieve(url, dest)
        print(f"saved {dest}")
    (OUT / f"van-lettering-{stamp}-prompt.txt").write_text(
        f"model: {a.model}\nreference field: {field}\nreference: {REF.name}\n\n{PROMPT}\n")


if __name__ == "__main__":
    main()
