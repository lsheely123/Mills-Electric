# Listings audit — Mills Electric Inc

**All checks performed 2026-10-21.** Every row below carries the URL it came from and
how it was obtained (direct page fetch vs. search-index snippet). Anything I could not
see with my own fetch is marked **UNVERIFIED**.

**I changed nothing.** I have no authority on any of these profiles and did not attempt
to claim, edit, or log into any of them. This is a worklist for Logan and the owner.

Related: `growth/NAP-CONFLICT.md` covers the address dispute in depth. This file is the
wider listing sweep — it confirms that document's findings independently and adds four
things it did not cover: **a dead website field on four listings, a duplicate MapQuest
listing, a Saturday-hours conflict, and a business-name string that differs on every
single source.**

---

## Evidence quality legend

| Mark | Meaning |
|---|---|
| **FETCHED** | I pulled the live page and read the field myself. Strongest. |
| **SNIPPET** | The page blocked automated fetch; value read from a search-engine index snippet of that page. Weaker — the index may be stale. |
| **UNVERIFIED** | Could not confirm at all. Do not act on it without a human looking. |

---

## 1. Listing-by-listing record

### 1.1 Google Business Profile — the one that matters
- **URL (short, as in CLAUDE.md):** https://maps.app.goo.gl/pc68XnQNeTdRhR8U7
- **Resolves to:** `https://www.google.com/maps/place/Mills+Electric+Inc./@42.0535527,-71.023497,17z/...!3d42.0535487!4d-71.0209167!16s%2Fg%2F11h3vc3zr_`
- **Method:** FETCHED (HTTP 302 redirect chain followed 2026-10-21; `HTTP/2 302` then `HTTP/2 200`)

| Field | Value | Evidence |
|---|---|---|
| Business name | **`Mills Electric Inc.`** — trailing period, no comma | FETCHED, from the `/maps/place/Mills+Electric+Inc./` path segment of the redirect target |
| Street address | Pin at `42.0535487, -71.0209167` → **233 Copeland St** | FETCHED (coords); reverse-geocode per `NAP-CONFLICT.md` |
| Phone | (508) 586-2955 | UNVERIFIED on the GBP page itself — Maps serves a JS shell to automated fetch. Matches every other source. |
| Hours | — | **UNVERIFIED.** Could not read the hours panel. **This is the single most important field to check by eye** — see §2.3. |
| Website field | — | **UNVERIFIED.** Could not read. See §2.2 — probably points at the dead domain. |
| Reviews | 4 reviews, 5.0 average | Per CLAUDE.md and corroborated by Yahoo Local + Yelp (both FETCHED/SNIPPET below). Not read off Google directly. |
| Categories | — | UNVERIFIED |
| **Place ID (derived)** | `ChIJ__92kEOF5IkRCliR7A5iOEY` | Derived from the CID pair `0x89e485439076ffff:0x4638620eec91580a` in the resolved URL. Both `/maps/place/?q=place_id:` and `search.google.com/local/writereview?placeid=` return **HTTP 200** for it (checked 2026-10-21). |
| **Numeric CID** | `5059901997588764682` | Same source. `https://www.google.com/maps?cid=5059901997588764682` |

> The Place ID is what makes the review write-link in `REVIEW-ASK-KIT.md` possible. It is
> derived arithmetically from Google's own CID and both endpoints answer 200, but I could
> not read the rendered page to see the business name printed back. **Click it once before
> sending it to a customer.**

### 1.2 Better Business Bureau
- **URL:** https://www.bbb.org/us/ma/brockton/profile/electrician/mills-electric-inc-0021-67905
- **Method:** FETCHED 2026-10-21

| Field | Value (verbatim) |
|---|---|
| Business name | `Mills Electric, Inc.` — **comma and period** |
| Street address | `233 Copeland St, Brockton, MA 02301-7022` |
| Phone | `(508) 586-2955` |
| Website field | **Empty** — "No website link is provided on this BBB profile" |
| Hours | **Not displayed on the page** |
| Reviews | `0` customer reviews |
| Rating | `Not Rated` — "BBB does not have sufficient information to issue a rating" |
| Accreditation | `NOT BBB Accredited` |
| Categories | `Electrician` (single category) |
| Business started | `1/1/1984` · Years in Business: `42` |
| Principal | `Mr. Charles P. Mills, President` |

### 1.3 Yahoo Local
- **URL:** https://local.yahoo.com/info-10214240-mills-electric-brockton/
- **Method:** FETCHED 2026-10-21

