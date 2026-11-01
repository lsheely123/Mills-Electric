# NAP conflict — Mills Electric Inc

**Status: UNRESOLVED. Blocks launch of the LocalBusiness schema.**
**Owner: Logan. Action: confirm with Charles Mills before the domain goes live.**

Last checked: 2026-10-21

NAP = Name, Address, Phone. Google cross-references these across the web to decide
whether a listing is trustworthy. A business whose own website disagrees with its own
Google Business Profile about its street address gets its local ranking suppressed —
which is exactly the problem this SEO pass is meant to fix. So this has to be settled
by a human, not guessed at by me.

---

## Note — 2026-10-31: the business card is NOT evidence

Charlie's old business card (shared in chat, not saved to the repo) reads
233 Copeland Street. Logan reports the card is likely years out of date and was supplied
for its look only. An old card agreeing with old directory listings proves nothing about
today: it is equally consistent with the business having moved *from* Copeland *to*
155 Main St. The conflict stays open. Ask Charlie directly.

The van lettering reads "Masters LIC. #11245A" vs 12245 everywhere else. Worth asking
about, but the card does not settle it either.

## What agrees

These match everywhere and are safe to ship:

| Field | Value | Agreed by |
|---|---|---|
| Name | Mills Electric, Inc. | all sources |
| Phone | (508) 586-2955 | all sources |
| MA Electrician licence | 12245 | CLAUDE.md (`#A-12245`), BuildZoom (`12245`) |
| City / State / ZIP | Brockton, MA 02301 | all sources |

## What does not agree

**The street address.** One value in our own repo, a different value in all five
external sources — *including the Google Business Profile that CLAUDE.md itself links to.*

