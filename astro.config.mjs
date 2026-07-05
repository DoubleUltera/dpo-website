// @ts-check

import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://dpo.dedioslaw.ph',
  integrations: [mdx(), sitemap()],

  // Inline component/global CSS into each page to remove the render-blocking
  // stylesheet request (improves FCP/LCP on this small brochure site).
  build: { inlineStylesheets: 'always' },

  vite: {
    plugins: [tailwindcss()],
  },
});