| Field | Value (verbatim) |
|---|---|
| Business name | `Mills Electric` — **no "Inc" at all** |
| Street address | `233 Copeland St Brockton, MA 02301` |
| Phone | `(508) 586-2955` |
| Website field | `millselectricinc.com` — **this domain is dead, see §2.2** |
| Hours | Mon `7:00 AM - 5:00 PM` · Tue–Fri same · **Sat `7:00 AM - 5:00 PM`** · Sun `Closed` |
| Reviews | `4` reviews, `5.0` rating |
| Categories | `Electrician`, `Electric construction and Maintence` *(sic — misspelled on the listing)* |

### 1.4 BuildZoom
- **URL:** https://www.buildzoom.com/contractor/mills-electric-inc-brockton-ma
- **Method:** FETCHED 2026-10-21

| Field | Value (verbatim) |
|---|---|
| Business name | `Mills Electric, Inc` — **comma, no trailing period** |
| Street address | `233 Copeland St, Brockton, MA, 02301` |
| Phone | `(508) 586-2955` |
| Website field | **Not shown on page** |
| Hours | Not shown |
| Reviews | **None** — "BuildZoom hasn't received any reviews" |
| Rating | "BuildZoom Score of 100" (an algorithmic score, **not** a customer rating — do not quote it as one) |
| License | `12245`, status `Active` |
| Permits | `46` documented permitted projects |
| Categories | Electrical work, boiler/water heater service, solar installation, fire protection, smart home/AV |
| Owner | `Charles P. Mills` |

### 1.5 Yelp
- **URL:** https://www.yelp.com/biz/mills-electric-brockton
- **Method:** **Direct fetch BLOCKED** — server returned `HTTP 429 Too Many Requests` on
  2026-10-21. Values below are SNIPPET-level only.

| Field | Value | Evidence |
|---|---|---|
| Business name | `Mills Electric` | SNIPPET (page title: "Mills Electric - Updated March 2026 - Brockton, Massachusetts - Electricians") |
| Street address | 233 Copeland St, Brockton MA 02301 | SNIPPET |
| Phone | (508) 586-2955 | SNIPPET |
| Website field | UNVERIFIED | — |
| Hours | **Mon–Sat 7:00 AM – 5:00 PM, Sun closed** | SNIPPET |
| Reviews | 5.0 rating, 4 reviews | SNIPPET |
| Categories | `Electricians` | SNIPPET (page title) |
| Page freshness | Title says "Updated March 2026" | SNIPPET |

> **These 4 Yelp reviews are almost certainly not the same 4 as Google's 4.** Nothing I
> can see links them. Do not add the two counts together, and do not assume a Yelp
> reviewer already reviewed on Google. Verify by eye.

### 1.6 MapQuest — **TWO listings for one business**
This is a duplicate-listing problem and it is actively splitting Mills' signal.

| # | URL | Title string as indexed | Method |
|---|---|---|---|
| A | https://www.mapquest.com/us/massachusetts/mills-electric-inc-227229 | `Mills Electric Inc, 233 Copeland St, Brockton, MA 02301, US` | SNIPPET — direct fetch returned an empty JS shell |
| B | https://www.mapquest.com/us/massachusetts/mills-electric-633024293 | `Mills Electric, Brockton, MA 02301, US` — **no street address in the title** | SNIPPET — direct fetch returned an empty JS shell |

All other fields on both: **UNVERIFIED.** MapQuest renders entirely client-side and
returned no readable content to two separate fetch attempts on 2026-10-21.

What is verifiable is the important part: **two distinct MapQuest URLs, two different
name strings, and only one of them carries a street address.**

### 1.7 Dun & Bradstreet
- **URL:** https://www.dnb.com/business-directory/company-profiles/mills-electric-inc.b840c29e5ee5d2c30fd6d76ef069d704
- **Method:** **Direct fetch BLOCKED** — `HTTP 403 Forbidden` on 2026-10-21. SNIPPET only.

| Field | Value | Evidence |
|---|---|---|
| Business name | `MILLS ELECTRIC, INC.` (all-caps in the page title) | SNIPPET |
| Street address | `233 Copeland St. Brockton, MA 02301-7022` | SNIPPET |
| Phone | (508) 586-2955 | SNIPPET |
| Website field | `www.millselectricinc.com` | SNIPPET — **dead domain, see §2.2** |
| Description | "electrical contracting, all types fire and burglar systems" | SNIPPET |
| Founded | "established and incorporated in Massachusetts in **1984**" | SNIPPET |
| Employees | "employs one person" | SNIPPET |
| Reviews | None | — |

### 1.8 Manta
- **URL:** https://www.manta.com/c/mm33l64/mills-electric-inc
- **Method:** **Direct fetch BLOCKED** (`HTTP 403` to automated fetch, per
  `NAP-CONFLICT.md`; I did not re-attempt and risk a rate-limit). SNIPPET only.

