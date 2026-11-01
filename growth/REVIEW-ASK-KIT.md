# Review ask kit — Mills Electric Inc

**Prepared 2026-10-21. Everything here is a DRAFT for Logan. Nothing has been sent to
anyone.** No customer was contacted, no profile was touched, no account was logged into.

The goal is the number in `growth/COMPETITOR-REVIEW-GAP.md`: **18 more Google reviews to
reach the competitor median of 22.**

A note on voice before anything else. Every word below is written to sound like a man who
has been wiring houses in Brockton since 1979 — short sentences, no adjectives he wouldn't
use out loud, no "we value your feedback," no "delighted," no exclamation points. If any
of it reads like it came from a marketing company, it will not get used, and it will not
work. **If a line feels wrong in the owner's mouth, cut it. A plainer ask beats a
polished one.**

---

## 0. Read this first — the two rules that are not negotiable

These are Google's rules, not preferences. Violating them can get every review on the
profile deleted, or the profile suspended — which would be strictly worse than the four
reviews Mills has now.

**1. No gating.** You may not ask "how did we do?" first and then send the review link
only to the people who answer well. Filtering for happy customers before showing the link
is prohibited. **Every customer gets the same link, regardless of how the job went.**

**2. No incentives.** No discount, no gift card, no entry into a drawing, no $10 off the
next service call, no free anything in exchange for a review. Not even for an honest one.
Not even if you'd give it to anyone who left a bad review too.

Also out, for the same reason: writing reviews for customers, asking employees or family
to review, posting from a second account, and buying reviews from anybody.

**Nothing in this kit does any of those things.** It is all one thing: asking a satisfied
customer, plainly, to say what happened. That is the only method that is both allowed and
durable.

Source: Google's prohibited and restricted content policy for Maps —
https://support.google.com/contributionpolicy/answer/7400114 (checked 2026-10-21).

---

## (a) The link

### The direct Google review write-link

```
https://search.google.com/local/writereview?placeid=ChIJ__92kEOF5IkRCliR7A5iOEY
```

Clicking this opens the Google review box for Mills Electric with the stars ready. It
works on phones and desktop. On a phone it hands off to the Google Maps app if it's
installed.

**How it was derived, and how confident to be.** CLAUDE.md lists the Maps short link
`https://maps.app.goo.gl/pc68XnQNeTdRhR8U7`. On 2026-10-21 that returned `HTTP/2 302` to:

```
https://www.google.com/maps/place/Mills+Electric+Inc./@42.0535527,-71.023497,17z/
data=!3m1!4b1!4m6!3m5!1s0x89e485439076ffff:0x4638620eec91580a!8m2!
3d42.0535487!4d-71.0209167!16s%2Fg%2F11h3vc3zr_
```

The pair `0x89e485439076ffff:0x4638620eec91580a` is the listing's CID. Encoded into
Google's Place ID format it gives `ChIJ__92kEOF5IkRCliR7A5iOEY`. Both
`search.google.com/local/writereview?placeid=…` and
`google.com/maps/place/?q=place_id:…` returned **HTTP 200** for it when checked.

> **UNVERIFIED:** I could not read the rendered page to see "Mills Electric Inc." printed
> back, because Google serves a JavaScript shell to automated fetching. The endpoints
> answer 200 and the ID is derived from Google's own identifier, so this is very likely
> correct — **but click it once yourself before it goes on a printed card.** Thirty
> seconds now beats five hundred cards pointing at the wrong business.

**Also useful:**

| Purpose | URL |
|---|---|
| Opens the listing (not the review box) | `https://www.google.com/maps?cid=5059901997588764682` |
| Same, Place ID form | `https://www.google.com/maps/place/?q=place_id:ChIJ__92kEOF5IkRCliR7A5iOEY` |

### The short `g.page` link — owner must generate this

The long link works fine in a text message, where it becomes a tappable bubble and nobody
reads it. **For anything printed or said out loud, the short link is much better.** Google
issues one free, but only to the verified profile owner.

