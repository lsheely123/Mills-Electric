# Mills Electric Inc — Complete Project Documentation

## BUSINESS INFORMATION

### Company Details
- **Name**: Mills Electric Inc
- **Type**: Electrical Contractor
- **Location**: 155 Main St, Brockton, MA 02301
- **License**: MA Master Electrician #A-12245

### Contact Information
- **Phone**: (508)-586-2955
- **Email**: Millselectricinc@gmail.com
- **Website**: https://github.com/lsheely123/Mills-Electric
- **Google Maps**: https://maps.app.goo.gl/pc68XnQNeTdRhR8U7

### Business Hours
- Monday–Friday: 7am–5pm
- Saturday: 7am–12pm
- Sunday: Closed
- Emergency: 24/7

### Company Stats
- Years in business: 18
- Permits pulled: 2,400+
- Median emergency response: 4 hours
- Workmanship warranty: 3 years

---

## GOOGLE RATINGS & REVIEWS

### Current Rating
- **Average**: 5.0 stars
- **Total Reviews**: 4
- **5-star Rating**: 100%

### Customer Reviews (Real - From Google Maps)

**1. Jose Oliveira** | 2024 | ⭐⭐⭐⭐⭐
> "I've had the pleasure of relying on Mills Electric for over 8 years for commercial and residential jobs. They arrive promptly at the scheduled time, and are well-prepared with the necessary tools and equipment."

**2. Candis West** | 2022 | ⭐⭐⭐⭐⭐
> "Mills electric is a reliable company to service your electrical needs."

**3. María "Loja"** | 2025 | ⭐⭐⭐⭐⭐
> (Rating only)

**4. James Kelleher** | 2020 | ⭐⭐⭐⭐⭐
> (Rating only)

---

## WEBSITE STRUCTURE

### Pages (6 total)
1. **index.html** - Home page
   - Hero section with electrician photo
   - Services overview (6 cards)
   - Google rating snapshot
   - Why Mills section with stats
   - Process (4 steps)
   - Service area table
   - FAQ section
   - CTA band

2. **services.html** - Services detail
   - Panel upgrades
   - Residential
   - Commercial
   - EV charging
   - Generators
   - Lighting

3. **about.html** - Company background
   - Mission and history
   - Credentials card
   - Stats grid
   - Service area coverage

4. **reviews.html** - Customer testimonials
   - Google rating snapshot
   - 4 real customer reviews
   - CTA to Google Maps

5. **contact.html** - Contact & estimates
   - Estimate request form
   - Direct contact info
   - Business hours
   - Service area map
   - FAQ section

6. **404.html** - Error page
   - Branded 404 message
   - Navigation back to home

---

## DESIGN SYSTEM

### Colors
- **Primary Navy**: #07224B (headers, buttons, footer)
- **Accent Yellow/Volt**: #FFCB1F (highlights, CTAs)
- **Light Mist**: #F0F4FA (section backgrounds)
- **Text Navy**: #1A2332
- **Muted Gray**: #64748B

### Typography
- **Headings**: Archivo Black (bold, all-caps for impact)
- **Body**: Inter 400/500/600/700 (readable, professional)
- **Code/Data**: JetBrains Mono (technical elements)

### Components
- Buttons (primary, secondary, outline styles)
- Cards (service cards, review cards)
- Form inputs and textareas
- Star rating display (⭐ SVG icons)
- Snapshot grid (ratings display)

### CSS File
- `assets/site.css` - All styling

---

## ASSETS & IMAGES

### Logo Files (assets/logos/)
- `reversed-logo-on-navy.png` - White logo on dark background (footer)
- `primary-logo-on-white.png` - Navy logo on light background
- `me-mark-alone.png` - Mark only (no text)
- Favicons: 32px, 192px, 180px, 512px

### Photography
- `assets/crew-panel.jpg` - Electrician working in panel (hero image)
- `assets/mills-electric-map.png` - Google Maps screenshot (service area)

### Brand Assets (brand_assets/)
- `mills-electric-brand-book.html` - Full brand guidelines
- `tokens.css` - Color and spacing tokens
- Logos folder with all variations

---

## CONTENT DETAILS

### Service Categories
1. **Panel Upgrades** - 100A to 200A service, breaker replacement
2. **Residential** - Rewiring, new circuits, troubleshooting
3. **Commercial** - Tenant fit-outs, three-phase, retrofits
4. **EV Charging** - Level 2 home chargers, load calculations
5. **Generators** - Standby units, transfer switches
6. **Lighting** - Recessed, under-cabinet, exterior, LED retrofits

### Service Area (Towns Covered)
- Same day: Brockton, Abington, Avon, Holbrook, Randolph, Stoughton, Whitman
- Next day: Bridgewater, East Bridgewater, West Bridgewater, Easton, Rockland