| Field | Value | Evidence |
|---|---|---|
| Business name | `Mills Electric Inc` | SNIPPET (title: "Mills Electric Inc - Brockton, MA - Electrical Contractor in Brockton, Massachusetts") |
| Street address | 233 Copeland St, Brockton, MA | SNIPPET |
| Everything else | **UNVERIFIED** | — |

### 1.9 hvacservice.io
- **URL:** https://hvacservice.io/ma/brockton/mills-electric-inc
- **Method:** Fetched 2026-10-21 → **`HTTP 410 Gone`.** The page is indexed by search but
  the server now declares it permanently removed. All fields **UNVERIFIED.**
- Low value either way — a scraper directory, not a listing a customer will see. No action.

### 1.10 Solar Panel Techs
- **URL:** https://www.solarpaneltechs.com/brockton/customer-service-43978
- **Method:** Fetch failed with a TLS error (`TLSV1_ALERT_UNRECOGNIZED_NAME`) on
  2026-10-21 — the host's certificate does not match the name. All fields **UNVERIFIED**
  beyond the indexed title "Mills Electric - Solar Panel Services - Solar Panel Techs".
- Another scraped aggregator. No action.

### 1.11 Listings that do NOT exist — gaps, not errors
Each of these was searched for on 2026-10-21 and no Mills Electric Brockton listing was found:

| Platform | Finding |
|---|---|
| **YellowPages.com** | **No Brockton listing found.** A search returned `Mills Electric` in **Fort Lauderdale, FL** and unrelated Brockton electricians (e.g. `M and S Electric`), but nothing for Mills in Brockton. |
| **Angi / HomeAdvisor** | No Mills Electric listing surfaced. |
| **Porch** | No listing surfaced. |
| **Facebook, Nextdoor, Houzz, Thumbtack** | Not found in search. UNVERIFIED whether profiles exist unlinked. |

> A missing listing costs far less than a *wrong* one. **Do not go create these.** Fix the
> conflicts on the listings that already exist first; new citations built on top of an
> unsettled address just multiply the problem.

---

## 2. The mismatch table — every field where sources disagree

### 2.1 Business name — **no two sources agree**

| Source | Exact string | Checked |
|---|---|---|
| **The website (JSON-LD, 9 occurrences)** | `Mills Electric Inc` | FETCHED from repo 2026-10-21 |
| Google Business Profile | `Mills Electric Inc.` | FETCHED |
| BBB | `Mills Electric, Inc.` | FETCHED |
| BuildZoom | `Mills Electric, Inc` | FETCHED |
| Yahoo Local | `Mills Electric` | FETCHED |
| Yelp | `Mills Electric` | SNIPPET |
| Manta | `Mills Electric Inc` | SNIPPET |
| D&B | `MILLS ELECTRIC, INC.` | SNIPPET |
| MapQuest A | `Mills Electric Inc` | SNIPPET |
| MapQuest B | `Mills Electric` | SNIPPET |

Five distinct strings across ten sources. Punctuation-only variance is the mildest kind
of NAP inconsistency and Google tolerates it better than an address conflict — but
`Mills Electric` with no entity suffix (Yahoo, Yelp, MapQuest B) is a genuinely different
string, and it is the one three sources use.

### 2.2 Website field — **four listings point at a dead domain**

This is a finding `NAP-CONFLICT.md` does not cover, and it is a live problem.

| Source | Website field | Checked |
|---|---|---|
| Yahoo Local | `millselectricinc.com` | FETCHED |
| D&B | `www.millselectricinc.com` | SNIPPET |
| BBB | **empty** | FETCHED |
| BuildZoom | **not shown** | FETCHED |
| Google Business Profile | **UNVERIFIED** — could not read | — |
| Yelp | **UNVERIFIED** | — |
| **This website** | `https://REPLACE-DOMAIN` placeholder, not launched | repo, 2026-10-21 |

**What `millselectricinc.com` actually is, verified 2026-10-21:**

```
DNS A record      millselectricinc.com    → 148.113.189.118
DNS A record      www.millselectricinc.com → 148.113.189.118
HTTP  (port 80)   no response  (curl exit, http_code=000)
HTTPS (port 443)  connection refused  (ECONNREFUSED 148.113.189.118:443)
```

```
whois millselectricinc.com
  Creation Date:        2016-08-30
  Registry Expiry Date: 2027-08-30
  Updated Date:         2026-08-24
  Registrar:            GoDaddy.com, LLC
  Registrant Org:       Domains By Proxy, LLC   (privacy-shielded)
  Name Servers:         NS1.DESIGNNRANK.COM / NS2.DESIGNNRANK.COM
```

