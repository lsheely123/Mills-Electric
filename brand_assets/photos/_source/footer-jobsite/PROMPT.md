# Footer photo concepts (Higgsfield)

**Mood (Logan, 2026-11-03):** bright and sunny, "nice, not depressing and grey like the one he gave".
Hyper-realistic. Replaces `assets/footer-jobsite.jpg` (Charlie's overcast van-at-gravel shot, upscaled).

## Composition rules for this slot (all concepts)
The footer is a full-bleed photo under a smoked-glass panel:
- Only the **top band** shows clear: ~200px on desktop, ~140px on phones. Put the subject's
  most recognisable part (roofline, ladders, lights, skyline) in the **upper third**.
- Phones crop the photo to a **narrow centre strip**, so keep the subject **horizontally centred**.
- The lower half sits behind glass with small grey text on it: keep it **calm and mid-to-dark**.
  No big bright highlights down there (footer text contrast is ≥ 5.14:1 today; re-check after).
- Wide 21:9, 2K or larger. No people's faces, no watermarks, **no invented text or signs**.
- Don't repeat the hero: the hero is already the van in a house driveway.

## Concepts
Run one with `python3 make_footer_photo.py --concept <name>`.

| name | idea | why it fits | needs reference? |
|---|---|---|---|
| `stone-yard` | Charlie's van at a sunlit stone yard, golden hour, blue sky | Closest to his photo, just happy | yes (keeps his van + lettering) |
| `stone-yard-rear` | Same yard, van from the rear three-quarter, ladders and rack in silhouette against sunset | Shows the van with **no lettering for AI to garble** | yes |
| `south-shore-dusk` | Elevated view over a South Shore town at blue hour, streets and windows lighting up | "We keep the lights on here"; dark lower half suits the glass | no |
| `service-drop` | Low angle on a utility pole and service drop at golden hour, big clean sky | Iconic electrical image; sky fills the clear band | no |
| `high-bay` | A finished warehouse with rows of glowing LED high-bays receding into the distance | Commercial work; dark, rhythmic, glows through the glass | no |
| `new-panel` | Macro of a freshly finished panel: dressed conductors, labelled breakers, warm light | Craftsmanship; but close to the stats band's panel photo | no |
| `lights-on` | A New England colonial at dusk, every window glowing, porch and path lights on | "We keep your lights on", no words needed | no |
| `generator-snow` | A Cape after a snowfall, lit up while the street is dark, standby generator beside it | The 24/7 / storm story, without being grey | no |
| `kitchen-night` | A finished kitchen at night, only the recessed, under-cabinet and pendant lights on | Finished work that glows through the glass | no |
| `tailgate` | The van from directly behind, rear doors open, wire spools and tools, sunset sky | The van with no lettering to garble | yes |
| `power-lines` | Poles and lines running off across a South Shore salt marsh at sunset | Simpler, more local `service-drop` | no |
| `main-street` | A small-town main street at blue hour, lit storefronts, street lamps, steeple | Commercial work; risk: AI invents shop signs | no |

Recommendation (Nov 3): `lights-on` first, `generator-snow` if the footer should lean into
emergencies, `stone-yard-rear` / `tailgate` if it must be the van. A real photo from Charlie
beats all of them if he can get one: landscape, golden hour, subject in the top third.

Run every concept at once: `python3 make_footer_photo.py --concept all --t2i-model <id>`.
The prompts themselves live in `CONCEPTS` in make_footer_photo.py.

## Non-AI options (already rendered)
`python3 make_footer_art.py` draws these locally, no credentials needed:
- `line-drawing.png`: a gold line drawing of a house's electrical service (pole, drop, meter,
  panel, circuits, generator) on graphite, scaled to sit entirely in the clear band.
- `engine-turned.png`: the logos' engine-turned gold texture, pushed very dark.

It also writes `preview-<name>.png` (plus `preview-current.png`): a rough mock of the 1440px
footer with the clear band and glass panel, for comparing options. Not a real render, so
re-check the live footer after a swap.
