// Every answer in a page's FAQPage JSON-LD must also appear in that page's
// visible HTML. A page that hardcodes the same copy on both surfaces can be
// corrected on one and left wrong on the other — greps for the corrected text
// then report it clean. That happened to index.astro; this fails the build.
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

const problems = [];
for (const page of pages) {
	const html = readFileSync(page, 'utf8');
	// Search the body with every <script> stripped — otherwise each JSON-LD
	// answer matches itself and the check passes no matter what.
	const body = html.replace(/<script[^>]*>.*?<\/script>/gs, '');
	for (const [, block] of html.matchAll(/<script type="application\/ld\+json"[^>]*>(.*?)<\/script>/gs)) {
		if (!block.includes('"FAQPage"')) continue;
		for (const q of JSON.parse(block).mainEntity) {
			const answer = q.acceptedAnswer.text;
			// ponytail: substring match, not DOM parsing. Enough because both
			// surfaces render the same source string verbatim.
			if (!body.includes(answer)) problems.push(`${page}: "${q.name}" — JSON-LD answer is not in the visible copy`);
		}
	}
}

if (problems.length) {
	console.error(`FAQ parity: ${problems.length} mismatch(es)\n` + problems.join('\n'));
	process.exit(1);
}
console.log(`FAQ parity: OK across ${pages.length} pages`);