### Key Messages
- "Wired right the first time"
- "The panel is cleaner than we found it"
- "Four steps, no surprises"
- "Every circuit gets labelled. Every permit gets pulled."

---

## TECHNICAL SETUP

### Git Repository
- **Remote**: https://github.com/lsheely123/Mills-Electric.git
- **Branch**: main
- **Commits**: 2 (initial + placeholder update)

### File Structure
```
/Users/logansheely/Web Design/
├── index.html
├── about.html
├── services.html
├── reviews.html
├── contact.html
├── 404.html
├── make-deploy.sh
├── CLAUDE.md
├── Mills_Electric_Project.md (this file)
├── assets/
│   ├── site.css
│   ├── crew-panel.jpg
│   ├── mills-electric-map.png
│   └── logos/
├── brand_assets/
│   ├── mills-electric-brand-book.html
│   ├── tokens.css
│   └── logos/
├── deploy/ (auto-generated)
│   ├── *.html
│   └── assets/
└── tools/, _archive/, temporary screenshots/
```

### Deployment
- **Build**: Run `./make-deploy.sh` 
- **Deploy to**: Cloudflare Pages (`deploy/` folder)
- **Excludes**: brand_assets/, tools/, _archive/, screenshots/

### Form Integration
- **Service**: Lead Connector (GHL)
- **Webhook URL**: Stored in contact.html `data-webhook`
- **Fallback**: Opens visitor's email app if webhook fails

---

## REVISION CHECKLIST

When updating this site, follow this order:

### 1. Update Business Info (if changed)
- [ ] Phone number (find/replace across all 6 pages)
- [ ] Email address (find/replace across all 6 pages)
- [ ] Address or hours
- [ ] License number

### 2. Update Ratings (if changed)
- [ ] index.html snapshot (lines ~72-85)
- [ ] reviews.html snapshot (lines ~51-64)
- [ ] Average rating number
- [ ] Total reviews count
- [ ] Percentage of 5-star reviews

### 3. Update Reviews (if changed)
- [ ] Delete old reviews from reviews.html
- [ ] Add new review HTML (name, date, stars, text)
- [ ] Keep to 4 reviews for layout

### 4. Update Images (if changed)
- [ ] Replace crew-panel.jpg in assets/
- [ ] Replace mills-electric-map.png in assets/
- [ ] Images appear in: index.html (line 56), contact.html (line 136)

