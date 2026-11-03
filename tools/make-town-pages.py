#!/usr/bin/env python3
"""
Generates the eight town service-area pages.

Why a generator: the masthead, band CTA and footer must stay byte-identical to
the six original pages. Hand-maintaining that across eight files guarantees
drift. Edit the chrome here once; re-run; all eight stay in step.

What is NOT generated: the per-town copy. Each town has its own hand-written
housing-stock and electrical-reality text in TOWNS below. These are not doorway
clones — if you find yourself templating the prose, stop.

Ground rules baked in, per CLAUDE.md and the brief:
  - logo <img> sizes are hardcoded: masthead mark 96x39 (me-mark-gold.png), footer 165x95.
  - v3.1 palette only. Gold buttons take BLACK labels. No red on gold.
    These pages introduce no new colour; they reuse existing classes.
  - No claim that is not already on the site. The only numbers used are the
    published 3hr median, the per-town rows from index.html's service-area
    table, and the licence number.
  - No invented job counts, no invented testimonials.

Launch placeholder: absolute URLs use https://REPLACE-DOMAIN
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOMAIN = "https://REPLACE-DOMAIN"
BIZ_ID = f"{DOMAIN}/#electrician"

PHONE_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
             'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6'
             'A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1'
             'L8 9.8a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>')

CHECK_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
             'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<path d="M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 '
             '4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 '
             '4 4 0 0 1 0-6.76z"/><path d="m9 12 2 2 4-4"/></svg>')

SERVICE_LINKS = [
    ("panel", "Panel upgrades"),
    ("residential", "Residential"),
    ("commercial", "Commercial"),
    ("ev", "EV charging"),
    ("generators", "Generators"),
    ("lighting", "Lighting"),
]

# ---------------------------------------------------------------------------
# Per-town copy. Hand-written. `std` and `emerg` are copied verbatim from the
# service-area table already published on index.html — the only response-time
# figures on these pages, alongside the published 3hr median.
# ---------------------------------------------------------------------------
TOWNS = [
    dict(
        name="Abington", zips=["02351"], std="Same day", emerg="Under 2 hr",
        title="Electrician in Abington, MA — Mills Electric Inc",
        desc="Licensed electrician serving Abington, MA. Panel upgrades, knob-and-tube "
             "replacement, EV chargers and 24/7 emergency calls. Free estimates.",
        h1="Electrician in<br>Abington",
        lead="Abington is a short run up Route 18 from our shop in Brockton. "
             "Same-day on standard calls, and we know the housing stock here.",
        stock_h2="What Abington is built out of",
        stock=[
            "Abington grew outward from its rail stop and the Route 18 and 123 corridors, "
            "and the age of a house here tells you most of what you need to know about its "
            "wiring. The older center is wood-frame homes and capes from roughly 1900 to "
            "1940. Push out from there and you are into postwar ranches from the fifties "
            "and sixties, then subdivisions from the eighties onward.",
            "The pre-war stock near the center is where we spend most of our time. That is "
            "where 60-amp fuse services are still in place, and where knob-and-tube turns up "
            "once you get a light into the attic — cloth-insulated conductors on porcelain "
            "knobs, spliced in open air, with no ground anywhere in the circuit.",
        ],
        seen_title="Common in Abington",
        seen=[
            "60-amp fuse panels in pre-war homes",
            "Knob-and-tube in attics and exterior walls",
            "Two-prong outlets with no equipment ground",
            "Overloaded kitchen circuits added decades later",
            "Service upgrades requested by a home insurer",
        ],
        reality_h2="A 1920s service and a modern load",
        reality=[
            "An EV charger is the clearest example of the problem. A Level 2 charger wants a "
            "dedicated 240V circuit pulling 40 or 48 amps continuously. On a 60-amp service "
            "that was sized for lighting, a range and not much else, there is simply no room "
            "for it — and no honest installer can make room without upgrading the service.",
            "So the first thing we do on an older Abington house is a load calculation, not a "
            "quote for the charger. It tells you whether you are buying a charger install or a "
            "service upgrade with a charger on the end of it. Either way you get the number "
            "before we start, and we pull the permit and meet the inspector ourselves.",
        ],
    ),
    dict(
        name="Whitman", zips=["02382"], std="Same day", emerg="Under 2 hr",
        title="Electrician in Whitman, MA — Mills Electric Inc",
        desc="Licensed electrician serving Whitman, MA. Panel and service upgrades in older "
             "village-center homes, EV chargers, generators, 24/7 emergency calls.",
        h1="Electrician in<br>Whitman",
        lead="Whitman's village center is some of the oldest housing stock we work in, "
             "and it has its own set of problems. Same-day on standard calls.",
        stock_h2="What Whitman is built out of",
        stock=[
            "Whitman's center is dense with two-storey wood-frame houses put up for the shoe "
            "and boot trade between the 1890s and the 1920s. Narrow lots, detached garages set "
            "back behind the house, and basements of fieldstone or brick laid up in mortar.",
            "Those basements matter more than people expect. A panel bolted to a damp "
            "fieldstone wall corrodes at the lugs and the neutral bar, and corrosion at a "
            "termination is a heat problem before it is anything else. When we open a panel "
            "down there the first thing we look at is the condition of the connections, not "
            "the breaker count.",
        ],
        seen_title="Common in Whitman",
        seen=[
            "Corrosion at panel lugs in damp fieldstone basements",
            "100A panels fitted in the 1970s or 80s, now full",
            "Cloth-insulated branch circuits behind plaster",
            "Sub-panels needed for a dryer or charger circuit",
            "Weatherhead and service mast damage after storms",
        ],
        reality_h2="The house that has already been upgraded once",
        reality=[
            "Most Whitman center homes are not untouched. They have been through one upgrade "
            "already: a 100-amp panel dropped in thirty or forty years ago, which was generous "
            "at the time. It is now full, with tandem breakers doubled up in slots that were "
            "never meant to take them, and the original cloth-insulated branch circuits still "
            "running out of it behind the plaster.",
            "That puts you in an awkward middle. Adding a dryer circuit or an EV charger means "
            "either a sub-panel, if the service can still carry the load, or a full service "
            "upgrade if it cannot. We do the load calculation first and tell you which one you "
            "are actually looking at. If something behind the plaster changes the number once "
            "we are in, we stop and tell you before we carry on.",
        ],
    ),
    dict(
        name="Easton", zips=["02356 North Easton", "02375 South Easton"],
        std="Next day", emerg="Under 3 hr",
        title="Electrician in Easton, MA — Mills Electric Inc",
        desc="Licensed electrician serving Easton, North Easton and South Easton, MA. "
             "Generator installs, panel upgrades, historic-home wiring, 24/7 emergency calls.",
        h1="Electrician in<br>Easton",
        lead="Easton runs from 19th-century North Easton village to large modern colonials "
             "on wooded lots. Those are two different electrical jobs.",
        stock_h2="What Easton is built out of",
        stock=[
            "Most of Easton is bigger lots and bigger houses — centre-entrance colonials and "
            "garrisons built from the sixties through the nineties, often with a finished "
            "basement, an attached garage and an outbuilding or two. Many are on a well and a "
            "septic system, which means pump circuits and alarm circuits that a town-water "
            "house does not have.",
            "Then there is North Easton village, which is a different century: 19th-century "
            "stone and timber around the Ames shovel works and the Richardson buildings. Those "
            "properties bring the opposite problem from the colonials. You cannot open a "
            "plaster-on-lath wall to fish a cable without doing real damage, so the work has to "
            "be planned around surface raceway, existing chases and whatever route the last "
            "electrician left behind.",
        ],
        seen_title="Common in Easton",
        seen=[
            "Standby generators and automatic transfer switches",
            "Well pump and septic alarm circuits",
            "Large colonials outgrowing a 100A service",
            "Outbuilding and garage feeders",
            "Historic properties where walls cannot be opened",
        ],
        reality_h2="Why generators come up more here",
        reality=[
            "Easton's distribution is largely overhead and runs through heavy tree cover. That "
            "combination is what makes a storm outage an Easton problem more than a downtown "
            "Brockton one, and it is why standby generators and transfer switches are a more "
            "common conversation on this side of the service area.",
            "Done properly that is a generator sized off an actual load calculation, an "
            "automatic transfer switch so the changeover does not depend on anyone being home, "
            "and a permit and inspection on the install. We also service standby units we did "
            "not put in — if yours has not been load-tested in a few years, it is worth knowing "
            "whether it will actually start before the night you need it.",
        ],
    ),
    dict(
        name="Stoughton", zips=["02072"], std="Same day", emerg="Under 3 hr",
        title="Electrician in Stoughton, MA — Mills Electric Inc",
        desc="Licensed electrician serving Stoughton, MA. Aluminum branch wiring repairs, "
             "panel upgrades, EV chargers and 24/7 emergency calls. Free estimates.",
        h1="Electrician in<br>Stoughton",
        lead="Stoughton has a specific wiring issue tied to when much of it was built. "
             "Worth knowing which side of it your house falls on.",
        stock_h2="What Stoughton is built out of",
        stock=[
            "Stoughton splits in two. Around the commuter rail station and the town centre "
            "there is older and denser stock, including a good number of two- and "
            "three-families. Out from there it is large postwar tracts — ranches and "
            "split-levels put up quickly across the fifties, sixties and early seventies.",
            "That build-out window is the thing to know about. A lot of Stoughton housing went "
            "up inside the years when aluminum was used for branch-circuit wiring, roughly 1965 "
            "to 1973, and that wiring is still in the walls.",
        ],
        seen_title="Common in Stoughton",
        seen=[
            "Aluminum branch-circuit wiring in 1965–1973 homes",
            "Split-level panels in tight utility closets",
            "Two- and three-family metering near the centre",
            "Original 100A services now running central air",
            "Receptacle and switch terminations running warm",
        ],
        reality_h2="Aluminum branch wiring, and what to do about it",
        reality=[
            "Aluminum expands and contracts more than copper under load. At a receptacle or "
            "switch screw, that cycling slowly works the termination loose, and a loose "
            "termination carrying current gets hot. It is the connections that fail, not the "
            "wire in the middle of the run — which is why the problem shows up at devices and "
            "in panels rather than inside the walls.",
            "There are two honest answers. Pigtail every device termination with connectors "
            "approved for copper-to-aluminum, which is the usual route, or rewire the affected "
            "circuits, which costs more and is sometimes the better call. What you should not "
            "do is hang a pile of new fixtures and smart switches off it without finding out "
            "what you have first. If your house is from that window, say so when you call and "
            "we will check the terminations while we are there.",
        ],
    ),
    dict(
        name="Randolph", zips=["02368"], std="Same day", emerg="Under 3 hr",
        title="Electrician in Randolph, MA — Mills Electric Inc",
        desc="Licensed electrician serving Randolph, MA. Two- and three-family metering and "
             "sub-panels, service upgrades, EV chargers, 24/7 emergency calls.",
        h1="Electrician in<br>Randolph",
        lead="Randolph has a lot of single-families that became two- and three-families. "
             "That conversion is where most of the electrical work is.",
        stock_h2="What Randolph is built out of",
        stock=[
            "Randolph was built out hard in the fifties and sixties — capes, ranches and "
            "split-levels, street after street of them. What makes Randolph different from "
            "Holbrook or Avon, which have similar stock, is how many of those single-families "
            "have since been converted into two- and three-family homes.",
            "We are based in Brockton, so multi-family is familiar ground; the triple-deckers "
            "here at home are a daily part of the work. But a purpose-built triple-decker and a "
            "converted Randolph cape are not the same animal. The triple-decker was wired as "
            "three units from the start. The conversion was wired as one house and then "
            "adapted, usually more than once, often without a permit.",
        ],
        seen_title="Common in Randolph",
        seen=[
            "Conversions with metering that was never properly separated",
            "A second kitchen fed off the original house panel",
            "Sub-panels in closets and other no-access locations",
            "Common-area lighting on a tenant's meter",
            "Original 100A service now carrying AC and two tenants",
        ],
        reality_h2="Getting a converted house metered properly",
        reality=[
            "The pattern we find most often is a second kitchen running off the original panel, "
            "a sub-panel put somewhere it should not be — a bedroom closet, behind a door that "
            "does not open fully — and hallway or basement lighting landing on whichever "
            "tenant's meter was closest. None of that is academic if you are the landlord: it "
            "is a billing dispute and an inspection problem waiting to happen.",
            "Sorting it out means each unit on its own meter and its own panel, common areas "
            "back on house power, and working clearance in front of every panel. It is a "
            "permit job and an inspection, both of which we handle. If you are buying a "
            "converted two-family here, this is the thing worth having looked at before you "
            "close rather than after.",
        ],
    ),
    dict(
        name="Holbrook", zips=["02343"], std="Same day", emerg="Under 2 hr",
        title="Electrician in Holbrook, MA — Mills Electric Inc",
        desc="Licensed electrician serving Holbrook, MA. Service upgrades on 1950s capes and "
             "ranches, storm damage repairs, EV chargers, 24/7 emergency calls.",
        h1="Electrician in<br>Holbrook",
        lead="Holbrook is small, close by, and mostly modest postwar homes — many still "
             "on the service they were built with. Same-day on standard calls.",
        stock_h2="What Holbrook is built out of",
        stock=[
            "Holbrook is a small town with modest housing stock: mostly capes and ranches from "
            "the 1950s build-out, on small lots, with some older homes closer to the centre. "
            "There is not a lot of new construction, which means a high proportion of houses "
            "are still working off something close to their original electrical service.",
            "In practice that is a 100-amp panel if somebody upgraded it at some point, or a "
            "60-amp fuse box if nobody ever did. Both are common here, and the fuse boxes are "
            "the ones that tend to surface when a house changes hands or an insurer starts "
            "asking questions.",
        ],
        seen_title="Common in Holbrook",
        seen=[
            "Original 60-amp fuse services never upgraded",
            "Finished cape attics on one overloaded added circuit",
            "Weatherhead and service mast damage under tree cover",
            "Small panels with no spare slots",
            "Two-prong outlets throughout",
        ],
        reality_h2="The finished attic on one circuit",
        reality=[
            "The classic Holbrook cape has a second floor that was finished after the fact, and "
            "almost always off a single circuit run up from below. One bedroom, sometimes two, "
            "plus whatever lighting — all on one 15-amp branch that was never intended to be "
            "anybody's living space. It works until someone puts a window air conditioner or a "
            "space heater up there, and then it does not.",
            "The fix is proper circuits for those rooms, which usually means spare capacity in "
            "the panel, which on a 60-amp fuse service means the service first. We will tell you "
            "the order the work has to happen in and what each stage costs, so you can do it in "
            "pieces if that suits you better.",
            "The other recurring Holbrook call is storm damage. Heavy tree cover over overhead "
            "service drops means a branch takes the weatherhead or bends the mast. That is an "
            "emergency call and we answer those any hour.",
        ],
    ),
    dict(
        name="Avon", zips=["02322"], std="Same day", emerg="Under 2 hr",
        title="Electrician in Avon, MA — Mills Electric Inc",
        desc="Licensed electrician serving Avon, MA. Commercial and industrial electrical work "
             "on the Route 24 corridor plus residential service upgrades. 24/7 emergency calls.",
        h1="Electrician in<br>Avon",
        lead="Avon is the one town on our list where the commercial side of the work comes "
             "up as often as the residential. We do both.",
        stock_h2="What Avon is built out of",
        stock=[
            "Avon is the smallest town we cover — a few thousand people — and its residential "
            "stock looks much like Holbrook's: modest older homes and small postwar lots, a lot "
            "of them still on their original service.",
            "What makes Avon different is everything along Route 24 and Route 28. For a town of "
            "its size, Avon carries a disproportionate amount of commercial and light-industrial "
            "space, and that changes the mix of work. Here the call is as likely to be a "
            "warehouse or a unit being turned over for a new tenant as it is a house.",
        ],
        seen_title="Common in Avon",
        seen=[
            "Three-phase service for light-industrial space",
            "High-bay and warehouse lighting retrofits",
            "Rooftop unit disconnects and whips",
            "Code-violation corrections before a tenant move-in",
            "Older small-town residential services",
        ],
        reality_h2="Fit-outs on a deadline",
        reality=[
            "Commercial work on the Route 24 corridor is usually a schedule problem as much as "
            "an electrical one. A tenant has a move-in date, the space needs power where the "
            "last tenant did not need it, and there is an inspection between you and occupancy. "
            "Three-phase service, panel and feeder work, lighting on the new layout, disconnects "
            "for rooftop units, and whatever the last fit-out left behind that will not pass.",
            "We pull our own permits and meet the inspector ourselves, which on a fit-out is "
            "the part that actually protects the date. We also quote in writing with parts and "
            "labour separated, so a landlord and a tenant can see what each of them is paying "
            "for. Scheduled maintenance on small commercial buildings is part of what we do "
            "too — see the commercial section on the services page for the detail.",
        ],
    ),
    dict(
        name="Bridgewater", zips=["02324"], std="Next day", emerg="Under 3 hr",
        title="Electrician in Bridgewater, MA — Mills Electric Inc",
        desc="Licensed electrician serving Bridgewater, MA. EV chargers, pool and hot tub "
             "circuits, generators and rental-property detector compliance. Free estimates.",
        h1="Electrician in<br>Bridgewater",
        lead="Bridgewater has the newest housing stock we work in. That flips the job from "
             "fixing old wiring to adding load to good wiring.",
        stock_h2="What Bridgewater is built out of",
        stock=[
            "Bridgewater is the newest of the eight towns on this list. Large subdivisions from "
            "the nineties and two-thousands make up much of it, alongside a historic centre and "
            "a substantial rental market around Bridgewater State University.",
            "That changes what we get called for. A 1995 subdivision colonial already has a "
            "200-amp service and a modern breaker panel. There is no knob-and-tube to replace "
            "and no fuse box to argue with the insurer about. The work here is additive — "
            "putting new load onto a system that can actually take it.",
        ],
        seen_title="Common in Bridgewater",
        seen=[
            "EV chargers on services with real spare capacity",
            "Pool and hot tub circuits — bonding and GFCI protection",
            "Finished basement circuits, lighting and egress",
            "Generator transfer switches on modern panels",
            "Smoke and CO detector compliance in student rentals",
        ],
        reality_h2="Adding load instead of chasing it",
        reality=[
            "An EV charger in a Bridgewater subdivision is usually the straightforward version "
            "of the job: the service has spare capacity, the panel has slots, and the run to "
            "the garage is short. We still do the load calculation — a second charger, or a "
            "charger plus a heat pump, can take a 200-amp service closer to its limit than "
            "people expect — but the answer is normally yes, and the install passes first time.",
            "Pool and hot tub circuits are the ones where the detail matters most. Equipotential "
            "bonding and the right GFCI protection are not optional and are exactly what an "
            "inspector will look at. We would rather do that properly than come back to it.",
            "The rental market around the university brings a different list: working smoke and "
            "CO detectors in the right locations, and enough properly protected outlets that "
            "nobody in the house is running a space heater off a power strip. If you are a "
            "landlord here, that is a worthwhile annual visit.",
        ],
    ),
]

for t in TOWNS:
    t["slug"] = f"electrician-{t['name'].lower()}-ma.html"


# ---------------------------------------------------------------------------
def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;")


def jstr(s):
    import json
    return json.dumps(s, ensure_ascii=False)


def masthead():
    return f"""<header class="masthead">
  <div class="wrap masthead-in">
    <a class="logo-link brand" href="index.html" aria-label="Mills Electric Inc home">
      <img src="assets/logos/me-mark-gold.png" alt="" width="96" height="39">
      <span class="brand-txt"><span class="brand-name">Mills Electric</span><span class="brand-sub">Inc · Since 1979</span></span>
    </a>
    <nav class="nav" aria-label="Main">
      <div class="navgroup">
        <a class="navlink" href="index.html">Home</a>
        <a class="navlink" href="services.html">Services</a>
        <a class="navlink" href="about.html">About</a>
        <a class="navlink" href="reviews.html">Reviews</a>
        <a class="navlink" href="contact.html">Contact</a>
      </div>
      <a class="btn btn-primary btn-sm" href="tel:+15085862955">{PHONE_SVG}(508)-586-2955</a>
    </nav>
  </div>
