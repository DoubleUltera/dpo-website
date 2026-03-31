# DPO Consulting Website - Region 8, Philippines

Professional website for Atty. Renerio de Dios Jr., TÜV Certified Data Protection Officer serving Eastern Visayas (Region 8), Philippines.

## 🎯 Project Overview

This website is designed to establish market dominance for DPO consulting services across Region 8 (Leyte, Samar, and Biliran) while also offering complementary notarial services.

**Key Features:**
- ⚡ Lightning-fast static site (95+ PageSpeed score)
- 📝 Easy blog management via CMS (no coding required)
- 📧 Automated contact form with email responses
- 🔒 Security-focused design and SEO optimization
- 📱 Mobile-first responsive design
- 🆓 **Total cost: ₱600-800/year** (domain only - everything else free!)

## 🚀 Technology Stack

- **[Astro 4.x](https://astro.build)** - Modern static site generator
- **[Decap CMS](https://decapcms.org)** - Git-based content management
- **[Netlify](https://netlify.com)** - Free hosting + CDN + forms
- **[EmailJS](https://emailjs.com)** - Contact form automation
- **[Tailwind CSS v4](https://tailwindcss.com)** - Styling framework

## 📁 Project Structure

```
dpo-website/
├── public/                      # Static assets
│   ├── admin/                   # Decap CMS configuration
│   │   ├── config.yml           # CMS settings
│   │   └── index.html           # CMS entry point
│   ├── tuv-certificate.pdf      # TÜV DPO certification
│   └── dpo-attendance-certificate.pdf
│
├── src/
│   ├── components/              # Reusable UI components
│   │   ├── BaseHead.astro       # SEO meta tags
│   │   ├── Footer.astro         # Site footer
│   │   └── Header.astro         # Navigation header
│   │
│   ├── content/
│   │   └── blog/                # Blog posts (Markdown)
│   │       ├── what-is-data-protection-officer-philippines.md
│   │       ├── data-privacy-act-2012-compliance-guide.md
│   │       ├── common-data-privacy-violations-philippines.md
│   │       ├── npc-registration-guide-philippines.md
│   │       └── data-breach-response-plan-philippines.md
│   │
│   ├── layouts/
│   │   └── BlogPost.astro       # Blog post template
│   │
│   ├── pages/                   # Website pages
│   │   ├── index.astro          # Homepage
│   │   ├── about.astro          # About page
│   │   ├── contact.astro        # Contact form
│   │   ├── blog/                # Blog listing and posts
│   │   └── services/            # Service pages
│   │       ├── dpo-consulting.astro
│   │       └── notarial.astro
│   │
│   ├── styles/
│   │   └── global.css           # Global styles and theme
│   │
│   └── consts.ts                # Site configuration
│
├── astro.config.mjs             # Astro configuration
├── tailwind.config.cjs          # Tailwind configuration
├── netlify.toml                 # Netlify deployment settings
├── DEPLOYMENT.md                # Deployment instructions
└── package.json                 # Dependencies
```

## 🛠️ Local Development

### Prerequisites

- Node.js 20.x or higher
- npm (comes with Node.js)

### Installation

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm run dev
   ```

3. **Open your browser:**
   - Website: http://localhost:4321
   - CMS (requires Netlify deployment): http://localhost:4321/admin

### Development Commands

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server at `localhost:4321` |
| `npm run build` | Build production site to `dist/` folder |
| `npm run preview` | Preview production build locally |
| `npm run astro ...` | Run Astro CLI commands |

## 📝 Managing Content

### Adding Blog Posts

**Option 1: Via CMS (Recommended - No coding required)**
1. Deploy to Netlify (see [DEPLOYMENT.md](DEPLOYMENT.md))
2. Go to `https://your-site.com/admin`
3. Log in with Netlify Identity
4. Click **"Blog Posts"** → **"New Blog Post"**
5. Write and publish!

**Option 2: Via Code**
1. Create a new `.md` file in `src/content/blog/`
2. Add frontmatter and write your content in Markdown
3. Commit and push to GitHub

### Updating Pages

Edit the `.astro` files in `src/pages/` directory and push to GitHub for automatic deployment.

## 🚀 Deployment

See the comprehensive [DEPLOYMENT.md](DEPLOYMENT.md) guide for step-by-step instructions.

**Quick Summary:**
1. Push code to GitHub
2. Connect GitHub repo to Netlify
3. Enable Netlify Identity for CMS
4. Configure EmailJS for contact form
5. (Optional) Add custom domain

## 📧 Contact Form Setup

Configure EmailJS for automated email responses. See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

## 🎨 Branding & Design

**Color Scheme:**
- **Primary (Deep Blue):** `#1e3a8a` - Trust, security, professionalism
- **Accent (Gold):** `#f59e0b` - TÜV certification accent
- **Neutrals:** Grays for text and backgrounds

**Typography:**
- **Headings:** Poppins (bold, professional)
- **Body:** Inter (clean, readable)

## 💰 Cost Breakdown

| Service | Cost | Notes |
|---------|------|-------|
| Domain (.com) | ₱600-800/year | Required |
| Netlify Hosting | FREE | 100GB bandwidth/month |
| Decap CMS | FREE | Unlimited posts |
| EmailJS | FREE | 200 emails/month |
| SSL Certificate | FREE | Auto-provisioned |

**Total: ₱600-800/year**

## 📈 Growth Strategy

**Phase 1: Launch**
- Deploy website
- Publish initial blog posts
- Set up Google Business Profile

**Phase 2: Content Marketing**
- Publish 2-3 blog posts per week
- Share on social media
- Build email list

**Phase 3: Paid Marketing**
- Facebook Ads targeting Region 8
- Google Ads for high-intent keywords

## 🤝 Support

**Technical Documentation:**
- Netlify: [docs.netlify.com](https://docs.netlify.com)
- Astro: [docs.astro.build](https://docs.astro.build)
- Decap CMS: [decapcms.org/docs](https://decapcms.org/docs)
- EmailJS: [emailjs.com/docs](https://emailjs.com/docs)

---

**Built for Region 8 businesses seeking data privacy compliance**

*For deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)*