**I did not attempt this and could not — it requires being signed in as the owner.**
Steps for Charles Mills (or whoever holds the profile login):

1. Sign in to the Google account that manages the Mills Electric listing — the one that
   was used to verify it.
2. Search Google for `my business`, or go to the Business Profile directly from Maps
   while signed in. (The standalone Google Business Profile Manager site was retired;
   management now happens in Search and Maps.)
3. Find **"Ask for reviews"** / **"Get more reviews."** It usually sits in the profile's
   main action row next to Edit Profile, Read Reviews, and Messages.
4. Google displays a short review link, typically in the form `https://g.page/r/XXXXXXXX/review`.
5. Use **Copy link**. Save it somewhere permanent — the truck binder, Logan's notes, and
   the bottom of this file.
6. Paste it into the texts, the email, the print card and the QR code, replacing the long
   link everywhere.

**If no one can get into that account, stop and fix that first.** An unclaimed or
inaccessible Business Profile is a bigger problem than the review count — it also blocks
every fix in `growth/LISTINGS-AUDIT.md` (the hours, the website field, the address).
Verify ownership before running the 90-day plan.

**Paste the short link here once you have it:**

```
g.page short link:  ________________________________________
Retrieved by: ______________  Date: __________
```

---

## (b) The text message

Send it **the same afternoon**, from the truck, while the customer is still standing in a
room that works again. A text sent three days later converts a fraction as well.

### Residential — 232 characters

```
Hi [Name] - Charles from Mills Electric. Thanks for having us out today.
If the work looks good to you, would you mind leaving us a quick review
on Google? Takes about a minute and it genuinely helps a small shop like
ours. [LINK] - Thanks, Charles
```

Within the 300-character limit with room for a longer first name and the short link.

**Why it is built this way:**
- Says who it is in the first four words. An unknown number asking for anything gets
  deleted.
- **"If the work looks good to you"** is the honest version of the ask. It is not gating —
  the link is right there either way, and it goes to everyone. It just doesn't presume.
- "Takes about a minute" removes the real objection, which is never willingness, it's
  effort.
- "a small shop like ours" is true and is the reason people actually do it.
- Signed with a first name. Not "The Mills Electric Team."

### Commercial — 251 characters

```
[Name] - Charles Mills. Thanks for the work at [site] today. If you were
happy with how we handled it, a short Google review would help us a lot
with other property and facility folks looking for a licensed shop. [LINK]
Appreciate it. - Charles
```

**What changed and why:** names the *site*, not "your home" — a facilities manager runs
six buildings and needs to know which one. "how we handled it" is the commercial
yardstick: scheduling, tenant disruption, cleanup, inspection. And it gives a reason
aimed at him specifically — his review gets read by his peers, which is a small piece of
professional standing, not a favor.

### Rules for sending

- **One text. Never a second one.** No follow-up, no "just bumping this." A reminder text
  about a review is how a good customer becomes an irritated one. The in-person script in
  (d) handles follow-up properly.
- Send from the phone that did the job, if possible. The number is recognized.
- Always use the customer's actual first name. Never "Valued Customer."
- Never send to someone you had a dispute with, who hasn't paid, or whose job isn't
  finished and inspected.

---

## (c) The email

For commercial accounts, property managers, and older residential customers who don't
text. Longer, but not by much.

**Subject lines — pick one:**
- `Quick favor - Mills Electric`
- `Thanks for today - one small ask`
- *(commercial)* `[Site name] - and a quick favor`

**Body:**

```
[Name],

Thanks again for having us out [today / last week] for the [panel upgrade /
service call / generator work].

I'll ask you something I've never been any good at asking. We've been
doing electrical work in Brockton since 1979, and in all that time I've
barely asked anybody to review us online. We have four reviews. Most of
the shops we're up against have thirty or forty.

If you were happy with the work, would you leave us a short review on
Google? Two sentences is plenty - what we did and whether we showed up
when we said we would. Here's the link:

[LINK]

If something wasn't right, call me instead and I'll come back out.

Thanks,
Charles Mills
Mills Electric Inc.
(508) 586-2955
MA Master Electrician #A-12245
```