</header>"""


# The trust bar replaces the old .facts chips. Same four strings as index.html.
def trust():
    return """<div class="trust">
  <div class="wrap trust-in">
    <div class="trust-item"><span class="trust-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/></svg></span><span>MA Master Electrician #A-12245</span></div>
    <div class="trust-item"><span class="trust-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg></span><span>24/7 emergency</span></div>
    <div class="trust-item"><span class="trust-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 2v20l2-1 2 1 2-1 2 1 2-1 2 1 2-1 2 1V2l-2 1-2-1-2 1-2-1-2 1-2-1-2 1Z"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"/><path d="M12 17.5v-11"/></svg></span><span>Free estimates</span></div>
    <div class="trust-item"><span class="trust-icon"><svg viewBox="0 0 24 24" fill="currentColor" stroke="none" aria-hidden="true"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg></span><span>5.0 on Google</span><span class="stars" role="img" aria-label="5 out of 5 stars"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg></span></div>
  </div>
</div>"""


def band_and_footer():
    svc = "\n".join(
        f'        <a href="services.html#{a}">{n}</a>' for a, n in SERVICE_LINKS)
    return f"""<section class="band section">
  <div class="wrap grid auto-2 gap-12 items-center">
    <div>
      <h2 class="t-h2">Get a price<br>this week</h2>
      <p class="t-lead prose mt-6">Estimates are free and we do not charge a call-out fee to quote.
        Tell us what the problem is and we will tell you what it costs.</p>
    </div>
    <div class="band-cta">
      <a class="band-tel" href="tel:+15085862955">(508)-586-2955</a>
      <a class="btn btn-primary" href="contact.html">Request an estimate</a>
    </div>
  </div>
