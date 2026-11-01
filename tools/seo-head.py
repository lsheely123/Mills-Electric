#!/usr/bin/env python3
"""
Injects canonical + Open Graph + Twitter card tags and JSON-LD into the six
original pages. Idempotent: re-running replaces the managed block rather than
stacking duplicates.

The managed block is delimited by the SEO-BLOCK markers. Anything outside them
is left exactly as it was — this script does not touch layout, copy or the
inline var(--...) colour refs the pages carry.

Launch placeholder: every absolute URL uses https://REPLACE-DOMAIN
One find-replace of that literal string across the repo sets the whole site.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOMAIN = "https://REPLACE-DOMAIN"

OG_IMG = f"{DOMAIN}/assets/mills-van.jpg"
OG_IMG_W, OG_IMG_H = "1280", "852"
OG_IMG_ALT = "A Mills Electric crew member working inside an open service panel"

BEGIN = "<!-- SEO-BLOCK:BEGIN (managed by tools/seo-head.py — edit there, not here) -->"
END = "<!-- SEO-BLOCK:END -->"

# ---------------------------------------------------------------------------
# The LocalBusiness/Electrician node. Referenced by @id from the other pages
# so there is exactly one business entity across the site.
#
# ADDRESS AND GEO ARE DELIBERATE PLACEHOLDERS. See growth/NAP-CONFLICT.md.
# CLAUDE.md says 155 Main St; BBB, D&B, BuildZoom, Manta, Yahoo and the Google
# Business Profile pin all say 233 Copeland St. Not guessing. Logan confirms
# with the owner, then the two placeholder blocks below get real values.
# ---------------------------------------------------------------------------
BIZ_ID = f"{DOMAIN}/#electrician"

ELECTRICIAN = """{
  "@context": "https://schema.org",
  "@type": "Electrician",
  "@id": "%(biz)s",
  "name": "Mills Electric Inc",
  "url": "%(domain)s/",
  "telephone": "+15085862955",
  "email": "Millselectricinc@gmail.com",
  "image": "%(img)s",
  "logo": "%(domain)s/assets/logos/reversed-logo-on-black.png",
  "description": "Residential and commercial electrical work in Brockton and across the South Shore. Panel upgrades, EV charging, generators, lighting, and 24/7 emergency service.",
  "foundingDate": "1979",
  "priceRange": "$$",
  "currenciesAccepted": "USD",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "ADDRESS_UNCONFIRMED",
    "addressLocality": "Brockton",
    "addressRegion": "MA",
    "postalCode": "02301",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "GEO_UNCONFIRMED",
    "longitude": "GEO_UNCONFIRMED"
  },
  "hasCredential": {
    "@type": "EducationalOccupationalCredential",
    "credentialCategory": "license",
    "name": "MA Master Electrician #A-12245"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "07:00",
      "closes": "17:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Saturday",
      "opens": "07:00",
      "closes": "12:00"
    }
  ],
  "areaServed": [
%(areas)s
  ],
  "sameAs": [
    "https://maps.app.goo.gl/pc68XnQNeTdRhR8U7"
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "5.0",
    "reviewCount": "4",
    "bestRating": "5",
    "worstRating": "1"
  }
}"""

# Brockton plus the eight towns that now have their own pages. The published
# service-area table on index.html also lists East Bridgewater, West Bridgewater
# and Rockland; they are included here because the site already claims them.
AREA_TOWNS = [
    "Brockton", "Abington", "Avon", "Bridgewater", "East Bridgewater",
    "West Bridgewater", "Easton", "Holbrook", "Randolph", "Rockland",
    "Stoughton", "Whitman",
]


def areas_json(indent="    "):
    return ",\n".join(
        '%s{ "@type": "City", "name": "%s", "addressRegion": "MA", "addressCountry": "US" }'
        % (indent, t)
        for t in AREA_TOWNS
    )


# ---------------------------------------------------------------------------
# FAQ — lifted verbatim from the existing <details> blocks. Nothing invented.
#
# The same six Q&As are printed on index.html, services.html AND contact.html.
# FAQPage markup is emitted on index.html ONLY: Google treats the same FAQPage
# repeated across several URLs as duplicate structured data, and the home page
# is the strongest host for it.
# ---------------------------------------------------------------------------
FAQ = [
    ("What residential electrical services do you handle?",
     "Panel and service upgrades, rewiring, new circuits, outlets and switches, lighting, "
     "ceiling fans, EV chargers, generators, and smoke and CO detectors. If it is on a "
     "circuit in your house, we work on it."),
    ("Where should I start if I do not know what is wrong?",
     "Call and describe what you are seeing. Most problems we can narrow down over the "
     "phone, and we will tell you whether it needs a visit or whether it is something you "
     "can check yourself first."),
    ("Do you take small jobs as well as large ones?",
     "Yes. A single dead outlet is a normal call for us. There is no minimum job size, and "
     "we quote small work the same way we quote a full service upgrade."),
    ("Do you pull permits?",
     "We pull the permit on any work that requires one, meet the inspector ourselves, and "
     "hand you the closed-out paperwork. You do not have to coordinate any of it."),
    ("How fast can you get here in an emergency?",
     "We answer emergency calls 24/7. Response time depends on where you are in our "
     "service area — see the town list for typical windows."),
    ("Are you licensed and insured?",
     "Yes. We hold a MA Master Electrician #A-12245 and carry full liability and workers "
     "compensation insurance. Certificates are available on request."),
]


def faq_json():
    items = ",\n".join(
        """    {
      "@type": "Question",
      "name": %s,
      "acceptedAnswer": { "@type": "Answer", "text": %s }
    }""" % (jstr(q), jstr(a))
        for q, a in FAQ
    )
    return """{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": "%s/#faq",
  "mainEntity": [
%s
  ]
}""" % (DOMAIN, items)


def jstr(s):
    import json
    return json.dumps(s, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Services — the six the page already describes, with the "Typically includes"
# bullets reused verbatim as the service catalogue.
# ---------------------------------------------------------------------------
SERVICES = [
    ("panel", "Panel upgrades",
     "100A to 200A service, breaker replacement, and fixing the fuse box that your insurer keeps asking about.",
     ["Service upgrades to 200A", "Panel and breaker replacement", "Fuse box removal",
      "Meter socket repair", "Whole-home surge protection"]),
    ("residential", "Residential",
     "Rewiring, new circuits, outlets and switches, ceiling fans, and troubleshooting the breaker that keeps tripping.",
     ["Knob-and-tube replacement", "New circuits and outlets", "Ceiling fans and fixtures",
      "Troubleshooting and repair", "Smoke and CO detectors"]),
    ("commercial", "Commercial",
     "Tenant fit-outs, three-phase service, lighting retrofits, and scheduled maintenance for small commercial buildings.",
     ["Tenant fit-outs", "Three-phase service", "Lighting retrofits",
      "Scheduled maintenance", "Code-violation corrections"]),
    ("ev", "EV charging",
     "Level 2 home chargers on a dedicated circuit, load calculation included so the install passes first time.",
     ["Level 2 charger installs", "Load calculations", "Dedicated 240V circuits",
      "Permit and inspection", "Multi-unit parking"]),
    ("generators", "Generators",
     "Standby generator installs with automatic transfer switches, plus annual service on units we did not put in.",
     ["Standby generator installs", "Automatic transfer switches", "Annual service and testing",
      "Interlock kits", "Portable generator inlets"]),
    ("lighting", "Lighting",
     "Recessed and under-cabinet lighting, exterior and security fixtures, and LED retrofits that cut the bill.",
     ["Recessed lighting", "Under-cabinet lighting", "Exterior and security",
      "LED retrofits", "Landscape lighting"]),
]


def services_json():
    blocks = []
    for anchor, name, desc, bullets in SERVICES:
        offers = ",\n".join(
            """        {
          "@type": "Offer",
          "itemOffered": { "@type": "Service", "name": %s }
        }""" % jstr(b) for b in bullets
        )
        blocks.append("""{
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": "%s/services.html#%s",
  "serviceType": %s,
  "name": %s,
  "description": %s,
  "provider": { "@id": "%s" },
  "areaServed": [
%s
  ],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": %s,
    "itemListElement": [
%s
    ]
  }
}""" % (DOMAIN, anchor, jstr(name), jstr(name), jstr(desc), BIZ_ID,
        areas_json("    "), jstr(name + " — typically includes"), offers))
    return blocks


def breadcrumb(label, path):
    return """{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "%s/" },
    { "@type": "ListItem", "position": 2, "name": %s, "item": "%s/%s" }
  ]
}""" % (DOMAIN, jstr(label), DOMAIN, path)


# ---------------------------------------------------------------------------
# Per-page head config. Titles and descriptions are the ones already on each
# page — reused, not rewritten.
# ---------------------------------------------------------------------------
PAGES = {
    "index.html": dict(
        canonical=f"{DOMAIN}/",
        og_url=f"{DOMAIN}/",
        og_type="website",
        noindex=False,
    ),
    "services.html": dict(
        canonical=f"{DOMAIN}/services.html",
        og_url=f"{DOMAIN}/services.html",
        og_type="website",
        noindex=False,
    ),
    "about.html": dict(
        canonical=f"{DOMAIN}/about.html",
        og_url=f"{DOMAIN}/about.html",
        og_type="website",
        noindex=False,
    ),
    "reviews.html": dict(
        canonical=f"{DOMAIN}/reviews.html",
        og_url=f"{DOMAIN}/reviews.html",
        og_type="website",
        noindex=False,
    ),
    "contact.html": dict(
        canonical=f"{DOMAIN}/contact.html",
        og_url=f"{DOMAIN}/contact.html",
        og_type="website",
        noindex=False,
    ),
    # 404 gets OG + a self-referencing canonical to satisfy the same contract as
    # every other page, plus noindex so it never enters the index. It is
    # deliberately the one page left out of sitemap.xml.
    "404.html": dict(
        canonical=f"{DOMAIN}/404.html",
        og_url=f"{DOMAIN}/404.html",
        og_type="website",
        noindex=True,
    ),
}


def jsonld_for(page):
    out = []
    if page == "index.html":
        out.append(ELECTRICIAN % dict(
            biz=BIZ_ID, domain=DOMAIN, img=OG_IMG, areas=areas_json()))
        out.append(faq_json())
    elif page == "services.html":
        out.append(breadcrumb("Services", "services.html"))
        out.extend(services_json())
    elif page == "about.html":
        out.append(breadcrumb("About us", "about.html"))
    elif page == "reviews.html":
        # BreadcrumbList only. No Review/aggregateRating node here on purpose:
        # Google disallows self-serving review markup for LocalBusiness, and the
        # rating already lives once on the Electrician node on index.html.
        out.append(breadcrumb("Reviews", "reviews.html"))
    elif page == "contact.html":
        out.append(breadcrumb("Contact", "contact.html"))
    elif page == "404.html":
        out.append(breadcrumb("Page not found", "404.html"))
    return out


def extract(html, tag_re, label):
    m = re.search(tag_re, html)
    if not m:
        sys.exit(f"could not find {label}")
    return m.group(1).strip()


def build_block(page, cfg, title, desc):
    L = [BEGIN,
         "<!-- Absolute URLs use the launch placeholder https://REPLACE-DOMAIN —",
         "     find-replace that exact literal across the repo at launch. -->"]
    if cfg["noindex"]:
        L.append('<meta name="robots" content="noindex, follow">')
    L.append(f'<link rel="canonical" href="{cfg["canonical"]}">')
    L += [
        f'<meta property="og:type" content="{cfg["og_type"]}">',
        '<meta property="og:site_name" content="Mills Electric Inc">',
        '<meta property="og:locale" content="en_US">',
        f'<meta property="og:title" content="{esc(title)}">',
        f'<meta property="og:description" content="{esc(desc)}">',
        f'<meta property="og:url" content="{cfg["og_url"]}">',
        f'<meta property="og:image" content="{OG_IMG}">',
        f'<meta property="og:image:width" content="{OG_IMG_W}">',
        f'<meta property="og:image:height" content="{OG_IMG_H}">',
        f'<meta property="og:image:alt" content="{esc(OG_IMG_ALT)}">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{esc(title)}">',
        f'<meta name="twitter:description" content="{esc(desc)}">',
        f'<meta name="twitter:image" content="{OG_IMG}">',
        f'<meta name="twitter:image:alt" content="{esc(OG_IMG_ALT)}">',
    ]
    for blob in jsonld_for(page):
        L.append('<script type="application/ld+json">')
        L.append(blob)
        L.append('</script>')
    L.append(END)
    return "\n".join(L) + "\n"


def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;")


def main():
    for page, cfg in PAGES.items():
        p = ROOT / page
        html = p.read_text(encoding="utf-8")

        # strip any previous managed block so this is re-runnable
        html = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n?",
                      "", html, flags=re.S)

        title = extract(html, r"<title>(.*?)</title>", f"{page} <title>")
        desc = extract(html, r'<meta name="description" content="(.*?)">',
                       f"{page} meta description")
        title = title.replace("&amp;", "&")
        desc = desc.replace("&amp;", "&").replace("&quot;", '"')

        block = build_block(page, cfg, title, desc)
        if "</head>" not in html:
            sys.exit(f"{page}: no </head>")
        html = html.replace("</head>", block + "</head>", 1)
        p.write_text(html, encoding="utf-8")
        print(f"  patched {page}")


if __name__ == "__main__":
    main()
