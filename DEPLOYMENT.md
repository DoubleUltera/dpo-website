# DPO Website Deployment Guide

This guide will walk you through deploying your DPO consulting website to Netlify for **FREE**. The entire process takes about 15-30 minutes.

## Prerequisites

Before you begin, you'll need:
- A GitHub account (free - sign up at [github.com](https://github.com))
- A Netlify account (free - sign up at [netlify.com](https://netlify.com))
- Your website files (already in this directory)

## Step-by-Step Deployment

### Step 1: Create a GitHub Repository

GitHub will store your website code and enable automatic deployments when you make changes.

1. **Sign in to GitHub** at [github.com](https://github.com)

2. **Create a new repository:**
   - Click the **"+"** button in the top right
   - Select **"New repository"**
   - Repository name: `dpo-website` (or your preferred name)
   - Description: "DPO Consulting Website for Region 8"
   - Choose **Public** (required for free Netlify hosting)
   - **Do NOT** initialize with README (we already have files)
   - Click **"Create repository"**

3. **Push your code to GitHub:**

   Open your terminal in this directory and run these commands:

   ```bash
   # Initialize git repository (if not already done)
   git init

   # Add all files
   git add .

   # Create your first commit
   git commit -m "Initial commit: DPO website for Region 8"

   # Add your GitHub repository as remote
   # Replace YOUR-USERNAME with your GitHub username
   git remote add origin https://github.com/YOUR-USERNAME/dpo-website.git

   # Push to GitHub
   git branch -M main
   git push -u origin main
   ```

   **Your code is now on GitHub!**

### Step 2: Deploy to Netlify

Netlify will automatically build and host your website for free.

1. **Sign in to Netlify** at [netlify.com](https://netlify.com)
   - You can sign in with your GitHub account for easier integration

2. **Create a new site:**
   - Click **"Add new site"** → **"Import an existing project"**

3. **Connect to GitHub:**
   - Click **"GitHub"**
   - Authorize Netlify to access your GitHub account
   - Search for and select your `dpo-website` repository

4. **Configure build settings:**
   - **Branch to deploy:** `main`
   - **Build command:** `npm run build` (should be pre-filled)
   - **Publish directory:** `dist` (should be pre-filled)
   - Click **"Deploy site"**

5. **Wait for deployment:**
   - Netlify will install dependencies and build your site (2-5 minutes)
   - You'll see a random subdomain like `random-name-123456.netlify.app`
   - Once deployment is complete, click the URL to view your site!

**🎉 Your website is now live!**

### Step 3: Set Up Decap CMS (Blog Management)

Enable Netlify Identity so you can log in to your CMS at `/admin`.

1. **Enable Netlify Identity:**
   - In your Netlify dashboard, go to **Site settings** → **Identity**
   - Click **"Enable Identity"**

2. **Configure registration:**
   - Under **Identity** → **Registration**, select **"Invite only"**
   - This prevents random people from accessing your CMS

3. **Enable Git Gateway:**
   - Under **Identity** → **Services**, click **"Enable Git Gateway"**
   - This allows the CMS to save changes to GitHub

4. **Invite yourself:**
   - Go to **Identity** tab
   - Click **"Invite users"**
   - Enter your email address
   - Check your email and accept the invitation
   - Create a password

5. **Test the CMS:**
   - Go to `https://your-site-name.netlify.app/admin`
   - Log in with your email and password
   - You should see the Decap CMS dashboard!

**✅ You can now manage your blog from `/admin` without touching code!**

### Step 4: Set Up EmailJS (Contact Form)

Configure automated email responses for your contact form.

1. **Create an EmailJS account:**
   - Go to [emailjs.com](https://emailjs.com)
   - Sign up for a **FREE** account (200 emails/month)

2. **Add an email service:**
   - Go to **Email Services** → **Add New Service**
   - Choose your email provider (Gmail recommended)
   - Connect your email account
   - Note your **Service ID** (e.g., `service_abc123`)

3. **Create email templates:**

   **Template 1: User Auto-Reply**
   - Go to **Email Templates** → **Create New Template**
   - Template Name: `User Auto-Reply`
   - Subject: `We received your inquiry - {{company_name}}`
   - Content:
     ```
     Dear {{from_name}},

     Thank you for contacting us regarding {{service}} services.

     We have received your inquiry and will review it shortly. You can expect a response within 1-2 business days.

     Your message:
     {{message}}

     Best regards,
     Atty. Renerio de Dios Jr.
     TÜV Certified Data Protection Officer
     Tacloban City, Leyte

     Phone: [Your Phone]
     Email: [Your Email]
     ```
   - Note your **Template ID** (e.g., `template_xyz789`)

   **Template 2: Attorney Notification**
   - Create another template
   - Template Name: `New Client Inquiry Notification`
   - To Email: `{{to_email}}` (you'll set this to your email)
   - Subject: `New DPO Inquiry from {{from_name}}`
   - Content:
     ```
     New inquiry received via website contact form:

     Name: {{from_name}}
     Company: {{company_name}}
     Email: {{from_email}}
     Phone: {{phone}}
     Service Interest: {{service}}
     Location: {{location}}

     Message:
     {{message}}

     ---
     Received: {{current_date}}
     ```
   - Note your **Template ID** for this one too

4. **Get your Public Key:**
   - Go to **Account** → **General**
   - Copy your **Public Key** (e.g., `abc123XYZ456`)

5. **Update the contact form:**
   - Open `src/pages/contact.astro` in a text editor
   - Find these lines:
     ```javascript
     emailjs.init("YOUR_PUBLIC_KEY"); // Replace with your Public Key
     ```
   - Replace with your actual keys:
     ```javascript
     emailjs.init("abc123XYZ456"); // Your Public Key from step 4
     ```
   - Find:
     ```javascript
     emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', formData)
     ```
   - Replace with:
     ```javascript
     emailjs.send('service_abc123', 'template_xyz789', formData)
     ```
   - Do the same for the attorney notification email

6. **Push changes to GitHub:**
   ```bash
   git add src/pages/contact.astro
   git commit -m "Configure EmailJS for contact form"
   git push
   ```

   Netlify will automatically rebuild and deploy your site with working email!

### Step 5: Add a Custom Domain (Optional)

Replace the `random-name-123456.netlify.app` URL with your own domain.

1. **Purchase a domain:**
   - Recommended registrars for Philippines:
     - [Namecheap](https://www.namecheap.com) - ~₱600/year
     - [GoDaddy](https://www.godaddy.com) - ~₱700/year
     - [Google Domains](https://domains.google) - ~₱800/year
   - Suggested domain: `dporegion8.com` or similar

2. **Add domain to Netlify:**
   - In Netlify dashboard, go to **Domain settings**
   - Click **"Add custom domain"**
   - Enter your domain (e.g., `dporegion8.com`)
   - Follow the instructions to update your domain's DNS settings

3. **Enable HTTPS:**
   - After DNS propagates (can take up to 24 hours)
   - Netlify will automatically provision a free SSL certificate
   - Your site will be accessible via `https://dporegion8.com`

4. **Update configuration:**
   - Edit `netlify.toml` and update the domain redirect:
     ```toml
     from = "https://www.dporegion8.com/*"
     to = "https://dporegion8.com/:splat"
     ```

### Step 6: Configure Google Analytics (Optional)

Track website visitors and performance.

1. **Create a Google Analytics 4 property:**
   - Go to [analytics.google.com](https://analytics.google.com)
   - Create an account and property
   - Get your **Measurement ID** (format: `G-XXXXXXXXXX`)

2. **Add to your website:**
   - Open `src/components/BaseHead.astro`
   - Add this code before the closing `</head>` tag:
     ```html
     <!-- Google Analytics -->
     <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
     <script>
       window.dataLayer = window.dataLayer || [];
       function gtag(){dataLayer.push(arguments);}
       gtag('js', new Date());
       gtag('config', 'G-XXXXXXXXXX');
     </script>
     ```

3. **Push changes:**
   ```bash
   git add src/components/BaseHead.astro
   git commit -m "Add Google Analytics tracking"
   git push
   ```

## Automatic Deployments

Now that everything is set up, every time you:
1. Update blog content via `/admin` CMS, or
2. Push code changes to GitHub

Netlify will **automatically rebuild and deploy** your site within 2-5 minutes!

## Managing Your Website

### How to Publish a New Blog Post

1. Go to `https://your-site-name.netlify.app/admin`
2. Log in with your email and password
3. Click **"Blog Posts"** → **"New Blog Post"**
4. Write your post using the rich text editor
5. Click **"Publish"**
6. Your post goes live automatically!

### How to Update Pages

If you need to update service pages, contact information, or other content:

1. Edit the `.astro` files in the `src/pages/` directory
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update [page name]"
   git push
   ```
3. Netlify automatically deploys the changes

### How to Monitor Website Performance

**Netlify Analytics (Optional - ₱500/month):**
- Real-time visitor stats
- No cookies or GDPR notices required
- Philippine traffic breakdown

**Google Analytics (FREE):**
- Detailed visitor behavior
- Traffic sources
- Most popular pages
- Requires cookie consent notice

**Microsoft Clarity (FREE):**
- Heatmaps and session recordings
- See how users interact with your site
- No monthly limits
- Sign up at [clarity.microsoft.com](https://clarity.microsoft.com)

## Troubleshooting

### Build Failed

**Error:** `Command failed with exit code 1`

**Solution:**
1. Check the build log in Netlify
2. Common issues:
   - Missing dependencies: Run `npm install` locally
   - Syntax errors: Check the error message for file/line number
   - Environment variables: Set in Netlify **Site settings** → **Environment variables**

### CMS Not Loading

**Error:** Can't access `/admin` or login fails

**Solution:**
1. Make sure Netlify Identity is enabled
2. Make sure Git Gateway is enabled
3. Clear browser cache and try again
4. Check `public/admin/config.yml` is properly configured

### Contact Form Not Sending

**Error:** Form submits but no email received

**Solution:**
1. Check EmailJS dashboard for errors
2. Verify Service ID and Template IDs are correct
3. Check spam folder
4. Verify EmailJS free tier limit not exceeded (200/month)

### Site Not Updating After Changes

**Solution:**
1. Check Netlify **Deploys** tab for build status
2. Click **"Trigger deploy"** → **"Clear cache and deploy"**
3. For CMS changes, make sure changes were committed to GitHub

## Cost Breakdown

### Year 1 (Minimal)
- ✅ **Domain:** ₱600-800/year (`.com` domain)
- ✅ **Hosting (Netlify):** FREE (100GB bandwidth/month)
- ✅ **CMS (Decap):** FREE (unlimited)
- ✅ **Email automation (EmailJS):** FREE (200 emails/month)
- ✅ **SSL Certificate:** FREE (auto-provisioned by Netlify)
- ✅ **Analytics:** FREE (Google Analytics + Microsoft Clarity)

**Total Year 1: ₱600-800**

### Optional Upgrades (If Business Grows)
- Professional email (`you@dporegion8.com`): FREE via Zoho or ₱1,200/year
- Netlify Pro (if >100GB bandwidth): ₱1,000/month
- EmailJS Pro (if >200 forms/month): ₱500/month

## Support Resources

**Netlify Documentation:**
- [Netlify Docs](https://docs.netlify.com)
- [Netlify Support Community](https://answers.netlify.com)

**Decap CMS Documentation:**
- [Decap CMS Docs](https://decapcms.org/docs)

**Astro Documentation:**
- [Astro Docs](https://docs.astro.build)

**EmailJS Documentation:**
- [EmailJS Docs](https://www.emailjs.com/docs)

## Next Steps

Now that your website is live:

1. **Test everything:**
   - Contact form submission
   - Blog post publishing via CMS
   - Mobile responsiveness
   - Page loading speed

2. **Content creation:**
   - Publish regular blog posts (2-3 per week recommended)
   - Share posts on social media

3. **SEO optimization:**
   - Submit sitemap to Google Search Console: `https://your-site.com/sitemap-index.xml`
   - Create Google Business Profile
   - Get listed in local directories

4. **Marketing:**
   - Share blog posts on Facebook, LinkedIn
   - Engage with Region 8 business communities
   - Leverage your TÜV certification in all marketing

**🎉 Congratulations! Your DPO consulting website is now live and ready to attract clients!**

---

*For technical support or questions, refer to the documentation links above or reach out to the development team.*