</section>
<footer class="foot">
  <img class="foot-bg" src="assets/footer-jobsite.jpg" alt="" width="1448" height="1086" loading="lazy" decoding="async">
  <div class="wrap foot-in">
    <div class="foot-grid">
      <div>
        <img class="foot-logo" src="assets/logos/reversed-logo-on-black.png" alt="Mills Electric Inc" width="165" height="95">
        <p class="t-small foot-blurb">
          Electrical contractor serving Brockton and the South Shore.
        </p>
      </div>
      <div>
        <h4>Services</h4>
{svc}
      </div>
      <div>
        <h4>Company</h4>
        <a href="about.html">About us</a>
        <a href="reviews.html">Reviews</a>
        <a href="contact.html">Contact</a>
        <a href="services.html">All services</a>
      </div>
      <div>
        <h4>Contact</h4>
        <a class="foot-tel" href="tel:+15085862955">(508)-586-2955</a>
        <a href="mailto:Millselectricinc@gmail.com">Millselectricinc@gmail.com</a>
        <h4>Hours</h4>
        <p class="t-small foot-meta">
          Mon–Fri 7am–5pm<br>Sat 7am–12pm<br><small>24/7 for emergencies</small>
        </p>
      </div>
    </div>
    <div class="foot-bottom">
      <p class="t-caption">&copy; 2026 Mills Electric Inc</p>
      <p class="t-caption right">MA Master Electrician #A-12245</p>
    </div>
  </div>
