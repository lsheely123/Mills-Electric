# Mills Electric Inc — Website

## Business Details
- **Company**: Mills Electric Inc
- **Phone**: (508)-586-2955
- **Email**: Millselectricinc@gmail.com
- **Address**: 155 Main St, Brockton, MA 02301
- **Hours**: Mon–Fri 7am–5pm, Sat 7am–12pm, 24/7 emergencies

## Online Presence
- **GitHub**: https://github.com/lsheely123/Mills-Electric
- **Google Maps**: https://maps.app.goo.gl/pc68XnQNeTdRhR8U7
- **License**: MA Master Electrician #A-00000

## Current Google Ratings
- **Average**: 5.0 stars
- **Total reviews**: 4
- **5-star percentage**: 100%

## Key Assets
- **Hero image**: assets/crew-panel.jpg (electrician at panel)
- **Service area map**: assets/mills-electric-map.png (Brockton location)
- **Brand logos (v2.0, current)**: brand_assets/logos/ — `me-primary`, `me-primary-reversed`,
  `me-horizontal`, `me-horizontal-reversed`, `me-mark`, `me-mark-reversed`,
  `me-badge-circle`, `me-badge-hex`, `me-mono-{navy,white,yellow,red}`
  - Original artwork: brand_assets/logos/_source/
  - Superseded v1 files: brand_assets/logos/_v1/
- **Site logos**: assets/logos/ — **still v1 artwork** (no red bolt). The website has not yet
  been migrated to the v2.0 logos or the Signal Red palette.

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
- **index.html** — Home page with hero, services overview, ratings snapshot
- **services.html** — Detailed service offerings
- **about.html** — Company background and credentials
- **reviews.html** — Full review list and Google rating
- **contact.html** — Contact form, hours, map, estimate request
- **404.html** — Error page

## Design System
Source of truth: `brand_assets/mills-electric-brand-book.html` (v2.0). Tokens mirrored in
`brand_assets/tokens.css`. If anything disagrees, the brand book wins.

- **Primary color**: Navy (#07224B)
- **Accent color**: Volt/Yellow (#FECA04)
- **Trim color**: Signal Red (#E4151B) — added in brand book v2.0
- **Color mix**: roughly 65% navy/neutrals, 25% white, 8% yellow, 2% red
- **Font**: Inter (body), Archivo Black (headings)
- **CSS**: assets/site.css

### Signal Red rules
- Red is **trim, not a theme**: hairlines, a sheared edge, the emergency badge, the lockup itself.
- At most **one** red button per site — the 24/7 emergency CTA — with a **white** label.
- Never `#E4151B` on navy (3.30:1); use `#FF6B6F` on navy surfaces.
- Never red directly against yellow (3.09:1); put navy or white between them.
- Status `danger` is `#A4161A`, deliberately deeper than brand red.

## Deployment
- Run `./make-deploy.sh` to build the `deploy/` folder
- Deploy folder ready for Cloudflare Pages
- Excludes: brand_assets/, tools/, _archive/, screenshots/

## For Revisions & Updates
When making changes:
1. Update contact info here first
2. Keep phone, email, and hours consistent across all 6 HTML pages
3. Update Google ratings in index.html and reviews.html snapshots
4. Rebuild deploy/ folder before pushing: `./make-deploy.sh`
5. Commit and push with clear message: `git commit -m "Update [what changed]"`

## Notes
- GitHub PAT was used for initial push — consider revoking after first push for security
- Contact.html had a revert issue; always verify it after IDE edits
- Review text for Jose Oliveira is truncated at source (Google screenshot)
- María and James reviews are rating-only from the Google source