### 5. Update Links (if changed)
- [ ] Google Maps link (currently: https://maps.app.goo.gl/pc68XnQNeTdRhR8U7)
- [ ] Location in all 4 pages that reference it

### 6. Before Pushing
- [ ] Run: `./make-deploy.sh`
- [ ] Check deploy/ folder has latest changes
- [ ] `git status` to see all changes
- [ ] Verify no stale phone numbers or emails remain
- [ ] `git add .` → `git commit -m "Update [description]"`
- [ ] `git push` to GitHub

---

## COMMON UPDATES

### Changing Phone Number
```bash
# Replace (508)-586-2955 with new number across all files
sed -i '' 's/(508)-586-2955/(NEW-NUMBER)/g' *.html
```

### Changing Email
```bash
# Replace Millselectricinc@gmail.com with new email
sed -i '' 's/Millselectricinc@gmail.com/newemail@domain.com/g' *.html
```

### Updating Google Ratings
1. Visit: https://maps.app.goo.gl/pc68XnQNeTdRhR8U7
2. Get current: average, total count, 5-star %
3. Find these lines and update:
   - index.html: `<div class="snap-n">5.0</div>` (line 73)
   - index.html: `<div class="snap-n">4</div>` (line 78)
   - index.html: `<div class="snap-n">100%</div>` (line 82)
   - Same in reviews.html (lines 52, 57, 61)

### Adding New Review
```html
<article class="review">
  <div class="review-top">
    <span class="avatar" aria-hidden="true">XX</span>
    <span>
      <span class="review-name">Full Name</span><br>
      <span class="review-date"><time datetime="YYYY">Month Year</time></span>
    </span>
  </div>
  <span class="stars " role="img" aria-label="5 out of 5 stars">
    <!-- 5 star SVGs here -->
  </span>
  <p class="review-body">Review text here...</p>
</article>
```

---

## SECURITY NOTES

### GitHub
- PAT was used for initial push (consider revoking)
- Token was removed from .git/config
- Only push via `origin` remote

### Form Integration
- GHL webhook URL stored in contact.html
- Fallback email: Millselectricinc@gmail.com
- All form submissions go through GHL or email

---

## DEPLOYMENT SCRIPT (make-deploy.sh)

```bash
#!/bin/sh
# Assembles the publishable site into deploy/ — drag that folder into Cloudflare Pages.
# Everything not listed here (brand_assets, tools, _archive, screenshots) stays private.
set -e
cd "$(dirname "$0")"
rm -rf deploy
mkdir -p deploy
cp index.html services.html about.html contact.html reviews.html 404.html deploy/
cp -R assets deploy/
echo "deploy/ ready — $(find deploy -type f | wc -l | tr -d ' ') files, $(du -sh deploy | cut -f1)"
find deploy -type f | sed 's|^deploy/|  |' | sort
```

**To run**: `./make-deploy.sh` from the project root

---

## GIT WORKFLOW

### Initial Setup (already done)
```bash
# Initialize repo
git init

# Create .gitignore
# Contents:
.DS_Store
.claude/
node_modules/
*.log
temporary screenshots/

# Add all files
git add .

# First commit
git commit -m "Initial commit: Mills Electric 5-page website"

# Add remote
git remote add origin https://github.com/lsheely123/Mills-Electric.git

# Push to GitHub
git push -u origin main
```

### For Updates
```bash
# See what changed
git status

# Add specific files
git add index.html contact.html assets/

# Commit with message
git commit -m "Update business contact info"

# Push to GitHub
git push
```

### View History
```bash
git log --oneline
```

---

## HTML TEMPLATE STRUCTURE

### Header (on all pages)
```html
<header class="masthead">
  <div class="wrap masthead-in">
    <a class="logo-link" href="index.html" aria-label="Mills Electric Inc home">
      <img src="assets/logos/reversed-logo-on-navy.png" alt="Mills Electric Inc" width="132" height="85">
    </a>
    <nav class="nav" aria-label="Main">
      <a class="navlink" href="index.html">Home</a>
      <a class="navlink" href="services.html">Services</a>
      <a class="navlink" href="about.html">About</a>
      <a class="navlink" href="reviews.html">Reviews</a>
      <a class="navlink" href="contact.html">Contact</a>
      <a class="btn btn-onnavy btn-sm" href="tel:+15085862955">
        <svg><!-- phone icon --></svg>(508)-586-2955
      </a>
    </nav>
  </div>
</header>
```

### Footer (on all pages)
```html
<footer class="foot">
  <div class="wrap" style="padding-block:64px">
    <div class="grid gap-8" style="grid-template-columns:repeat(auto-fit,minmax(180px,1fr))">
      <div>
        <img src="assets/logos/reversed-logo-on-navy.png" alt="Mills Electric Inc" width="148" height="95" style="margin-bottom:24px">
        <p class="t-small" style="color:var(--navy-400); max-width:32ch">
          Electrical contractor serving Brockton and the South Shore.
        </p>
      </div>
      <div>
        <h4>Services</h4>
        <a href="services.html#panel">Panel upgrades</a>
        <a href="services.html#residential">Residential</a>
        <!-- ... more links ... -->
      </div>
      <div>
        <h4>Contact</h4>
        <a href="tel:+15085862955" style="font-weight:600; color:var(--white)">(508)-586-2955</a>
        <a href="mailto:Millselectricinc@gmail.com">Millselectricinc@gmail.com</a>
        <p class="t-small" style="color:var(--navy-400); margin-top:12px; line-height:1.5">
          Mon–Fri 7am–5pm<br>Sat 7am–12pm<br><span style="font-size: 0.85em;">24/7 for emergencies</span>
        </p>
      </div>
    </div>
  </div>
</footer>
```

### Google Rating Snapshot (index.html & reviews.html)
```html
<div class="snapshot">
  <div class="snapshot-head">
    <svg><!-- checkmark icon --></svg>
    <span class="t-eyebrow">Google rating snapshot</span>
  </div>
  <div class="snapshot-body">
    <div class="snap-cell">
      <div class="snap-n">5.0</div>
      <span class="stars " role="img" aria-label="5 out of 5 stars">
        <!-- 5 star SVGs -->
      </span>
      <div class="snap-l">Average rating</div>
    </div>
    <div class="snap-cell">
      <div class="snap-n">4</div>
      <div class="snap-l">Total Google reviews</div>
    </div>
    <div class="snap-cell">
      <div class="snap-n">100%</div>
      <div class="snap-l">Rated five stars</div>
    </div>
  </div>
  <div class="snapshot-foot">
    <a class="btn btn-outline btn-sm" href="https://maps.app.goo.gl/pc68XnQNeTdRhR8U7" rel="noopener">View on Google Maps</a>
  </div>
</div>
```

### Review Card (reviews.html)
```html
<article class="review">
  <div class="review-top">
    <span class="avatar" aria-hidden="true">JO</span>
    <span>
      <span class="review-name">Jose Oliveira</span><br>
      <span class="review-date"><time datetime="2024">2024</time></span>
    </span>
  </div>
  <span class="stars " role="img" aria-label="5 out of 5 stars">
    <!-- 5 star SVGs -->
  </span>
  <p class="review-body">Review text here...</p>
</article>
```

---

## KEY FILES & THEIR PURPOSES

| File | Purpose |
|------|---------|
| `index.html` | Homepage with hero, services, ratings, FAQ |
| `services.html` | Detailed service offerings |
| `about.html` | Company background and credentials |
| `reviews.html` | Customer testimonials |
| `contact.html` | Contact form and direct contact info |
| `404.html` | Error page |
| `assets/site.css` | All styling |
| `assets/crew-panel.jpg` | Hero image |
| `assets/mills-electric-map.png` | Service area map |
| `assets/logos/` | All logo variations |
| `make-deploy.sh` | Build script for deployment |
| `.gitignore` | Git ignore rules |
| `CLAUDE.md` | Quick context for AI updates |
| `Mills_Electric_Project.md` | This complete documentation |

---

## TESTING CHECKLIST

Before each push, verify:

- [ ] All phone numbers are (508)-586-2955
- [ ] All emails are Millselectricinc@gmail.com
- [ ] Business hours show: Mon–Fri 7am–5pm, Sat 7am–12pm
- [ ] Google ratings are current (5.0, 4 reviews, 100%)
- [ ] Hero image loads (crew-panel.jpg)
- [ ] Service area map loads (mills-electric-map.png)
- [ ] All links work (internal and external)
- [ ] Google Maps link: https://maps.app.goo.gl/pc68XnQNeTdRhR8U7
- [ ] Mobile responsive (test in browser dev tools)
- [ ] No broken images or 404s
- [ ] Form submits properly
- [ ] `./make-deploy.sh` runs without errors
- [ ] deploy/ folder has all files

---

## COMMON PROBLEMS & SOLUTIONS

### Phone/Email Not Updating
**Problem**: Changed in one place but not everywhere
**Solution**: Use find/replace across all HTML files
```bash
# Mac/Linux:
sed -i '' 's/old-phone/new-phone/g' *.html

# Linux:
sed -i 's/old-phone/new-phone/g' *.html
```

### Images Not Showing
**Problem**: Image path wrong
**Solution**: 
- Check file is in `assets/` folder
- Verify filename (case-sensitive on servers)
- Use `src="assets/filename.jpg"` not `src="./assets/filename.jpg"`

### Form Not Sending
**Problem**: GHL webhook not working
**Solution**:
1. Check webhook URL in contact.html `data-webhook` attribute
2. Fallback will open user's email app
3. Verify email link: `mailto:Millselectricinc@gmail.com`

### deploy/ folder not updating
**Problem**: Run `./make-deploy.sh` but old files still there
**Solution**: Script should delete and rebuild automatically
```bash
# Manual rebuild:
rm -rf deploy
./make-deploy.sh
```

### GitHub push fails
**Problem**: Authentication error
**Solution**:
```bash
# Use PAT:
git push https://[YOUR_PAT]@github.com/lsheely123/Mills-Electric.git main

# Or update remote:
git remote set-url origin https://[YOUR_PAT]@github.com/lsheely123/Mills-Electric.git
git push
```

---

## FOR FUTURE CLIENT PROJECTS

1. **Copy this file** as a template
2. **Replace all Mills Electric info** with new client details
3. **Update the file paths** if structure changes
4. **Keep the structure** - it works!
5. **Save in each client's folder** as `[ClientName]_Project.md`

---

## QUICK REFERENCE COMMANDS

```bash
# Check status
git status

# See recent changes
git log --oneline -5

# Build for deployment
./make-deploy.sh

# Push changes
git push

# Check for stale content
grep -r "555-0147\|millselectric.example\|placehold.co" *.html

# View file structure
find . -type f -name "*.html" -o -name "*.css" -o -name "*.jpg" -o -name "*.png" | sort
```

---

## CONTACT INFORMATION FOR REFERENCE

- **Business Phone**: (508)-586-2955
- **Business Email**: Millselectricinc@gmail.com
- **GitHub Repository**: https://github.com/lsheely123/Mills-Electric
- **Google Maps**: https://maps.app.goo.gl/pc68XnQNeTdRhR8U7
- **Office Address**: 155 Main St, Brockton, MA 02301

---

*Last updated: September 10, 2026*
*Created by: Claude with Logan Sheely*
*Contains: Complete business info, code samples, deployment instructions, troubleshooting, and templates*