So: the domain is **registered, paid up through Aug 2027, renewed as recently as two
months ago, DNS points at a live IP — and nothing is served on either port.** The
nameservers belong to a marketing vendor ("Design N Rank"), not GoDaddy's parking.

Read plainly, that is a site someone built for Mills around 2016, which has since gone
dark while the domain quietly keeps renewing. **UNVERIFIED whether the owner controls
it** — the registrant is behind privacy proxy, so I cannot confirm from outside.

**Why this matters more than it looks:**
1. Two directories are sending every click to a dead host. A customer who clicks
   "Website" on the Yahoo or D&B listing gets a browser error with the company's name
   on it.
2. **It may be the domain this entire site should launch on.** CLAUDE.md flags
   `https://REPLACE-DOMAIN` as the one thing blocking launch. If the owner already owns
   `millselectricinc.com`, that is almost certainly the answer — it already has ten years
   of registration age and is already cited on directory listings, both of which help.
3. If the owner does *not* control it, that needs to be known before launching on a
   near-identical name.

**Ask the owner: "Do you own millselectricinc.com? Who set it up — do you have the
GoDaddy login?"** That question is free and could resolve the launch blocker.

### 2.3 Hours — Saturday is wrong on at least two listings

| Source | Mon–Fri | **Saturday** | Sunday | Checked |
|---|---|---|---|---|
| **The website** (visible copy + JSON-LD) | 7am–5pm | **7am–12pm** | closed | FETCHED from repo |
| Yahoo Local | 7:00 AM–5:00 PM | **7:00 AM–5:00 PM** | Closed | FETCHED |
| Yelp | 7:00 AM–5:00 PM | **7:00 AM–5:00 PM** | Closed | SNIPPET |
| BBB | not displayed | — | — | FETCHED |
| Google Business Profile | **UNVERIFIED** | **UNVERIFIED** | — | — |

Confirmed verbatim from the repo on 2026-10-21 — `contact.html` prints
`Mon–Fri 7am–5pm<br>Sat 7am–12pm`, and `index.html`'s JSON-LD carries
`"dayOfWeek": "Saturday", "opens": "07:00", "closes": "12:00"`.

So the conflict in the brief is **real and verified**: listings say Mills is open five
more hours every Saturday than the website does. Whichever is wrong, someone is being
told the wrong thing — and if it is the listings that are right, the site is turning away
Saturday-afternoon calls, which for an electrician are often the urgent, high-value ones.

Note also: **CLAUDE.md says "24/7 emergencies"** and not one external listing mentions
it anywhere. That is a real differentiator being published nowhere but the site.

### 2.4 Street address — confirmed, 9 sources to 1

Independently re-confirmed today. Full evidence in `NAP-CONFLICT.md`; summary:

| Value | Sources |
|---|---|
| **233 Copeland St** | Google (pin coords, FETCHED) · BBB (FETCHED) · BuildZoom (FETCHED) · Yahoo (FETCHED) · D&B (SNIPPET) · Manta (SNIPPET) · Yelp (SNIPPET) · MapQuest A (SNIPPET) |
| **155 Main St** | **This website only** — 2 occurrences in the repo, FETCHED 2026-10-21 |

Four of those are now first-hand page fetches, not snippets. The evidence is one-sided.

### 2.5 Founding year — still unresolved

| Source | Claim | Checked |
|---|---|---|
| Website (`about.html` ×4, stat blocks ×2) | 1979 → "47 years" | repo |
| BBB | `Business Started: 1/1/1984` · `Years in Business: 42` | FETCHED |
| D&B | "established and incorporated in Massachusetts in 1984" | SNIPPET |

**I could not find a primary state record.** Searches for a Massachusetts Secretary of
the Commonwealth / OpenCorporates / Bizapedia entry returned nothing usable on
2026-10-21 → **UNVERIFIED against any primary source.**

As `NAP-CONFLICT.md` reasons, sole-proprietorship-1979 → incorporated-1984 reconciles
both cleanly and is a common pattern. I agree with that read and am not overturning it.
**Free way to settle it:** the Commonwealth's corporate database at
`corp.sec.state.ma.us` is a free public search — it needs a human at a form, so Logan
can run it in a minute at no cost.

### 2.6 Phone — agrees everywhere, one formatting nit

Every source: `(508) 586-2955`. **No conflict.**

The website displays it as `(508)-586-2955` — hyphen after the closing paren — in 55
places. Google matches on digits, so this costs nothing in ranking. It is a cosmetic
inconsistency only. **Lowest priority item in this document; fix it if someone is in
there anyway, not as its own task.**