| Source | Street address it publishes |
|---|---|
| **CLAUDE.md + `contact.html` + `index.html` footer** | **155 Main St**, Brockton, MA 02301 |
| BBB | 233 Copeland St, Brockton, MA 02301-7022 |
| Dun & Bradstreet | 233 Copeland St, Brockton, MA 02301 |
| BuildZoom | 233 Copeland St, Brockton, MA 02301 |
| Manta | 233 Copeland St, Brockton, MA (403'd on fetch; address per search index) |
| Yahoo Local | 233 Copeland St, Brockton, MA (per search index) |
| **Google Business Profile** (the `maps.app.goo.gl` link in CLAUDE.md) | **pin resolves to 233 Copeland St** — see below |

### The Google Maps link in CLAUDE.md points at Copeland St, not Main St

This is the important part. CLAUDE.md lists this as the official Google Maps URL:

    https://maps.app.goo.gl/pc68XnQNeTdRhR8U7

That short link 302-redirects to a full Maps URL carrying the place's own coordinates:

    https://www.google.com/maps/place/Mills+Electric+Inc./@42.0535527,-71.023497,17z/...
    !8m2!3d42.0535487!4d-71.0209167!16s%2Fg%2F11h3vc3zr_

Reverse-geocoding the pin (`42.0535487, -71.0209167`) via OpenStreetMap Nominatim returns:

    233, Copeland Street, Skyview Village, Campello, Brockton, Plymouth County,
    Massachusetts, United States

155 Main St is in downtown Brockton (roughly 42.083, -71.018). The GBP pin is ~2 miles
south of there, in Campello. **The two addresses are not the same place and not a
typo for each other.**

So the score is: our repo says Main St; BBB, D&B, BuildZoom, Manta, Yahoo and Google all
say Copeland St. I am not making the call — but Logan should know the evidence is
lopsided, and that the one source that matters most for ranking (Google) is on the
Copeland St side.

### Source URLs

- BBB — https://www.bbb.org/us/ma/brockton/profile/electrician/mills-electric-inc-0021-67905
  > "233 Copeland St. Brockton, MA 02301-7022" · "(508) 586-2955" · "Business Started: 1/1/1984"
  > · "Mr. Charles P. Mills, President" · "Years in Business: 42" · NOT BBB Accredited, Not Rated
- Dun & Bradstreet — https://www.dnb.com/business-directory/company-profiles/mills-electric-inc.b840c29e5ee5d2c30fd6d76ef069d704
  > "233 Copeland St. Brockton, MA 02301-7022" · "electrical contracting, all types fire and
  > burglar systems" · "established and incorporated in Massachusetts in 1984" · "employs one person"
- BuildZoom — https://www.buildzoom.com/contractor/mills-electric-inc-brockton-ma
  > "233 Copeland St, Brockton, MA 02301" · "(508) 586-2955" · MA Electrician licence "12245",
  > verified active as of September 2026 · "approximately 46 permitted projects"
- Manta — https://www.manta.com/c/mm33l64/mills-electric-inc
  (returns HTTP 403 to automated fetch; Copeland St address read from the search index snippet,
  **so treat this one as weaker evidence than the four above**)
- Yahoo Local — https://local.yahoo.com/info-10214240-mills-electric-brockton/
  (Copeland St per search index; not fetched directly)
- Google Business Profile — https://maps.app.goo.gl/pc68XnQNeTdRhR8U7
  (pin at 42.0535487, -71.0209167 → 233 Copeland St, per reverse geocode above)

### Minor caveat on the ZIP

OSM's reverse geocode returned postcode `02379` for the pin. `02379` is West Bridgewater,
so that is almost certainly OSM data imprecision at the Brockton/W. Bridgewater line.
BBB's `02301-7022` is the more credible ZIP+4 and matches CLAUDE.md's `02301`.
**Use 02301.** Confirm the +4 with the owner if you want the full ZIP+4 in the schema.

---

## Second, separate conflict: the founding year

Not what I was asked to look into, but it surfaced while verifying the address and it is
load-bearing, so flagging it.

| Source | Claim |
|---|---|
| CLAUDE.md, `about.html` body copy, `about.html` `<h2>`, `about.html` meta description | Started **1979** → "47 years", "Forty-seven years on the South Shore" |
| BBB | "Business Started: **1/1/1984**" · "Years in Business: 42" |
| Dun & Bradstreet | "established and incorporated in Massachusetts in **1984**" |

**This may not actually be a contradiction.** A business that operated as a sole
proprietorship from 1979 and incorporated as "Mills Electric, Inc." in 1984 would produce
exactly this split, and CLAUDE.md's separate "56 years in the industry" figure implies
Charles Mills was working the trade well before either date. 1979 is a defensible
*founding* date even if 1984 is the *incorporation* date.

But note what CLAUDE.md says about the 47: *"47 years is load-bearing. It sets the 1979
founding date, which also appears in about.html's body copy, its `<h2>` and its meta
description."* So if the owner says the right number is 1984, **four** places in
about.html plus the stat blocks on two pages have to move together.

**I shipped `foundingDate: 1979`** in the schema, because that is what the site already
publishes and the brief said to source values from CLAUDE.md. Flagging it rather than
changing it. Confirm with the owner.

---

## What I did in the code because of this

`index.html` carries the `Electrician` JSON-LD block. Its `address` and `geo` are
**deliberately non-functional placeholders**, each wrapped in an HTML comment explaining why:

```
ADDRESS_UNCONFIRMED
GEO_UNCONFIRMED
```

Everything else in that block — name, phone, email, hours, priceRange, areaServed,
foundingDate, sameAs, aggregateRating — is real and shipped.

**Publishing the schema with these placeholders still in it is worse than having no
address in the schema at all.** Resolve this first.

### Resolution steps

1. Ask Charles Mills: which address is the business's actual place of business today?
2. Then, in `index.html`, replace the two placeholder blocks with the confirmed values.
   For the geo, use the coordinates of the **confirmed** address — do not reuse the
   `42.0535487, -71.0209167` pin above unless Copeland St is the answer.
3. If the answer is Copeland St, also fix the human-visible copy, which currently says
   155 Main St in two places:
   - `contact.html` — the "Direct" card, the address `<li>`
   - `index.html` — the footer "Contact" column
   (`services.html`, `about.html`, `reviews.html` and `404.html` footers do **not** print a
   street address, so they need no change.)
4. If the answer is Main St, the Google Business Profile is wrong and is actively costing
   the business rankings — fix the GBP address, then chase BBB, D&B, BuildZoom, Manta and
   Yahoo to match.
5. Either way: once settled, make every listing identical, down to the abbreviation
   (`St` vs `Street`). Consistency is the whole point.
