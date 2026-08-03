#!/usr/bin/env python3
"""Check every JSON-LD block on the live site against the real schema.org
vocabulary: are the types real, and is each property actually allowed on the
type it is attached to?

    python3 tools/validate-schema-vocab.py            # live site
    python3 tools/validate-schema-vocab.py dist       # local build

This is NOT part of `npm run build` — it downloads a 1.5 MB vocabulary, and a
network hiccup must never fail a deploy. Run it by hand after editing any
JSON-LD block. It found `issuedBy` on an EducationalOccupationalCredential,
which is valid only on Certification/Permit/Ticket; `check-schema.mjs` cannot
see that class of error and neither can a grep.

Google's Rich Results Test (https://search.google.com/test/rich-results) is
still the authority on whether a rich result will actually be *shown* — this
only checks the vocabulary is used correctly.
"""
import glob
import json
import os
import re
import sys
import urllib.request

VOCAB_URL = 'https://schema.org/version/latest/schemaorg-current-https.jsonld'
CACHE = os.path.join(os.path.dirname(__file__), '.schemaorg-cache.jsonld')

PAGES = [
	'', 'about/', 'services/dpo-consulting/', 'services/notarial/', 'contact/',
	'start/', 'card/', 'for/banks/', 'for/hotels/', 'for/lending/',
	'blog/', 'blog/npc-registration-guide-philippines/',
	'blog/what-is-data-protection-officer-philippines/',
	'blog/data-privacy-act-2012-compliance-guide/',
	'blog/common-data-privacy-violations-philippines/',
	'blog/data-breach-response-plan-philippines/',
]
SITE = 'https://dpo.dedioslaw.ph/'

# Google recommends these for Article/BlogPosting. None are strictly required.
ARTICLE_RECOMMENDED = ('author', 'datePublished', 'dateModified', 'headline', 'image')
ISO_8601 = re.compile(r'^\d{4}-\d{2}-\d{2}(T[\d:.]+(Z|[+-]\d{2}:?\d{2}))?$')


def load_vocabulary():
	if not os.path.exists(CACHE):
		print(f'downloading {VOCAB_URL} …', file=sys.stderr)
		urllib.request.urlretrieve(VOCAB_URL, CACHE)
	# The published file uses CURIEs ("schema:Person") and bundles several
	# foreign vocabularies; keep only schema.org's own terms.
	graph = [n for n in json.load(open(CACHE))['@graph'] if n['@id'].startswith('schema:')]

	supertypes, domains = {}, {}
	for n in graph:
		name = n['@id'].removeprefix('schema:')
		if n.get('@type') == 'rdfs:Class':
			parents = n.get('rdfs:subClassOf', [])
			supertypes[name] = [p['@id'].removeprefix('schema:') for p in (parents if isinstance(parents, list) else [parents])]
		elif n.get('@type') == 'rdf:Property':
			d = n.get('schema:domainIncludes', [])
			domains[name] = {x['@id'].removeprefix('schema:') for x in (d if isinstance(d, list) else [d])}
	return supertypes, domains


SUPERTYPES, DOMAINS = load_vocabulary()


def ancestors(t, seen=None):
	seen = seen if seen is not None else set()
	if t in seen or t not in SUPERTYPES:
		return seen
	seen.add(t)
	for parent in SUPERTYPES[t]:
		ancestors(parent, seen)
	return seen


def check_node(node, path, problems):
	declared = node.get('@type')
	declared = declared if isinstance(declared, list) else [declared]
	valid_on = set()
	for t in declared:
		if t not in SUPERTYPES:
			problems.append(f'{path}: unknown type "{t}"')
		valid_on |= ancestors(t)

	for key, value in node.items():
		if key.startswith('@'):
			continue
		if key not in DOMAINS:
			problems.append(f'{path}: unknown property "{key}"')
			continue
		if not (DOMAINS[key] & valid_on):
			problems.append(f'{path}: "{key}" is not valid on {"+".join(declared)} — only on {", ".join(sorted(DOMAINS[key]))}')
		for child in (value if isinstance(value, list) else [value]):
			if isinstance(child, dict) and '@type' in child:
				check_node(child, f'{path}.{key}', problems)


def check_article(node, problems):
	for field in ARTICLE_RECOMMENDED:
		if not node.get(field):
			problems.append(f'Google recommends "{field}" for Article — missing')
	for field in ('datePublished', 'dateModified'):
		if node.get(field) and not ISO_8601.match(node[field]):
			problems.append(f'{field} is not ISO 8601: {node[field]}')
	if node.get('dateModified', '') < node.get('datePublished', ''):
		problems.append('dateModified precedes datePublished')
	if len(node.get('headline', '')) > 110:
		problems.append(f'headline is {len(node["headline"])} chars — long titles get truncated')


def sources():
	if len(sys.argv) > 1:
		root = sys.argv[1]
		return [(p, open(p, encoding='utf-8').read()) for p in sorted(glob.glob(f'{root}/**/*.html', recursive=True))]
	out = []
	for page in PAGES:
		url = SITE + page
		req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		out.append((url, urllib.request.urlopen(req).read().decode()))
	return out


total = bad = 0
for name, html in sources():
	blocks = re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', html, re.S)
	if not blocks:
		continue
	print(f'\n{name}  ({len(blocks)} block(s))')
	for raw in blocks:
		total += 1
		try:
			node = json.loads(raw)
		except json.JSONDecodeError as e:
			print(f'  x INVALID JSON: {e}')
			bad += 1
			continue
		label = node.get('@type')
		label = label if isinstance(label, str) else '+'.join(label)
		problems = []
		check_node(node, label, problems)
		if isinstance(node.get('@type'), str) and 'Article' in ancestors(node['@type']):
			check_article(node, problems)
		if problems:
			bad += 1
			print(f'  x {label}')
			for p in problems:
				print(f'      {p}')
		else:
			print(f'  ok {label}')

print(f'\n{total} blocks checked, {total - bad} clean, {bad} with problems')
sys.exit(1 if bad else 0)