</footer>
<div class="callbar">
  <a class="btn btn-primary" href="tel:+15085862955"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2 4.2 2 2 0 0 1 4 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>Call (508)-586-2955</a>
  <a class="btn btn-ondark" href="contact.html">Get an estimate</a>
</div>"""


def jsonld(t):
    url = f"{DOMAIN}/{t['slug']}"
    city = ('{ "@type": "City", "name": %s, "addressRegion": "MA", "addressCountry": "US" }'
            % jstr(t["name"]))
    services = ",\n".join(
        '        { "@type": "Service", "name": %s, "url": "%s/services.html#%s" }'
        % (jstr(n), DOMAIN, a) for a, n in SERVICE_LINKS)
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Electrician",
  "@id": "{url}#business",
  "name": "Mills Electric Inc",
  "url": "{url}",
  "parentOrganization": {{ "@id": "{BIZ_ID}" }},
  "telephone": "+15085862955",
  "email": "Millselectricinc@gmail.com",
  "image": "{DOMAIN}/assets/mills-van.jpg",
  "logo": "{DOMAIN}/assets/logos/reversed-logo-on-black.png",
  "description": {jstr(t['desc'])},
  "foundingDate": "1979",
  "priceRange": "$$",
  "currenciesAccepted": "USD",
  "hasCredential": {{
    "@type": "EducationalOccupationalCredential",
    "credentialCategory": "license",
    "name": "MA Master Electrician #A-12245"
  }},
  "openingHoursSpecification": [
    {{
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "07:00",
      "closes": "17:00"
    }},
    {{
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Saturday",
      "opens": "07:00",
      "closes": "12:00"
    }}
  ],
  "areaServed": {city},
  "sameAs": ["https://maps.app.goo.gl/pc68XnQNeTdRhR8U7"],
  "makesOffer": {{
    "@type": "Offer",
    "itemOffered": [
{services}
    ]
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "{DOMAIN}/" }},
    {{ "@type": "ListItem", "position": 2, "name": "Service area", "item": "{DOMAIN}/#area" }},
    {{ "@type": "ListItem", "position": 3, "name": {jstr('Electrician in ' + t['name'] + ', MA')}, "item": "{url}" }}
  ]
}}
</script>"""