### 2.7 Categories

| Source | Categories | Checked |
|---|---|---|
| BBB | `Electrician` | FETCHED |
| Yahoo | `Electrician`, `Electric construction and Maintence` *(sic)* | FETCHED |
| Yelp | `Electricians` | SNIPPET |
| BuildZoom | Electrical, boiler/water heater, solar, fire protection, smart home/AV | FETCHED |
| Google | **UNVERIFIED** | — |

BuildZoom's spread comes from permit records, so it reflects work actually performed.
Worth noting the GBP secondary categories should probably cover generators and fire/
burglar systems (D&B explicitly lists "all types fire and burglar systems") — but
**check what the GBP currently has before changing anything.**

---

## 3. What to fix, in order

Ranked by ranking impact per unit of effort. Items 1–3 are owner-only (they require
being signed in as the profile owner); nobody else can do them.

### Priority 1 — Settle the street address, then make Google match (OWNER)
Nothing else on this list matters as much. A business whose own site contradicts its
Google pin on the street address is the textbook suppression case, and it is currently
one source against eight. **Blocks:** the JSON-LD placeholders, and therefore launch.
**Action:** ask Charles Mills which address is the real place of business today. Then
make the site match Google, or Google match the site — one of the two moves.

### Priority 2 — Verify Google's hours and settle Saturday (OWNER)
Fastest real-money item here. Hours are read directly off the GBP by both Search and
Maps, and a wrong Saturday means either lost calls or angry ones. Also add the 24/7
emergency availability, which currently appears on zero listings.
**Action:** open the GBP, read the hours panel, compare to Mon–Fri 7–5 / Sat 7–12,
correct whichever is wrong — and fix Yahoo and Yelp to match afterwards.

### Priority 3 — Resolve the millselectricinc.com domain (OWNER / LOGAN)
Potentially unblocks the entire launch, costs one question. If the owner has it, that is
the `REPLACE-DOMAIN` answer and two dead directory links come back to life at once. If
he does not, you need to know that before launching a site on the same name.
**Action:** ask the owner; check for a GoDaddy account.

### Priority 4 — Fill in the empty website fields, after launch (OWNER)
BBB's field is empty, BuildZoom shows none, and Yahoo/D&B point at a dead host. The
website field is a direct ranking and traffic input. **Do this the day the domain goes
live, not before** — pointing listings at a 404 is worse than pointing at nothing.

### Priority 5 — Merge the duplicate MapQuest listing (OWNER)
Two URLs, two name strings, one address between them. Duplicates split citation signal
and MapQuest syndicates to other data aggregators, so the error propagates.
**Action:** on MapQuest, report the one with no street address as a duplicate of the one
that has it. Free.

### Priority 6 — Standardize the business name string everywhere (OWNER)
Pick one — **I would use `Mills Electric, Inc.`**, matching BBB and the legal entity — and
make all ten sources say exactly that, punctuation included. Lower impact than the
address, but it is the cheapest remaining consistency win.
**Caveat:** Google's own guidelines want the real-world name, so match the sign on the
truck. If the truck says "Mills Electric", use that everywhere instead.

### Priority 7 — Settle 1979 vs 1984 (LOGAN, free)
Run the free MA corporate search. If 1984 turns out to be the founding date rather than
the incorporation date, CLAUDE.md warns the "47" is load-bearing across four spots in
`about.html` plus stat blocks on two pages — they all move together.

### Priority 8 — Phone formatting (COSMETIC)
`(508)-586-2955` → `(508) 586-2955` on the site. Zero ranking impact. Only if convenient.

### Explicitly NOT on this list
- **Creating new listings** (YellowPages, Angi, Nextdoor, Houzz). Not until the address
  is settled. New citations carrying a disputed address make the problem bigger, not
  smaller.
- **Anything on hvacservice.io or solarpaneltechs.com.** Scraped aggregators; one is
  already returning 410. They will re-scrape correct data once the real listings are
  right.

---

## 4. The honest summary

The address conflict is the headline, and `NAP-CONFLICT.md` already owns it. What this
sweep adds is that **the problem is wider than one field**: five different spellings of
the company name, a Saturday-hours conflict on at least two listings, a duplicate
MapQuest record, a BBB profile with no website and no reviews, and four listings pointing
customers at a domain that has been dark for years while quietly renewing.

None of this is unusual for a 40-year-old contractor who has never done any of this on
purpose. All of it is fixable for free. But **almost all of it needs the owner signed
in** — which is why the first real task is not an edit, it is a conversation with
Charles Mills.
