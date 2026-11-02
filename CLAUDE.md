# Mills Electric Inc — Website

## Business Details
- **Company**: Mills Electric Inc
- **Phone**: (508)-586-2955
- **Email**: Millselectricinc@gmail.com
- **Address**: 155 Main St, Brockton, MA 02301 — **DISPUTED, do not treat as settled.**
  BBB, D&B, BuildZoom, Manta, Yahoo *and the Google Business Profile pin linked below*
  all publish **233 Copeland St**. The JSON-LD ships an `ADDRESS_UNCONFIRMED` placeholder
  rather than guess. Full evidence and resolution steps: `growth/NAP-CONFLICT.md`.
  Confirm with the owner before launch.
- **Hours**: Mon–Fri 7am–5pm, Sat 7am–12pm, 24/7 emergencies
- **Founded**: 1979

## Company Stats (the "by the numbers" block)
These four appear **twice** — `index.html` ("Why Mills") and `about.html` ("By the
numbers"). They must stay identical; changing one and not the other puts two
contradictory claims on the same site.
| Figure | Label |
|---|---|
| 47 | Years of Mills Electric |
| 56 | Years in the industry |
| 3hr | Median response on emergency calls |
| *Warranty* (word, not a figure) | on select jobs |

- The warranty cell uses `.stat-n.stat-word` — a word rather than a number, so it steps
  down in size and pins its line-height to `.stat-n`'s box to keep captions aligned.
- **47 years is load-bearing.** It sets the 1979 founding date, which also appears in
  about.html's body copy, its `<h2>` ("Forty-seven years on the South Shore") and its
  meta description. Bump the 47 and all four have to move together.
- Retired in Sep 2026: "18 / Years in business", "2,400+ / Permits pulled and closed
  out", "4hr / Median emergency response", "3yr / Workmanship warranty".

## Online Presence
- **GitHub**: https://github.com/lsheely123/Mills-Electric
- **Google Maps**: https://maps.app.goo.gl/pc68XnQNeTdRhR8U7
- **License**: MA Master Electrician #A-12245

## Current Google Ratings
- **Average**: 5.0 stars
- **Total reviews**: 4
- **5-star percentage**: 100%

## Key Assets
- **Hero image**: assets/mills-van.jpg (the lettered black van, from Charlie, Oct 2026). Also the og/twitter/JSON-LD share image on all 14 pages. `crew-panel.jpg` is kept but unused.
- **Service area map**: assets/mills-electric-map.jpg (1200×807, Brockton location). Shown on
  index.html beside the service-area table and on contact.html. The 1.1 MB PNG was retired Nov 2026.
- **Brand logos (v3.1, current)**: brand_assets/logos/ — 10 PNGs:
  `me-primary`, `me-horizontal`, `me-mark`, `me-badge-circle`, `me-badge-hex`,
  each with a `-reversed` counterpart.
  - Source board (as delivered): brand_assets/logos/_source/board-3.1.png
    Earlier: board-3.0.png, transparent-3.0.png (also in assets/logos/)
  - Superseded: brand_assets/logos/_v3.0/ (gradient red), _v2/ (navy+yellow), _v1/
  - **Derived, not delivered**: everything `-reversed`, plus `me-mark`/`me-mark-reversed`
    and **both `me-badge-hex` files**. The 3.1 board supplied only 3 light-background
    lockups (primary, badge-circle, horizontal). Reversed = black shapes remapped to
    white; mark = a crop of the primary; badge-hex = carried over from 3.0 with its red
    flattened to #E90206, since 3.1 dropped it. Confirm the hex with the designer.
  - **Missing — must be requested**: the one-color set (`me-mono-black`, `-white`,
    `-gold`, `-red`) and **vector masters**. See below.

### Logo source quality — read before any print job
The 3.0 files were delivered as two flattened **RGB boards with no alpha channel**; the
"transparency" was a drawn checkerboard. Everything in brand_assets/logos/ was cut from
those boards and keyed back to real transparency, so the PNGs are clean — but they are
**not masters**. The board put the primary at just 790×457 with JPEG-soft, wavy edges.

**The shipped PNGs are rebuilt at 3×** (primary 2370×1371, horizontal 3696×732, mark
2135×895, badge-circle 1878×1752, badge-hex 1779×1257). Each colour region's contour was
re-derived at high resolution and re-rendered, which removes the compression mush and
gives clean, smooth edges. Verified non-destructive: silhouette IoU ≥ 0.993, coverage
delta ≤ 0.2%, identical bounding boxes and aspect ratios, all layer medians unchanged.

This is reconstruction, not recovery — it does NOT add detail the board never had, and the
gold's brushed texture is still 790px of information stretched over 2370. Good enough for
web and ordinary print; **still get vector (SVG/AI/EPS) from the designer** for a wrap, a
yard sign, or embroidery digitizing. To regenerate: brand_assets/logos/_source/board-3.1.png.
**Ask the designer for SVG/AI/EPS.**

- **Site logos**: assets/logos/ — **v3.1**:
  - `reversed-logo-on-black.png` — 660×382, transparent RGBA (4× the 165px display size),
    exported from `brand_assets/logos/me-primary-reversed.png`. Masthead + footer, all 6 pages.
  - `favicon-32/180/192/512.png` — the v3.1 mark centred on #0B0B0C, from
    `brand_assets/logos/me-mark-reversed.png`. 32/180/192 are linked from every page
    `<head>`; 512 still has no manifest pointing at it.
  - The old `reversed-logo-on-navy.png` is deleted (recoverable from git history).
  - **Don't put designer source boards in assets/** — `make-deploy.sh` copies all of
    `assets/`, so anything dropped there gets published. Source art lives in
    `brand_assets/logos/_source/`.

## Current Reviews (Real Customer Testimonials)
1. **Jose Oliveira** (2024, 5★)
   - "I've had the pleasure of relying on Mills Electric for over 8 years for commercial and residential jobs. They arrive promptly at the scheduled time, and are well-prepared with the necessary tools and equipment."

2. **Candis West** (2022, 5★)
   - "Mills electric is a reliable company to service your electrical needs."

3. **María "Loja"** (2025, 5★)
   - (Rating only, no text visible)

4. **James Kelleher** (2020, 5★)
   - (Rating only, no text visible)

## Pages
- **index.html** — Home page. Section order (Nov 2026 layout): full-bleed van hero with the
  12° red cut → trust bar → services (2 featured dark cards + 4) → dark stats band → quote-led
  reviews block (Jose Oliveira) → process timeline → service area (table + map) → FAQ → CTA band
- **services.html** — Detailed service offerings
- **about.html** — Company background and credentials
- **reviews.html** — Full review list and Google rating
- **contact.html** — Contact form, hours, map, estimate request
- **404.html** — Error page

### Town service-area pages (added Oct 2026) — 8 more, 14 total
`electrician-<town>-ma.html` for Abington, Whitman, Easton, Stoughton, Randolph,
Holbrook, Avon, Bridgewater. Targets "Electrician <Town> MA".

- **Generated, not hand-edited**: `tools/make-town-pages.py` owns the masthead, band
  CTA and footer so they cannot drift from the six core pages. Per-town prose lives in
  the `TOWNS` dict in that file. **Edit the generator and re-run it**, not the HTML.
- Each one is deliberately *not* a doorway clone — the housing-stock and
  electrical-reality copy is specific to that town (knob-and-tube in Abington's pre-war
  stock, aluminum branch wiring in Stoughton's 1965–73 tracts, generators in Easton,
  multi-family conversions in Randolph, and so on).
- The only numbers on them are the published 3hr median, that town's own row from
  index.html's service-area table, and the licence number. **No invented job counts,
  testimonials or response times** — keep it that way.
- They are linked from index.html's service-area table and about.html's chip row.
  Those links are what keeps them out of orphan status; don't remove them.

## Design System
Source of truth: `brand_assets/mills-electric-brand-book.html` (**v3.1**). Tokens mirrored in
`brand_assets/tokens.css`. If anything disagrees, the brand book wins.

> **The whole project is on v3.1.** v3.0 replaced Navy with Graphite Black and Volt Yellow
> with Brushed Gold; v3.1 flattened Signal Red. The brand book, `tokens.css`, the logo
> artwork, `assets/site.css`, all 6 pages and `deploy/` are all migrated. Layout, copy and
> structure were deliberately left untouched — the migration changed colour and logo only.

### v3.1 palette (brand book + tokens.css)
- **Primary color**: Graphite Black (#0B0B0C)
- **Accent color**: Brushed Gold (#DFAD37) — sampled from the delivered 3.0 logo artwork
  (median of the brushed E-bars). Supersedes the #C8A951 mockup value.
- **Trim color**: Signal Red (#E90206) — **flat since v3.1**. Through 3.0 the bolt carried
  a gradient (~#8B0000 to #FE493A); 3.1 uses one measured value. Never re-apply a gradient.
- **Red ramp**: 800 `#7E0103` · 700 `#B60205` · 600 `#C50205` · 500 `#E90206` ·
  300 `#FE6C6F` · 100 `#FDBABB` · 50 `#FEE9EA`
- **Color mix**: roughly 65% black/neutrals, 25% white, 8% gold, 2% red
- **Font**: Inter (body), Archivo Black (headings)
- **Gold ramp**: 700 `#6E5212` · 600 `#B98A1E` · 500 `#DFAD37` · 300 `#EAC97B` ·
  100 `#EEDEB9` · 50 `#F8F3E8`
- **Token renames**: `--me-navy-*` → `--me-black-*`, `--me-yellow-*` → `--me-gold-*`.
  Not aliased on purpose, so a stale `--me-navy-800` fails loudly.
- **CSS**: assets/site.css (v3.1) — **JS**: assets/site.js (masthead scroll state only)

### Superseded palettes (historical)
- v2.0: Navy #07224B, Volt Yellow #FECA04, Signal Red #E4151B (gradient bolt)
- v1: see git history

### Site CSS variable names
`assets/site.css` mirrors the brand book's rename rule — there is no `--navy` or `--volt`
anywhere in the site any more:
- `--navy*` → `--black*` (`--black`, `-900`, `-700`, `-600`, `-400`, `-200`, `-50`)
- `--volt*` → `--gold*` (`--gold`, `-700`, `-600`, `-300`, `-100`, `-50`)
- classes: `.btn-onnavy` → `.btn-ondark`, `.on-navy-muted` → `.on-dark-muted`,
  `.past-navy` → `.past-dark` (the last one is also in `assets/site.js` — keep them in sync)
- **No inline styles on any page** since the Nov 2026 layout pass. Headings default to black
  via CSS and go white inside `.dark .hero .pagehead .band .card-dark`; eyebrows carry the
  gold rule and colour by default. Keep it that way — new styling goes in site.css as a class.
- Two focus rings now: `--focus` (gold-600, for light surfaces) and `--focus-dark`
  (gold-300, used by `.logo-link`, `.navlink`, `.btn-ondark`, `.foot a`). Core gold is
  only 2.06:1 on white and fails as a lone non-text indicator.

### Layout classes added Nov 2026 (all in assets/site.css)
`.hero-bg/.hero-copy` (full-bleed photo hero), `.pagehead-bg/.pagehead-copy` (inner pages,
crew-panel.jpg behind a 78% black overlay — a photo slot), `.trust*` (licence / 24-7 / free
estimates / 5.0 bar), `.svc-grid .card-featured .card-dark`, `.stats-band .stats-grid .stat`,
`.timeline`, `.area-grid .map-card .tbl-wrap`, `.quote* .snapshot-stack`, `.band-tel` (giant
phone number), `.callbar` (sticky Call / Estimate bar ≤600px; the masthead phone button hides
there), `.foot-grid` etc., `.check-list .rule-list .link-gold .link-ink .chips-dark`.
Masthead phone button is `btn-primary` (gold) — allowed, the masthead is its own section.
Type scale stepped up on the 1.25 ratio: display 4.768rem, h2 3.05rem, pagehead h1 3.815rem.

### Logo sizing gotcha
Every logo `<img>` carries hardcoded `width`/`height` — **currently 165&times;95** (28 tags,
2 per page across all 14). Changing the artwork without updating those attributes squashes the logo; this
has bitten once already. 165px also clears the brand book's 160px digital minimum, so don't
shrink it below that.

Ratio history: v1 1.56:1 · v2.0 1.96:1 (165&times;84) · v3.0 2.10:1 · **v3.1 1.73:1
(165&times;95)**.

Per-lockup v3.1 ratios: primary **1.73:1**, horizontal **5.05:1**, mark **2.39:1**,
badge-circle **1.07:1** (nearly square), badge-hex **1.42:1**.

### Signal Red rules
- Red is **trim, not a theme**: hairlines, a sheared edge, the emergency badge, the lockup itself.
- At most **one** red button per site — the 24/7 emergency CTA — with a **white** label.
- Never `#E90206` as type on black (4.19:1); use `#FE6C6F` on black surfaces.
- **Never red against gold at all** — **2.27:1**, a hard fail. It was 3.09:1 against Volt
  Yellow, so this rule got *stricter* when gold arrived. Put black or white between them.
- Status `danger` is `#B60205` (red-700), deliberately deeper than brand red.
- The lockup red is **one flat value**. Gradients, bevels and glows on it are out.
- The masthead's 3px red rule is **transparent over the black band** and fades in only once
  the hero/pagehead clears the header (`.masthead.past-dark`, toggled by assets/site.js).
  Deliberate — red on black is only 4.19:1, and it keeps red inside its 2% budget.
- On the live site red appears in exactly three places: the masthead edge, the hero's
  12° sheared bottom edge (the cut is `clip-path` on `.hero`, the 4px line is `.hero::after`),
  and the contact form's error state. There is no red button. The hero has **no gold border**
  so the red line never meets gold; it meets the white trust bar.

### Gold rules (v3.1)
- Gold is **flat on screen** — no gradient, sheen or bevel. The brushed gradient
  (`--me-gold-brushed`) is for print, vinyl and signage only.
- Gold buttons take **black** labels (**9.53:1**). Never white on gold, never gold on white
  (both **2.06:1**); gold-toned text on white uses `gold-700` `#6E5212` (7.30:1).
- Focus rings are `gold-600` `#B98A1E` on light (3.13:1) and `gold-300` `#EAC97B` on dark
  (12.31:1) — core gold is only **2.06:1** on white and fails the 3:1 bar a focus indicator
  must clear alone. In site.css these are `--focus` and `--focus-dark`.
- **Gold never carries a safety message.** Volt Yellow was a warning color; Brushed Gold is
  not. Hazard/emergency signalling uses Signal Red or high-vis equipment outside the palette.

## SEO (added Oct 2026)
Before this pass the site had no JSON-LD, no sitemap, no robots.txt, no canonicals and
no Open Graph on any page. All six were added, plus the eight town pages.

### 🚨 `https://REPLACE-DOMAIN` — the one thing blocking launch
Every absolute URL on the site is the literal placeholder `https://REPLACE-DOMAIN`.
**One case-sensitive find-replace across the repo sets all of them**, then rebuild:

```sh
grep -rl 'REPLACE-DOMAIN' --include='*.html' --include='*.xml' --include='*.txt' . \
  | xargs sed -i '' 's|https://REPLACE-DOMAIN|https://therealdomain.com|g'
./make-deploy.sh
```

It appears in: all 14 pages (canonical, `og:url`, `og:image`, `twitter:image`, every
JSON-LD `@id`/`url`), `sitemap.xml` (13 `<loc>`), `robots.txt` (the `Sitemap:` line),
and both generator scripts in `tools/`. **robots.txt and sitemap.xml are inert until
this is done** — a relative `Sitemap:` directive is ignored by every crawler.

### The other two placeholders — `ADDRESS_UNCONFIRMED` / `GEO_UNCONFIRMED`
In index.html's `Electrician` block only. These are *not* find-replaceable; they need a
human answer first. See `growth/NAP-CONFLICT.md`. **Do not publish the schema with these
still in it** — a LocalBusiness with a junk address is worse than one with no address.

### What is where
- `index.html` — `Electrician` (the one business entity, `@id` `/#electrician`) + `FAQPage`
- `services.html` — `BreadcrumbList` + 6 × `Service`, each `provider`-linked to the above
- town pages — `Electrician` scoped to that town + `BreadcrumbList`
- about / reviews / contact / 404 — `BreadcrumbList`

Deliberate omissions, don't "fix" these without reading why:
- **FAQPage is on index.html only.** The same six Q&As are printed on services.html and
  contact.html too; duplicating the markup across three URLs is a known Google problem.
- **No `Review` markup on reviews.html.** Google disallows self-serving review markup on
  LocalBusiness. The rating lives once, as `aggregateRating` on the Electrician node.
- **404.html is noindex and excluded from sitemap.xml** (13 URLs, not 14). It is *not*
  disallowed in robots.txt — blocking it would stop crawlers reading the noindex tag.

### URL form
Canonicals and sitemap use `.html`, matching the real filenames and every internal link,
so they resolve on any host. Cloudflare Pages *also* serves the extensionless form and
308-redirects `/foo.html` → `/foo`. If you want extensionless to be canonical, change it
in `sitemap.xml` **and** every page's canonical/`og:url` together — never one alone.

## Deployment
- Run `./make-deploy.sh` to build the `deploy/` folder
- Deploy folder ready for Cloudflare Pages
- Excludes: brand_assets/, tools/, _archive/, growth/, screenshots/
- Ships **14 HTML pages + sitemap.xml + robots.txt + assets/**. The script warns if the
  page count is not 14, refuses to build if designer source art is found under `assets/`,
  and strips `.DS_Store` (which `cp -R` was previously publishing).

## For Revisions & Updates
When making changes:
1. Update contact info here first
2. Keep phone, email, and hours consistent across all 14 HTML pages
   (town pages: edit `tools/make-town-pages.py` and re-run, don't edit the HTML)
3. Update Google ratings in index.html and reviews.html snapshots
4. Rebuild deploy/ folder before pushing: `./make-deploy.sh`
5. Commit and push with clear message: `git commit -m "Update [what changed]"`

## Notes
- GitHub PAT is stored in the macOS keychain (`credential.helper = osxkeychain`), not in the
  repo — the remote URL is clean. Rotate it when convenient.
- Contact.html had a revert issue; always verify it after IDE edits
- Review text for Jose Oliveira is truncated at source (Google screenshot)
- María and James reviews are rating-only from the Google source