def build(t, others):
    url = f"{DOMAIN}/{t['slug']}"
    stock = "\n".join(
        f'      <p class="muted mt-{"6" if i == 0 else "4"}">\n        {p}\n      </p>'
        for i, p in enumerate(t["stock"]))
    seen = "\n".join(
        '        <li>\n'
        f'          {CHECK_SVG}<span>{x}</span></li>'
        for x in t["seen"])
    reality = "\n".join(
        f'      <p class="prose muted mt-{"6" if i == 0 else "4"}">\n        {p}\n      </p>'
        for i, p in enumerate(t["reality"]))
    svc_cards = "\n".join(
        f'''      <a class="card card-hover card-link" href="services.html#{a}">
        <h3 class="t-h4">{n}</h3>
      </a>''' for a, n in SERVICE_LINKS)
    zips = "\n".join(
        f'            <span class="chip">{z}</span>' for z in t["zips"])
    # outline buttons, not link-styled chips: a chip reads as a static label
    # (that is how about.html uses it), so a clickable one has no affordance.
    nearby = "\n".join(
        f'      <a class="btn btn-outline btn-sm" href="{o["slug"]}">{o["name"]}</a>'
        for o in others)

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t['title'])}</title>
<meta name="description" content="{esc(t['desc'])}">
<meta name="theme-color" content="#0B0B0C">
<link rel="icon" type="image/png" sizes="32x32" href="assets/logos/favicon-32.png?v=3.2">
<link rel="icon" type="image/png" sizes="192x192" href="assets/logos/favicon-192.png?v=3.2">
<link rel="apple-touch-icon" sizes="180x180" href="assets/logos/favicon-180.png?v=3.2">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap">
<link rel="stylesheet" href="assets/site.css">
<!-- Absolute URLs use the launch placeholder https://REPLACE-DOMAIN —
     find-replace that exact literal across the repo at launch. -->
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Mills Electric Inc">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{esc(t['title'])}">
<meta property="og:description" content="{esc(t['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/assets/mills-van.jpg">
<meta property="og:image:width" content="1448">
<meta property="og:image:height" content="1086">
<meta property="og:image:alt" content="The black Mills Electric work van, lettered in gold, parked outside a house in Brockton">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(t['title'])}">
<meta name="twitter:description" content="{esc(t['desc'])}">
<meta name="twitter:image" content="{DOMAIN}/assets/mills-van.jpg">
<meta name="twitter:image:alt" content="The black Mills Electric work van, lettered in gold, parked outside a house in Brockton">
{jsonld(t)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{masthead()}
<section class="pagehead">
  <!-- photo slot: swap src when job-site photos arrive -->
  <div class="pagehead-bg"><img src="assets/crew-panel.jpg" alt="" width="1280" height="852"></div>
  <div class="wrap"><div class="pagehead-copy">
    <p class="t-eyebrow crumb"><a href="index.html#area">Service area</a> &rsaquo; {t['name']}, MA</p>
    <h1 class="t-h1">{t['h1']}</h1>
    <p class="t-lead prose mt-6">{t['lead']}</p>
    <div class="actions">
      <a class="btn btn-primary" href="tel:+15085862955">{PHONE_SVG}Call (508)-586-2955</a>
      <a class="btn btn-ondark" href="contact.html">Request an estimate</a>
    </div>
  </div></div>
</section>
{trust()}
<main id="main">

<section class="section">
  <div class="wrap grid auto-2 gap-12 items-start">
    <div>
      <h2 class="t-h3">{t['stock_h2']}</h2>
{stock}
      <a class="btn btn-outline mt-8" href="services.html">See everything we do</a>
    </div>
    <div class="card">
      <p class="t-eyebrow muted">{t['seen_title']}</p>
      <ul class="check-list mt-6">
{seen}
      </ul>
    </div>
  </div>
</section>

<section class="section mist">
  <div class="wrap">
    <p class="t-eyebrow">{t['name']} specifics</p>
    <h2 class="t-h2 mt-3">{t['reality_h2']}</h2>
{reality}
  </div>
</section>

<section class="section">
  <div class="wrap grid auto-2 gap-12 items-start">
    <div>
      <p class="t-eyebrow">Getting to you</p>
      <h2 class="t-h2 mt-3">Booking a<br>{t['name']} call</h2>
      <p class="prose muted mt-6">
        We work out of Brockton, so {t['name']} is a local run for us. The two windows
        below are the ones already published in our service-area table; the 3hr figure is
        our median response across all emergency calls, everywhere we work. Emergency
        calls are answered 24/7.
      </p>
      <a class="btn btn-outline mt-8" href="contact.html">Request an estimate</a>
    </div>
    <div>
      <div class="card tbl-wrap">
        <table class="tbl">
          <thead><tr><th>Town</th><th>Standard call</th><th>Emergency</th></tr></thead>
          <tbody>
            <tr><td>{t['name']}</td><td class="t-data">{t['std']}</td><td class="t-data">{t['emerg']}</td></tr>
          </tbody>
        </table>
      </div>
      <div class="grid gap-8 mt-8 two-up">
        <div class="stat">
          <div class="stat-n">3hr</div>
          <p class="t-small muted mt-3">Median response on emergency calls</p>
        </div>
        <div>
          <p class="t-eyebrow muted">{'ZIP codes' if len(t['zips']) > 1 else 'ZIP code'}</p>
          <div class="chips mt-3">
{zips}
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="t-eyebrow">What we do in {t['name']}</p>
    <h2 class="t-h2 mt-3">All six, here<br>as anywhere</h2>
    <p class="t-lead prose muted mt-6">
      The full detail on each one — what it covers and what it typically includes — is on
      the <a href="services.html" class="link-gold">services page</a>.
    </p>
    <div class="grid auto-3 gap-6 mt-12">
{svc_cards}
    </div>
  </div>
</section>

<section class="section mist">
  <div class="wrap">
    <p class="t-eyebrow">Nearby</p>
    <h2 class="t-h2 mt-3">Other towns<br>we cover</h2>
    <div class="chips mt-8">
{nearby}
    </div>
    <p class="muted mt-8">
      The full list, including East Bridgewater, West Bridgewater and Rockland, is on the
      <a href="index.html#area" class="link-gold">home page</a>. If your town is not
      on it, call and ask — we take work outside the list regularly.
    </p>
  </div>
</section>

</main>
{band_and_footer()}
<script src="assets/site.js" defer></script>
</body>
</html>
"""


def main():
    for t in TOWNS:
        others = [o for o in TOWNS if o["name"] != t["name"]]
        (ROOT / t["slug"]).write_text(build(t, others), encoding="utf-8")
        print(f"  wrote {t['slug']}")


if __name__ == "__main__":
    main()