**Why the honest paragraph is in there.** "We have four reviews, our competitors have
thirty" is a specific, slightly uncomfortable true thing, and it converts better than any
amount of polish, because it turns the ask from a marketing request into a favor for a
person. The 1979 date and the licence number do the credibility work without a word of
self-praise.

**"Two sentences is plenty"** matters more than it looks. The reason people agree and then
never do it is that they imagine writing a paragraph. Tell them the real size of the job.

**"If something wasn't right, call me instead"** is the part to get right. This is *not*
gating — the review link is above it, unconditional, and it goes to every customer.
It is the ordinary thing a tradesman says. Do not restructure this into "click here if
happy / click here if unhappy." That version is a policy violation.

> **Note for Logan:** the email address in CLAUDE.md is `Millselectricinc@gmail.com`.
> **The `millselectricinc.com` domain is registered but serving nothing** — see
> §2.2 of `growth/LISTINGS-AUDIT.md`. Sort out whether the owner controls that domain
> before printing an email address anywhere; a `@millselectricinc.com` address may be
> available and would look considerably better on a commercial bid.

---

## (d) The 60-second in-person ask

**This is the highest-converting asset in this kit by a wide margin**, and it is the one
nobody practices. A face-to-face ask from the person who did the work converts several
times better than any text. The text's job is to be the link; the conversation's job is
to be the ask.

**Timing:** after the work is done, after you've shown them it works, tools packed,
standing by the door. Not while you're still on the ladder. Not before payment is
settled.

### The script

> **"Before I take off — can I ask you a favor? It'll take you a minute."**
>
> *(wait for them to say yes — they will)*
>
> **"We've been doing this in Brockton since '79, and I've never been any good at asking
> people to put something online. We've got four reviews on Google. The outfits we're
> bidding against have thirty, forty. And that's most of how people pick an electrician
> now."**
>
> **"If you were happy with how today went, would you leave us a couple sentences on
> Google? Doesn't need to be anything fancy — just what we did, and whether we showed up
> when we said we would."**
>
> *(then, and this is the part that matters)*
>
> **"I'll text you the link right now while I'm standing here, so you've got it."**
>
> *(send the text from (b) — on the spot, in front of them)*
>
> **"Appreciate it. And if anything acts up, you call me direct."**

### Why each beat is there

| Beat | What it does |
|---|---|
| "Can I ask you a favor" | Asks permission. They say yes to the small thing and are now listening. |
| "It'll take you a minute" | Sets the size before they can imagine it bigger. |
| "since '79" + "four reviews" | Specific and a little humbling. People help a person; they ignore a company. |
| "that's most of how people pick an electrician now" | The reason. Not a complaint — a fact they already know. |
| "a couple sentences … what we did, whether we showed up" | Removes the blank page. Most people's whole barrier is not knowing what to write. |
| **"I'll text you the link right now while I'm standing here"** | **The single most important line in this kit.** Converts intent into a link already on their phone. |
| "if anything acts up, call me direct" | Ends on service, not on the ask. |

### When they say "sure" and nothing happens

**This is the normal outcome, not a failure.** Most people mean it and then life happens.
Roughly three-quarters of sincere yeses never turn into a review without a nudge. Here's
the discipline:

**Do not send a second text. Ever.** It reads as nagging and costs more goodwill than the
review is worth.

**Instead:**

**1. The same-day text is the follow-up.** It already exists, it's already on their phone,
and it has the link in it. That's one nudge, delivered before they could forget. For most
customers that is where it ends, either way.

**2. Keep a list.** One sheet in the truck, or a note on the phone: name, date, job, and
whether they said yes. Two columns — *asked* and *posted*. Check Google once a week; it's
four reviews, you'll notice a new one. **Without this list you cannot tell the difference
between "nobody will do it" and "we only asked six people."** That distinction decides
whether the next ninety days are worth running.

**3. Use the next natural contact — never a manufactured one.** If they call you back for
anything at all — another job, a question, an estimate, a part — handle their thing first,
completely. Then, at the end:

> **"Hey — one thing. I sent you a link a while back about a Google review. No pressure at
> all, I know you're busy. But if you get a spare minute it really does help us."**

Said once, warmly, inside a conversation they started. Then let it go. **If it doesn't
land the second time, it is finished.** Never a third.

**4. The one case worth a deliberate call-back:** a large job, a long-standing customer,
or a commercial account where a review is genuinely valuable. Call — don't text — and be
straight about why you're calling:

> **"I'm calling about one thing and it's a favor, so tell me no if it's a bother. That
> review I mentioned — we're trying to get our Google page up where it ought to be, and
> yours would carry real weight because you've used us for years."**

Being direct that it's a favor is what makes it easy to say yes to. See
`growth/REACTIVATION-LIST.md` — that's exactly the call to make to Jose Oliveira.

**5. If they say no, or go quiet twice — that's the answer. Mark the list and move on.**
A customer who keeps calling Mills for twenty years is worth more than a review.

---

## (e) The print leave-behind card

**File: `growth/review-card.html`** — open it in a browser and print.

It is deliberately in `growth/`, **not `assets/`**. CLAUDE.md is explicit that
`make-deploy.sh` copies all of `assets/`, so anything dropped there gets published. This
card is an internal print asset and must never ship with the site. **Do not move it.**

Built on the v3.1 tokens from `brand_assets/tokens.css`: Graphite Black `#0B0B0C`,
Brushed Gold `#DFAD37`, Signal Red `#E90206`, Archivo Black headings, Inter body. It
respects the brand rules — gold is flat with a **black** label, red appears once as a
hairline and never against gold, and there is no red button.

Prints two cards per US Letter sheet. Cut along the dashed line.

### Generating the QR code — free, no account

The card has a large empty box where the QR goes. I did not generate one, because the QR
must encode the **short `g.page` link** from §(a), which only the owner can produce. Once
you have it:

**Option 1 — the QR Code generator inside Google Business Profile.** Some profiles offer
a downloadable QR alongside the "Ask for reviews" link. Check there first; it's already
pointed at the right place and costs nothing.

**Option 2 — a free generator.** Any of these work with no signup and no watermark:
`qr.io`, `qrcode-monkey.com`, `the-qrcode-generator.com`. Paste the link, pick **PNG at
1000×1000 or larger** (or SVG if offered), download, drop it into the box in
`review-card.html` replacing the placeholder `<div>` with an `<img>`.

**Option 3 — offline, no website at all.** With Python installed:
`pip install qrcode[pil]` then
`python3 -c "import qrcode; qrcode.make('PASTE_LINK').save('qr.png')"`.

**Three rules for the QR:**
1. **Avoid any generator that makes you sign up, or that offers a "dynamic" or "trackable"
   QR.** Those route through the vendor's server and stop working the day the free trial
   ends — with your cards already printed. **Static only.**
2. **Print it at least 1 inch square**, ideally 1.25". Smaller and phone cameras struggle
   in a dim hallway.
3. **Scan the printed card with an actual phone before printing five hundred.** Test it
   from about two feet away, in poor light. This is the step people skip.

### Where the cards go

- One left with the customer at the end of every job, handed over with the (d) script —
  **not** left silently on a counter.
- A stack in each truck.
- Clipped to every invoice that gets mailed or emailed.
- Given to the customer even when you've already texted them the link. Two ways to reach
  the same page is fine; two separate asks is not.

---

## (f) The 90-day cadence

The principle: **start with the people most likely to say yes.** Early wins keep the habit
alive. Starting with cold five-year-old customers produces silence in week one and the
whole thing gets dropped.

Target: **18 reviews in 90 days**, reaching the competitor median of 22.

---

### Days 1–7 — Setup. Zero asks.

Do not ask a single customer this week. Get the plumbing right first — an ask that lands
on a broken link is worse than no ask.

