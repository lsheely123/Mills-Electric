#!/usr/bin/env python3
"""Turn Charlie's phone photo of the van at the gravel lot into a hyper-realistic footer photo.

Credentials come from the environment only (never printed):
    HF_KEY="key-id:key-secret"            or
    HF_API_KEY="key-id"  HF_API_SECRET="key-secret"

Usage:
    pip install higgsfield-client  # once
    python3 make_footer_photo.py --concept stone-yard-rear [--n 2] [--model ...]
    python3 make_footer_photo.py --concept all --t2i-model <text-to-image model id>   # every concept
Outputs land here (source art, never published). Pick one, then export it to
assets/footer-jobsite.jpg (2400px wide, JPEG q82) and rebuild.
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
REF = HERE / "reference-van-gravel.png"   # Charlie's original, 886x378

VAN = (
    "Keep the same black Chevrolet Express work van as the reference, with the same yellow "
    "fibreglass extension ladders and aluminium ladder rack on the roof. "
)
COMMON = (
    "Wide 21:9 framing. Keep the main subject horizontally centred and in the upper third of "
        "the frame; the lower half calm, uncluttered and mid-to-dark. Hyper-realistic professional "
        "photograph, sharp detail, vivid but natural colour. No people's faces, no watermark, no "
        "text, no signs, no logos."
)
# name -> (prompt, uses the reference photo). See PROMPT.md for the thinking behind each.
CONCEPTS = {
    "stone-yard": (
        "Re-shoot this exact scene as a bright, upbeat photograph on a beautiful clear day. " + VAN +
        "Keep the gold lettering on its side exactly as in the reference (same words, layout, gold "
        "with dark red shadow; do not invent or change any text). Side-on, facing left, at a busy "
        "contractor stone yard: big sunlit piles of crushed stone behind it, warm sand and honey "
        "tones where the sun hits, a line of lush green summer trees, deep blue sky with a few soft "
        "white clouds. Golden-hour sun from the front-left, glossy sky reflections in the black "
        "paint. Not grey, not overcast, not gloomy. " + COMMON, True),
    "stone-yard-rear": (
        "Re-shoot this van in a new scene. " + VAN + "Seen from the rear three-quarter at a low "
        "angle, so the side lettering is not visible, parked at a contractor stone yard with tall "
        "piles of crushed stone. Late golden hour: the sun low behind the stone piles, warm rim "
        "light along the ladders and roof rack, a glowing orange-to-blue sky. " + COMMON, True),
    "south-shore-dusk": (
        "An elevated view over a small New England South Shore town at blue hour: tree-lined "
        "streets, colonial and triple-decker houses, a white church steeple, windows and "
        "streetlights glowing warm against a deep blue sky with the last orange light on the "
        "horizon. The sky and steeple fill the top of the frame; the rooftops below fall into "
        "soft darkness. " + COMMON, False),
    "service-drop": (
        "A low-angle view of a wooden utility pole with a pole-mounted transformer and a neat "
        "overhead service drop running to a house, at golden hour against a huge clear sky "
        "fading from gold to blue. Crisp silhouettes of the wires and insulators, a few green "
        "treetops at the bottom edge. " + COMMON, False),
    "high-bay": (
        "Inside a large, clean, newly finished warehouse at night: long rows of glowing LED "
        "high-bay lights receding to a vanishing point, polished concrete floor reflecting the "
        "lights, steel roof trusses. The lights fill the top of the frame; the lower half is "
        "dim floor. Cool white light with a slight warm cast. " + COMMON, False),
    "new-panel": (
        "A close-up of a freshly installed residential electrical panel with the cover off: "
        "neatly dressed and bundled conductors, a full row of new breakers with a handwritten "
        "circuit directory, clean grounding bar, warm work-light glow from above, shallow depth "
        "of field. " + COMMON, False),
    "lights-on": (
        "A classic New England centre-chimney colonial house at dusk, every window glowing "
        "warm, porch light and low path lights on, white clapboard catching the last light, "
        "a deep clear blue-hour sky with a thin band of orange on the horizon. The roofline "
        "and chimney sit high in the frame against the sky; the front lawn below falls into "
        "soft shadow. Inviting and calm. " + COMMON, False),
    "generator-snow": (
        "A grey-shingled New England Cape house at dusk after a fresh snowfall, every window "
        "glowing warm while the neighbouring houses along the street are dark, a clean "
        "standby generator on a pad beside the house with snow brushed off it. Clear "
        "lavender-and-gold sky, snow on the roof and the trees, peaceful not stormy. The "
        "roofline, lit windows and sky fill the top of the frame; the snowy yard below is "
        "in soft blue shadow. " + COMMON, False),
    "kitchen-night": (
        "A newly finished New England kitchen at night with only the electric lighting on: "
        "evenly spaced recessed ceiling lights, warm under-cabinet LED strips, three pendant "
        "lights over an island. The ceiling and pendants fill the top of the frame; the "
        "island and floor below are softly lit and dim. Clean, high-end, cosy. " + COMMON,
        False),
    "tailgate": (
        "Re-shoot this van in a new scene. " + VAN + "Seen from directly behind with both "
        "rear doors open, the interior shelving stocked with spools of copper wire, conduit "
        "and a tool bag, parked on a quiet road at golden hour. A glowing orange-to-blue "
        "sunset sky fills the top of the frame, the ladders and rack silhouetted against it; "
        "the road below in warm shadow. No lettering anywhere on the van. " + COMMON, True),
    "power-lines": (
        "A line of wooden utility poles and power lines running away toward the horizon "
        "across a coastal New England salt marsh at sunset: golden grasses, a still tidal "
        "creek reflecting the sky, a huge sky fading from deep orange to blue. The poles, "
        "wires and sky fill the top of the frame; the marsh below falls into shadow. "
        + COMMON, False),
    "main-street": (
        "A small New England town main street at blue hour: brick and clapboard storefronts "
        "with warm lit windows, old-fashioned street lamps glowing, a white church steeple "
        "against a deep blue sky. Shop signs blank, dark or too far away to read. The "
        "rooflines, lamps and steeple fill the top of the frame; the street below is dim "
        "and quiet. " + COMMON, False),
}

# Field names differ between hosted Seedream variants; try the common ones in order.
IMAGE_FIELDS = ("image_urls", "input_images", "images", "image_url")


def creds_present():
    return bool(os.environ.get("HF_KEY") or
                (os.environ.get("HF_API_KEY") and os.environ.get("HF_API_SECRET")))


def run(model, prompt, ref_url, n):
    if ref_url is None:  # text-to-image concept: no reference field to probe
        args = {"prompt": prompt, "resolution": "2K", "aspect_ratio": "21:9"}
        if n > 1:
            args["num_images"] = n
        print(f"submitting to {model} ...", flush=True)
        return hf.subscribe(model, arguments=args), None
    last = None
    for field in IMAGE_FIELDS:
        value = ref_url if field == "image_url" else [ref_url]
        args = {"prompt": prompt, field: value, "resolution": "2K", "aspect_ratio": "21:9"}
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


def make(concept, model, t2i_model, n, ref_url):
    prompt, uses_ref = CONCEPTS[concept]
    model = model if uses_ref else t2i_model
    result, field = run(model, prompt, ref_url if uses_ref else None, n)

    images = result.get("images") or []
    if not images:
        sys.exit(f"finished but returned no images: {list(result)}")
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    for i, img in enumerate(images, 1):
        url = img["url"] if isinstance(img, dict) else img
        ext = os.path.splitext(url.split("?")[0])[1] or ".png"
        dest = OUT / f"{concept}-{stamp}-{i}{ext}"
        urllib.request.urlretrieve(url, dest)
        print(f"saved {dest}")
    (OUT / f"{concept}-{stamp}-prompt.txt").write_text(
        f"model: {model}\nconcept: {concept}\nreference field: {field}\n\n{prompt}\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--concept", choices=sorted(CONCEPTS) + ["all"], default="stone-yard")
    ap.add_argument("--model", default="bytedance/seedream/v4/edit",
                    help="image-edit model for the concepts that use the reference photo")
    ap.add_argument("--t2i-model", default=None,
                    help="text-to-image model id from Higgsfield's list, for the concepts without one")
    ap.add_argument("--n", type=int, default=2)
    a = ap.parse_args()

    if not creds_present():
        sys.exit("No Higgsfield credentials in the environment. Set HF_KEY "
                 "(key-id:key-secret) or HF_API_KEY + HF_API_SECRET, then rerun.")
    concepts = sorted(CONCEPTS) if a.concept == "all" else [a.concept]
    t2i = [c for c in concepts if not CONCEPTS[c][1]]
    if t2i and not a.t2i_model:
        sys.exit(f"{', '.join(t2i)} are text-to-image: pass --t2i-model with a Higgsfield "
                 "text-to-image model id")

    OUT.mkdir(parents=True, exist_ok=True)
    ref_url = None
    if any(CONCEPTS[c][1] for c in concepts):
        if not REF.exists():
            sys.exit(f"missing reference image {REF}")
        print("uploading reference photo ...", flush=True)
        ref_url = hf.upload_file(str(REF))
    for c in concepts:
        print(f"== {c}", flush=True)
        make(c, a.model, a.t2i_model, a.n, ref_url)
