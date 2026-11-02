#!/usr/bin/env python3
"""Mills Electric — switch the site from staging to its real domain in one step.

Run from the project folder once Charlie has confirmed the street address and the
domain has been bought:

    python3 tools/go-live.py --domain millselectricinc.com --street "233 Copeland St"
    python3 tools/go-live.py --domain ... --street ... --lat 42.05 --lng -71.02
    python3 tools/go-live.py ... --no-deploy        # change files only

What it does, in order:
  1. Writes the confirmed street into the Electrician JSON-LD (index.html) and into
     the two places a visitor sees the address (index.html footer, contact.html).
  2. Writes --lat/--lng into the schema's geo block. Without them it removes the geo
     block instead: a LocalBusiness with no coordinates is fine, junk ones are not.
     For 233 Copeland St the Google Business Profile pin is 42.0535487, -71.0209167
     (growth/NAP-CONFLICT.md); for any other address, look the coordinates up.
  3. Replaces every https://REPLACE-DOMAIN (canonicals, Open Graph, JSON-LD,
     sitemap.xml, robots.txt and both generator scripts) with https://<domain>.
  4. Regenerates the town pages, refuses to continue if any placeholder survives,
     then builds and uploads to Cloudflare Pages (./make-deploy.sh --deploy).

It changes tracked files, so review `git diff` and commit afterwards. Attaching the
domain to the Pages project is a dashboard step; the script prints it at the end.
"""
import argparse
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLACEHOLDER = "https://REPLACE-DOMAIN"
OLD_STREET = "155 Main St"          # what the visible copy says today
SKIP_DIRS = {"deploy", "_archive", ".git", "node_modules", "brand_assets", "growth"}


def die(msg):
    print(f"go-live: {msg}", file=sys.stderr)
    sys.exit(1)


def files_with_placeholder():
    out = []
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix not in {".html", ".xml", ".txt", ".py"}:
            continue
        rel = p.relative_to(ROOT)
        if rel.parts[0] in SKIP_DIRS or p.name == "go-live.py":
            continue
        if PLACEHOLDER in p.read_text(encoding="utf-8"):
            out.append(p)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--domain", required=True, help="bare domain, e.g. millselectricinc.com")
    ap.add_argument("--street", required=True, help='confirmed street line, e.g. "233 Copeland St"')
    ap.add_argument("--lat", type=float)
    ap.add_argument("--lng", type=float)
    ap.add_argument("--no-deploy", action="store_true", help="change files but do not build/upload")
    a = ap.parse_args()

    domain = a.domain.strip().lower().removeprefix("https://").removeprefix("http://").rstrip("/")
    if not re.fullmatch(r"(?:[a-z0-9-]+\.)+[a-z]{2,}", domain) or domain.endswith("pages.dev"):
        die(f"'{a.domain}' does not look like a real domain")
    street = a.street.strip()
    if not re.fullmatch(r"\d+[A-Za-z]? [A-Za-z0-9 .'-]+", street):
        die(f"'{street}' does not look like a street line (expected e.g. '233 Copeland St')")
    if (a.lat is None) != (a.lng is None):
        die("give both --lat and --lng, or neither")

    index = ROOT / "index.html"
    s = index.read_text(encoding="utf-8")
    if "ADDRESS_UNCONFIRMED" not in s:
        die("index.html has no ADDRESS_UNCONFIRMED — has this already been run?")

    # 1. schema street
    s = s.replace('"streetAddress": "ADDRESS_UNCONFIRMED"', f'"streetAddress": "{street}"')
    # 2. schema geo
    geo = re.compile(r',\n  "geo": \{\n    "@type": "GeoCoordinates",\n'
                     r'    "latitude": "GEO_UNCONFIRMED",\n    "longitude": "GEO_UNCONFIRMED"\n  \}')
    if not geo.search(s):
        die("could not find the GEO_UNCONFIRMED block in index.html")
    if a.lat is not None:
        s = geo.sub(f',\n  "geo": {{\n    "@type": "GeoCoordinates",\n'
                    f'    "latitude": {a.lat},\n    "longitude": {a.lng}\n  }}', s)
    else:
        s = geo.sub("", s)
    index.write_text(s, encoding="utf-8")

    # 1b. visible address
    if street != OLD_STREET:
        for name in ("index.html", "contact.html"):
            p = ROOT / name
            t = p.read_text(encoding="utf-8")
            if OLD_STREET not in t:
                die(f"{name}: expected '{OLD_STREET}' in the visible address")
            p.write_text(t.replace(OLD_STREET, street), encoding="utf-8")

    # 3. domain
    changed = files_with_placeholder()
    for p in changed:
        p.write_text(p.read_text(encoding="utf-8").replace(PLACEHOLDER, f"https://{domain}"),
                     encoding="utf-8")
    print(f"go-live: domain set in {len(changed)} files")

    # 4. regenerate, verify, build
    subprocess.run([sys.executable, str(ROOT / "tools" / "make-town-pages.py")], check=True,
                   cwd=ROOT, stdout=subprocess.DEVNULL)
    left = [str(p.relative_to(ROOT)) for p in files_with_placeholder()]
    for p in ROOT.glob("*.html"):
        if re.search(r"ADDRESS_UNCONFIRMED|GEO_UNCONFIRMED", p.read_text(encoding="utf-8")):
            left.append(p.name)
    if left:
        die("placeholders still present in: " + ", ".join(sorted(set(left))))

    if not a.no_deploy:
        subprocess.run([str(ROOT / "make-deploy.sh"), "--deploy"], check=True, cwd=ROOT)

    print(f"""
go-live: files are set for https://{domain}. Remaining steps:
  1. Cloudflare dashboard > Workers & Pages > mills-electric > Custom domains:
     add {domain} and www.{domain} (DNS is automatic when the domain is on Cloudflare).
  2. Check https://{domain} loads, then review `git diff` and commit.
  3. Google Search Console: add the domain property and submit https://{domain}/sitemap.xml.
  4. Google Business Profile: set the website to https://{domain}/ and make the
     address match "{street}".
""")


if __name__ == "__main__":
    main()
