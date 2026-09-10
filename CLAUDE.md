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
- **Logos**: assets/logos/ (reversed-logo-on-navy.png for dark backgrounds)

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
- **Primary color**: Navy (#07224B)
- **Accent color**: Volt/Yellow (#FFCB1F)
- **Font**: Inter (body), Archivo Black (headings)
- **CSS**: assets/site.css

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
