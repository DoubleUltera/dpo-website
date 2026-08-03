# DPO Consulting Website - Project Documentation

## Project Overview

This is a professional consulting website for **Atty. Renerio de Dios Jr.**, a **TÜV Certified Data Protection Officer** for Region 8 (Eastern Visayas), Philippines. The website is designed to establish market dominance for DPO consulting services while offering complementary notarial services.

### Business Context

**Client Profile:**
- Licensed attorney and notary public
- TÜV Certified DPO (Certificate #7000532, valid until 2029)
- Based in Tacloban City, Leyte
- Target market: All of Region 8 (Leyte, Samar, Biliran)
- Dual services: DPO consulting (primary) + Notarial services (complementary)

**Project Goals:**
1. Dominate Region 8 DPO consulting market through SEO and thought leadership
2. Generate qualified leads via contact form (custom pricing model)
3. Build credibility through blog content and TÜV certification
4. Minimize operational costs (target: ₱600-800/year)
5. Enable non-technical client to manage blog independently

**Success Metrics:**
- 10+ qualified leads per month
- 50+ organic search visitors per day
- 5+ blog posts ranking on Google page 1
- 1,000+ monthly website visitors by Month 6

## Technical Architecture

### Technology Stack Rationale

**Astro 6.x** - Static Site Generator
- **Why:** Fastest loading times (95+ PageSpeed score), SEO-optimized, zero JavaScript by default
- **Alternative considered:** WordPress (rejected due to cost: ₱2,000-5,000/year hosting + security issues)
- **Cost:** FREE (open-source)

**Decap CMS** - Git-based Content Management
- **Why:** No backend database, easy WYSIWYG editor at `/admin`, free, integrates with Netlify Identity
- **Alternative considered:** Traditional database CMS (rejected due to complexity and cost)
- **Cost:** FREE (open-source)

**Netlify** - Hosting + CDN + Forms
- **Why:** 100GB/month free bandwidth, automatic HTTPS, built-in forms, seamless GitHub integration
- **Alternative considered:** Traditional shared hosting (rejected due to cost and manual deployment)
- **Cost:** FREE (within limits)

**EmailJS** - Contact Form Automation
- **Why:** 200 free emails/month, dual email workflow (user auto-reply + attorney notification)
- **Alternative considered:** Backend email service (rejected due to complexity)
- **Cost:** FREE (within limits)

**Tailwind CSS v4** - Styling Framework
- **Why:** Professional design system, mobile-first utilities, performance optimized
- **Note:** Had to use vanilla CSS instead of @apply due to v4 syntax changes
- **Cost:** FREE (open-source)

### Total Cost Analysis

**Year 1:**
- Domain registration: ₱600-800
- Everything else: ₱0

**Annual Recurring:**
- Domain renewal: ₱600-800
- All services: ₱0

**Optional Upgrades (if business scales):**
- Professional email: ₱0-1,200/year (Zoho free tier available)
- Netlify Pro: ₱1,000/month (if >100GB bandwidth)
- EmailJS Pro: ₱500/month (if >200 form submissions)

**ROI Calculation:**
- Website cost: ₱800/year
- DPO consulting fee: ₱50,000-200,000 per client
- ROI: 6,000% - 25,000% (even with just 1 client)

## Project Structure

```
dpo-website/
├── public/
│   ├── admin/                          # Decap CMS
│   │   ├── config.yml                  # CMS configuration (collections, fields, workflow)
│   │   └── index.html                  # CMS entry point (loads from CDN)
│   ├── fonts/                          # Atkinson Hyperlegible (self-hosted)
│   ├── qr-*.svg                        # QR codes on print collateral → /start, /for/*, /card
│   ├── dedios.vcf                      # vCard served from /card
│   ├── og-default.png                  # Open Graph fallback image
│   ├── favicon.*, apple-touch-icon.png
│   ├── robots.txt
│   ├── tuv-certificate.pdf             # TÜV DPO Certificate #7000532
│   └── dpo-attendance-certificate.pdf  # Training certificate
│
├── src/
│   ├── components/
│   │   ├── BaseHead.astro              # SEO meta tags, Open Graph, fonts, GA4
│   │   ├── FaqLanding.astro            # Whole-page layout for the /for/* landing pages
│   │   ├── Footer.astro                # Site footer with copyright
│   │   ├── FormattedDate.astro         # Date formatting for blog posts
│   │   ├── Header.astro                # Navigation with mobile menu
│   │   └── HeaderLink.astro            # Nav link with active state
│   │
│   ├── content/
│   │   └── blog/                       # Blog posts (Markdown + frontmatter)
│   │       ├── what-is-data-protection-officer-philippines.md
│   │       ├── data-privacy-act-2012-compliance-guide.md
│   │       ├── common-data-privacy-violations-philippines.md
│   │       ├── npc-registration-guide-philippines.md
│   │       └── data-breach-response-plan-philippines.md
│   │
│   ├── layouts/
│   │   └── BlogPost.astro              # Blog post layout
│   │
│   ├── pages/
│   │   ├── index.astro                 # Homepage — TÜV badge, services, FAQ
│   │   ├── about.astro                 # Credentials, certifications, Person schema
│   │   ├── contact.astro               # EmailJS form with dual workflow
│   │   ├── card.astro                  # Digital calling card (QR target, serves the vCard)
│   │   ├── start.astro                 # Leaflet QR landing page — assessment CTA
│   │   ├── 404.astro
│   │   ├── rss.xml.js                  # RSS feed
│   │   ├── blog/
│   │   │   ├── index.astro             # Blog listing page
│   │   │   └── [...slug].astro         # Dynamic blog post routes
│   │   ├── for/                        # Industry landing pages (QR targets on print collateral)
│   │   │   ├── banks.astro
│   │   │   ├── hotels.astro
│   │   │   └── lending.astro
│   │   └── services/
│   │       ├── dpo-consulting.astro    # Primary service (6 offerings, FAQ, schema)
│   │       └── notarial.astro          # Complementary service (6 categories)
│   │
│   ├── styles/
│   │   └── global.css                  # Custom CSS variables, component classes
│   │
│   ├── content.config.ts               # Content collections schema
│   └── consts.ts                       # Site configuration (name, description)
│
├── astro.config.mjs                    # Astro config (integrations, site URL)
├── check-schema.mjs                    # Build gate: FAQ parity + BlogPosting completeness
├── tools/
│   └── validate-schema-vocab.py        # Manual: every JSON-LD property checked against schema.org
├── netlify.toml                        # Netlify build settings, redirects, headers
├── DEPLOYMENT.md                       # Complete deployment guide
├── README.md                           # Project overview and quick start
└── package.json                        # Dependencies and scripts
```

Tailwind v4 is configured in `src/styles/global.css` via `@tailwindcss/vite` —
there is no `tailwind.config.cjs`.

## Key Technical Decisions

### 1. Styling Approach: Vanilla CSS over Tailwind @apply

**Problem:** Tailwind CSS v4 has different @apply syntax that caused build failures.

**Error Examples:**
```
Cannot apply unknown utility class 'font-heading'
Cannot apply unknown utility class 'btn'
```

**Solution:** Converted all component classes to vanilla CSS with CSS custom properties.

**Before (failed):**
```css
.btn-primary {
  @apply btn bg-primary-600 text-white hover:bg-primary-700;
}
```

**After (working):**
```css
.btn-primary {
  display: inline-flex;
  align-items: center;
  background-color: var(--color-primary-600);
  color: white;
  min-height: 48px;
}
.btn-primary:hover {
  background-color: var(--color-primary-700);
}
```

**Impact:** More verbose CSS but guaranteed compatibility and no build errors.

### 2. Mobile-First Design with 48px Touch Targets

**Rationale:** Most Philippine users access via mobile devices. All interactive elements (buttons, links, form inputs) have minimum 48px height for accessibility.

**Implementation:**
```css
.btn, .btn-primary, .btn-secondary {
  min-height: 48px;
  padding: 0 24px;
}

input, select, textarea {
  min-height: 48px;
  padding: 12px 16px;
}
```

### 3. Dual Email Workflow for Contact Form

**Architecture:**
1. **User submits form** → EmailJS triggers two templates:
   - **Template 1:** Auto-reply to user (professional acknowledgment)
   - **Template 2:** Notification to attorney (lead details)

**Configuration Required:**
```javascript
// User auto-reply
emailjs.send('service_id', 'template_user_autoreply', {
  from_name: formData.name,
  from_email: formData.email,
  company_name: formData.company,
  service: formData.service,
  message: formData.message
});

// Attorney notification
emailjs.send('service_id', 'template_attorney_notification', {
  to_email: 'attorney@email.com',
  from_name: formData.name,
  from_email: formData.email,
  phone: formData.phone,
  company_name: formData.company,
  service: formData.service,
  location: formData.location,
  message: formData.message
});
```

**See DEPLOYMENT.md for complete EmailJS setup instructions.**

### 4. SEO Strategy: Schema Markup + Regional Keywords

**Schema.org Structured Data** — 9 JSON-LD blocks across 7 pages:

| Page | Blocks |
|---|---|
| Homepage | `Attorney` + `ProfessionalService`, `FAQPage` |
| About | `Person` + `Occupation` |
| DPO Consulting | `Service`, `FAQPage` |
| `/start`, `/for/banks`, `/for/hotels`, `/for/lending` | `FAQPage` (one each, via `FaqLanding`) |
| Each blog post | `BlogPosting` (via `BlogPost.astro`) |

`BlogPosting` is built in the layout, so every post gets one from its own
frontmatter. `dateModified` comes from `updatedDate` and falls back to
`pubDate` — three posts carry `updatedDate: 2026-08-02`, the day their legal
content was corrected, and two carry `2026-08-03` from the audit-of-the-audit
pass. That is what renders as the "Last updated on" line in the hero. Decap CMS exposes the field, so it can be maintained without
touching code. Keep it honest: bump it when the content actually changes.

**FAQ copy is generated, never hardcoded twice.** Every page with a `FAQPage`
block declares a `const faqs = [{ q, a }]` array and renders **both** the JSON-LD
and the visible `<details>` accordion from it. The `/for/*` pages and `/start`
pass theirs to `FaqLanding`; `index.astro` and `dpo-consulting.astro` do it
inline.

This is enforced, not conventional. `check-schema.mjs` runs as part of
`npm run build` — which is Netlify's build command — and **fails the deploy** if
any `FAQPage` answer is missing from the rendered body of its own page. The rule
exists because a correction was once applied to a homepage JSON-LD block and not
to the accordion beside it, so the published page contradicted its own
structured data and every grep for the corrected text reported it clean.

**FAQ rich results no longer exist.** Google restricted them to well-known,
authoritative government and health sites in August 2023, then retired the
feature entirely on **7 May 2026** — Search stopped showing them and Search
Console stopped reporting on FAQ structured data. In **June 2026** the FAQ
search appearance, the rich result report, and *FAQ support in the Rich Results
Test itself* were dropped; the Search Console API follows in August 2026. So the
Rich Results Test will not report on the seven `FAQPage` blocks at all — that is
the tool, not a defect in the markup. Google's own guidance is that unused
structured data causes no problems and need not be removed. The `FAQPage` markup is
still valid structured data and still describes the page to non-Google consumers,
so it stays — but do not expect an FAQ rich result in Search, and do not judge
the markup by whether one appears. The parity rule earns its keep for accuracy,
not for rich results: it is what stops the page from contradicting itself.

**Validating changes.** `tools/validate-schema-vocab.py` checks every JSON-LD
block on the live site (or a local `dist/`) against the real schema.org
vocabulary — are the types real, is each property allowed on the type it is
attached to — plus Google's Article recommendations. It is deliberately **not**
in `npm run build`: it downloads a 1.5 MB vocabulary, and a network hiccup must
never fail a deploy. Run it by hand after editing any JSON-LD block. It caught
`issuedBy` on an `EducationalOccupationalCredential`, which is valid only on
`Certification`/`Permit`/`Ticket` — the correct property on a credential is
`recognizedBy`. Neither the build gate nor a grep can see that class of error.

Google's Rich Results Test (https://search.google.com/test/rich-results) stays
the authority on whether a rich result is actually *shown*; the script only
checks the vocabulary is used correctly.

Answers may contain `<strong>`, `<em>` and `<a>` — Google permits that tag set
in FAQ answers, and emitting the identical string on both surfaces is what makes
the parity check exact. **Never hardcode the pair on a new page.**

**Target Keywords:**
- Primary: "Data Protection Officer Philippines", "DPO Region 8", "DPO Leyte"
- Secondary: "Data Privacy Act compliance", "RA 10173 consultant", "NPC registration"
- Long-tail: "TÜV Certified DPO Tacloban", "Privacy Management Program Eastern Visayas"

**Location Targeting:**
- Region 8 provinces: Leyte, Northern Samar, Eastern Samar, Western Samar, Biliran
- Major cities: Tacloban, Ormoc, Catbalogan, Calbayog, Maasin, Borongan

### 5. No Public Pricing Strategy

**Rationale:** Forces prospect engagement via contact form, enables custom pricing based on company size, industry, and scope.

**Implementation:**
- Service pages describe offerings but show "Contact for Pricing"
- Contact form includes "Service Interest" dropdown for qualification
- Free compliance assessment offered as lead magnet

## Content Strategy

### Blog Content Pillars

**5 Initial Posts (Completed):**

1. **"What is a Data Protection Officer..."** (2,000 words)
   - Target: Business owners unfamiliar with DPO role
   - Keywords: DPO, RA 10173, NPC
   - Goal: Educate and establish authority

2. **"Data Privacy Act of 2012: Essential Compliance Guide..."** (2,500 words)
   - Target: Businesses seeking compliance roadmap
   - Keywords: RA 10173 compliance, Region 8
   - Goal: Comprehensive resource with practical steps

3. **"7 Common Data Privacy Violations..."** (3,000 words)
   - Target: Businesses wanting to avoid NPC penalties
   - Keywords: Data privacy violations, NPC penalties
   - Goal: Practical how-to guide with fixes

4. **"How to Register Your Business with the NPC..."** (2,800 words)
   - Target: Businesses requiring NPC registration
   - Keywords: NPC registration, PIC registration
   - Goal: Step-by-step process guide

5. **"Data Breach Response Plan: The 72-Hour Rule..."** (3,200 words)
   - Target: Businesses preparing for breach scenarios
   - Keywords: Data breach, NPC reporting, 72-hour rule
   - Goal: Complete breach response framework

**Ongoing Content Strategy:**
- Publish 2-3 blog posts per week
- Mix of compliance guides, industry-specific tips, NPC updates
- Share on Facebook + LinkedIn with Region 8 business groups
- Build email list via contact form for newsletter

### Blog Post Structure Template

```markdown
---
title: 'Compelling Title with Keywords'
description: 'Meta description (155 characters max)'
pubDate: YYYY-MM-DD
category: 'Compliance Tips' | 'Data Privacy Law' | 'Industry Focus'
tags: ['RA 10173', 'NPC', 'Compliance', etc.]
---

## Introduction
- Hook with relatable scenario or pain point
- Preview what reader will learn

## Main Content
- H2 sections with clear headings
- Practical examples from Region 8
- Action items and checklists
- Real-world scenarios

## Bottom Line Summary
- Key takeaways
- Next steps

## Call to Action
- Link to contact form
- Free consultation offer
- Mention TÜV certification

---

*Closing statement positioning attorney as Region 8 expert*
```

## Deployment Workflow

### Local Development
```bash
npm install          # Install dependencies
npm run dev          # Start dev server (localhost:4321)
npm run build        # Build production site, then run the JSON-LD schema gate
npm run preview      # Preview production build
```

`npm run build` is `astro build && node check-schema.mjs`. A non-zero exit from
the gate is a real failure — either a page's FAQ JSON-LD no longer matches its
visible copy, or a blog post is missing a well-formed `BlogPosting` block. Fix
the page; do not bypass the check.

### Production Deployment (Automatic via Netlify)

**Trigger:** Push to GitHub main branch

**Process:**
1. Netlify detects push via webhook
2. Runs `npm run build`
3. Publishes `dist/` folder to CDN
4. Updates live site (2-5 minutes)

**Manual Deploy:**
- Netlify Dashboard → Deploys → Trigger deploy

### Content Publishing Workflow

**Via CMS (Recommended):**
1. Go to `https://yoursite.com/admin`
2. Log in with Netlify Identity
3. Click "Blog Posts" → "New Blog Post"
4. Write in rich text editor
5. Click "Publish"
6. Decap CMS commits to GitHub
7. Netlify auto-deploys (2-5 minutes)

**Via Code:**
1. Create `.md` file in `src/content/blog/`
2. Add frontmatter (title, description, pubDate, category, tags)
3. Write content in Markdown
4. `git add .`
5. `git commit -m "New blog post: [title]"`
6. `git push`
7. Netlify auto-deploys

## Configuration Required for Launch

### 1. EmailJS Setup (Required for Contact Form)

**Steps:**
1. Create free account at [emailjs.com](https://emailjs.com)
2. Add email service (Gmail recommended)
3. Create two templates:
   - **User Auto-Reply Template**
   - **Attorney Notification Template**
4. Get Public Key, Service ID, Template IDs
5. Update `src/pages/contact.astro`:
   ```javascript
   emailjs.init("YOUR_PUBLIC_KEY");
   emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', formData);
   ```

**See DEPLOYMENT.md Section "Step 4: Set Up EmailJS" for complete instructions.**

### 2. Netlify Identity (Required for CMS)

**Steps:**
1. Netlify Dashboard → Site settings → Identity
2. Click "Enable Identity"
3. Registration: Select "Invite only"
4. Enable Git Gateway
5. Invite yourself via email
6. Accept invitation and create password

**See DEPLOYMENT.md Section "Step 3: Set Up Decap CMS" for complete instructions.**

### 3. Custom Domain — DONE

Live at **https://dpo.dedioslaw.ph**. `astro.config.mjs` (`site:`) and the
`netlify.toml` www→apex redirect both point at it. The `dporegion8.com` name
this file used to recommend was never purchased.

### 4. Google Analytics — DONE

GA4 is live in `src/components/BaseHead.astro` (`GA_MEASUREMENT_ID`).

## Security Measures

### Netlify Security Headers (netlify.toml)
- **X-Frame-Options:** DENY (prevents clickjacking)
- **X-Content-Type-Options:** nosniff (prevents MIME sniffing)
- **X-XSS-Protection:** 1; mode=block (blocks XSS attacks)
- **Referrer-Policy:** strict-origin-when-cross-origin
- **Permissions-Policy:** Restricts geolocation, microphone, camera

### HTTPS by Default
- Automatic SSL certificate provisioning via Let's Encrypt
- HTTPS redirect enabled in netlify.toml

### Static Site = No Database Vulnerabilities
- No SQL injection possible (no database)
- No server-side code execution
- Minimal attack surface

## Performance Optimizations

### Static Site Generation
- All pages pre-rendered at build time
- Zero client-side JavaScript (except EmailJS on contact page)
- Fast Time to First Byte (TTFB)

### Asset Optimization (netlify.toml)
- CSS/JS minification and bundling
- Image compression
- Cache headers:
  - Static assets: 1 year cache
  - HTML: No cache (immediate updates)

### CDN Distribution
- Netlify Edge Network serves content globally
- Philippine users served from Singapore edge node
- Sub-second page loads expected

## Brand Guidelines

### Color Palette
```css
Primary (Deep Blue): #1e3a8a  /* Trust, security, legal */
Primary Light: #3b82f6
Primary Dark: #1e40af

Accent (Gold): #f59e0b        /* TÜV certification color */
Accent Light: #fbbf24
Accent Dark: #d97706

Neutrals:
- Text: #1f2937 (neutral-800)
- Text Secondary: #6b7280 (neutral-600)
- Borders: #e5e7eb (neutral-200)
- Backgrounds: #f9fafb (neutral-50)
```

### Typography
- **Headings:** Poppins (600 weight for H1-H3)
- **Body:** Inter (400 regular, 600 semibold)
- **Size Scale:** 16px base, 1.25 scale ratio

### Voice & Tone
- **Professional** but approachable
- **Authoritative** without being intimidating
- **Educational** and helpful
- **Regional pride** (emphasize Region 8 focus)
- **Credential-forward** (mention TÜV certification)

## Common Maintenance Tasks

### Weekly
- Check contact form submissions (Netlify Forms dashboard)
- Respond to inquiries within 24 hours
- Publish 2-3 new blog posts

### Monthly
- Review Google Analytics for traffic trends
- Check for broken links
- Update service pages if offerings change
- Review and update blog content for SEO

### Annually
- Renew domain registration
- Update TÜV certificate expiration date (valid until 2029)
- Review and update pricing strategy
- Audit SEO performance and adjust keywords

## Troubleshooting

### Build Fails
**Check:** Netlify deploy log for errors
**Common causes:**
- Syntax errors in .astro files
- Missing frontmatter in blog posts
- Invalid YAML in config files
- **Schema gate failed** — `check-schema.mjs` names the page and the problem.
  For an FAQ mismatch, make that page render both surfaces from its `faqs`
  array. For a `BlogPosting` complaint, check the post's frontmatter. Do not
  remove the gate.

**Solution:** Test locally with `npm run build`

### CMS Not Loading
**Check:** Netlify Identity enabled and Git Gateway enabled
**Solution:**
1. Site settings → Identity → Enable Identity
2. Site settings → Identity → Services → Enable Git Gateway
3. Clear browser cache

### Contact Form Not Sending
**Check:** EmailJS dashboard for errors
**Common causes:**
- Incorrect Service ID or Template ID
- Free tier limit exceeded (200/month)
- Invalid email template variables

**Solution:** Verify credentials in contact.astro match EmailJS dashboard

### Blog Posts Not Appearing
**Check:** Frontmatter format in .md files
**Required fields:**
```yaml
---
title: 'String'
description: 'String'
pubDate: YYYY-MM-DD
category: 'String'
tags: ['Array', 'of', 'strings']
---
```

## Next Steps for Client

### Immediate (Before Launch)
1. ✅ Purchase domain name (₱600-800)
2. ✅ Create GitHub account and push code
3. ✅ Create Netlify account and deploy
4. ✅ Configure EmailJS for contact form
5. ✅ Set up Netlify Identity for CMS
6. ✅ Test contact form and CMS

### Week 1-2 (Launch Phase)
1. Set up Google Business Profile
2. Submit site to Google Search Console
3. Create social media profiles (Facebook, LinkedIn)
4. Share initial blog posts on social media
5. Join Region 8 business communities online
6. Set up email signature with website link

### Month 1-3 (Growth Phase)
1. Publish 2-3 blog posts per week
2. Engage with comments and inquiries
3. Monitor analytics and adjust strategy
4. Build local business directory citations
5. Consider Facebook Ads targeting Region 8
6. Network with accounting firms, law firms for referrals

### Month 4+ (Scale Phase)
1. Launch webinars on data privacy compliance
2. Create industry-specific compliance packages
3. Speaking engagements at business conferences
4. Partnerships with complementary service providers
5. Consider hiring support staff if lead volume justifies
6. Expand content to video (YouTube/Facebook)

## Project Completion Status

### ✅ Completed
- [x] Astro project initialization with blog template
- [x] Tailwind CSS configuration with branding colors
- [x] Decap CMS setup for easy blog management
- [x] Homepage with TÜV certification showcase
- [x] DPO Consulting service page (SEO optimized)
- [x] About page with credentials and certifications
- [x] Contact form with EmailJS automation
- [x] Notarial Services page
- [x] 5 initial blog posts (13,500+ words total)
- [x] Netlify deployment configuration (netlify.toml)
- [x] Complete deployment documentation (DEPLOYMENT.md)
- [x] Project README with quick start guide
- [x] Deployed and live at dpo.dedioslaw.ph (GA4 active)
- [x] Conversion pages: `/start`, `/card`, and the three `/for/*` industry
      landing pages, all QR targets on print collateral
- [x] Legal-accuracy audit of every page and post against RA 10173, its IRR
      and the NPC circulars (2026-08-02, see `../AUDIT-REPORT-2026-08-02.md`)
- [x] FAQ copy generated from one array per page, `BlogPosting` schema on every
      post, both enforced by the `check-schema.mjs` build gate

### ⏭️ Open
- [ ] Real client testimonials — the homepage cards are currently unattributed
- [ ] Google Business Profile

## Support Resources

**Official Documentation:**
- Astro: https://docs.astro.build
- Decap CMS: https://decapcms.org/docs
- Netlify: https://docs.netlify.com
- EmailJS: https://emailjs.com/docs
- Tailwind CSS: https://tailwindcss.com/docs

**Community Support:**
- Astro Discord: https://astro.build/chat
- Netlify Community: https://answers.netlify.com
- Stack Overflow: Tag questions with [astro] [netlify] [decap-cms]

**Philippine-Specific Resources:**
- National Privacy Commission: https://privacy.gov.ph
- NPC Circulars and Advisories: https://privacy.gov.ph/advisories/
- Data Privacy Act of 2012 (RA 10173): https://privacy.gov.ph/data-privacy-act/

---

**Project Build Date:** March 2026
**Last Updated:** August 3, 2026
**Built by:** Claude (Anthropic)
**Built for:** Atty. Renerio de Dios Jr. - TÜV Certified DPO, Region 8, Philippines