| # | Task | Who |
|---|---|---|
| 1 | Confirm who can sign in to the Google Business Profile. **If nobody can, everything stops here.** | Owner |
| 2 | Generate the `g.page` short link, §(a). Save it in three places. | Owner |
| 3 | Click the review link on a phone. Confirm it opens the box for **Mills Electric Inc.** | Owner |
| 4 | Verify the hours on the profile — Saturday is wrong on at least two listings (`LISTINGS-AUDIT.md` §2.3). A customer who finds wrong hours doesn't become a reviewer. | Owner |
| 5 | Generate and test the QR. Print 50 cards to start, not 500. | Logan |
| 6 | Set up the tracking sheet: name, date, job, asked, posted. | Owner |
| 7 | Read the two rules in §0 out loud to anyone who will be asking. | Owner |

---

### Days 8–30 — The warm list. Target: 8 reviews.

**Ask in this order. The order is the whole method.**

**Tier 1 — the four named existing reviewers (Days 8–14).**
They have already publicly endorsed Mills. The highest-probability asks in the entire
business. Full scripts in **`growth/REACTIVATION-LIST.md`** — note that two of them are
*not* being asked for a review at all, because they already left one.

**Tier 2 — every job completed in the last 30 days (Days 8–21).**
Recent, specific, the work is fresh. Text from §(b) the same day for anything still
closing; for jobs already finished, one text, one time, no follow-up.

**Tier 3 — the repeat residential customers (Days 15–30).**
Anyone who has called Mills two or more times. They've already voted with their phone.
Owner knows these names without a list. Call, don't text — use the §(d) language adapted
for the phone, and send the link while you're on the call.

---

### Days 31–60 — Every new job, without exception. Target: 7 reviews.

This is where it becomes a habit instead of a campaign.

- **Every completed job gets the §(d) ask and the §(b) text. Every one.** Not the ones
  that went especially well — all of them. Selecting for happy customers is the gating
  violation in §0.
- Card left behind on every job.
- Commercial accounts get the email version, §(c), since the person who hires you often
  isn't the person on site.
- **Week 6 check:** pull the tracking sheet. If *asked* is high and *posted* is low, the
  link is the problem — retest it. If *asked* is low, the ask isn't happening, and that's
  a conversation, not a tooling fix.

---

### Days 61–90 — The back catalogue. Target: 3+ reviews.

Now the colder list, after the habit is established and there are 10–15 reviews on the
page making the profile look alive.

- Customers from the last 1–3 years, in order of **how big the job was** — a panel
  upgrade or a generator install is remembered; a single outlet is not.
- Commercial and property-management accounts: ask for the named reference as well as the
  review (see `REACTIVATION-LIST.md`).
- Anyone who said yes earlier and didn't post — **one** nudge, only inside a conversation
  they started. §(d) step 3.
- **Day 90:** recount. Re-run the competitor numbers in `COMPETITOR-REVIEW-GAP.md`; they
  will have moved too.

---

### What "good" looks like

| Milestone | Reviews | What it means |
|---|---:|---|
| Start | 4 | Last of nine in the market |
| ~9 | 9 | Passes Landerholm (8) and WS Anderson (6) — **second in Brockton proper** |
| ~22 | 22 | **Hits the competitor median.** The target. |
| ~39 | 39 | Passes John Page (38) — **first in Brockton on both volume and rating** |

Counts are as of 2026-10-21 and will drift. Sources in `COMPETITOR-REVIEW-GAP.md`.

**If 90 days produces 10 instead of 18, that is still a 150% increase and a market-position
change.** The failure mode is not a low conversion rate. It is not asking.

---

## Quick reference — the one-page version

| | |
|---|---|
| **Review link** | `https://search.google.com/local/writereview?placeid=ChIJ__92kEOF5IkRCliR7A5iOEY` |
| **Short link** | *owner to generate — §(a)* |
| **When to ask** | End of the job, in person, before leaving |
| **Then** | Text the link **while standing there** |
| **Follow-up** | Only inside a conversation they start. Once. Never a third time. |
| **Never** | Incentives · gating · asking only happy customers · a second reminder text |
| **Target** | 18 more reviews → 22 total → market median |
