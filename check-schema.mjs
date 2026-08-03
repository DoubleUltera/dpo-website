// Build gate for the JSON-LD in dist/. Two rules:
//
//   1. FAQ parity — every answer in a page's FAQPage block must also appear in
//      that page's visible HTML. A page that hardcodes the same copy on both
//      surfaces can be corrected on one and left wrong on the other, and greps
//      for the corrected text then report it clean. That happened to
//      index.astro.
//   2. Blog posts must carry a well-formed BlogPosting block. They went months
//      without one because nothing checked.
import { readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const pages = [];
(function walk(dir) {
	for (const e of readdirSync(dir, { withFileTypes: true })) {
		const p = join(dir, e.name);
		if (e.isDirectory()) walk(p);
		else if (e.name.endsWith('.html')) pages.push(p);
	}
})('dist');

const BLOGPOSTING_REQUIRED = ['headline', 'description', 'datePublished', 'dateModified', 'author', 'publisher', 'image', 'mainEntityOfPage'];

const problems = [];
for (const page of pages) {
	const html = readFileSync(page, 'utf8');
	// Search the body with every <script> stripped — otherwise each JSON-LD
	// answer matches itself and the check passes no matter what.
	const body = html.replace(/<script[^>]*>.*?<\/script>/gs, '');
	const blocks = [...html.matchAll(/<script type="application\/ld\+json"[^>]*>(.*?)<\/script>/gs)].map(([, b]) => JSON.parse(b));

	for (const block of blocks.filter((b) => b['@type'] === 'FAQPage')) {
		for (const q of block.mainEntity) {
			// ponytail: substring match, not DOM parsing. Enough because both
			// surfaces render the same source string verbatim.
			if (!body.includes(q.acceptedAnswer.text)) problems.push(`${page}: "${q.name}" — JSON-LD answer is not in the visible copy`);
		}
	}

	// Every rendered post, but not the /blog listing index.
	if (/^dist\/blog\/.+\/index\.html$/.test(page)) {
		const post = blocks.find((b) => b['@type'] === 'BlogPosting');
		if (!post) problems.push(`${page}: no BlogPosting schema`);
		else {
			const missing = BLOGPOSTING_REQUIRED.filter((k) => !post[k]);
			if (missing.length) problems.push(`${page}: BlogPosting missing ${missing.join(', ')}`);
			if (post.dateModified < post.datePublished) problems.push(`${page}: BlogPosting dateModified precedes datePublished`);
		}
	}
}

if (problems.length) {
	console.error(`Schema check: ${problems.length} problem(s)\n` + problems.join('\n'));
	process.exit(1);
}
console.log(`Schema check: OK across ${pages.length} pages`);
