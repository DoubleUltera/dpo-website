# Quick Deploy Guide

## Every time you make changes and want to publish:

```bash
# 1. Add all changed files
git add .

# 2. Commit with a message describing what changed
git commit -m "Your description of changes here"

# 3. Push to GitHub (auto-deploys to Netlify)
git push
```

## Common commit messages:
- `git commit -m "Add new blog post about [topic]"`
- `git commit -m "Update contact information"`
- `git commit -m "Fix typo on homepage"`
- `git commit -m "Update service pricing"`

## One-liner (all steps at once):
```bash
git add . && git commit -m "Your message" && git push
```

## Check what changed before committing:
```bash
git status          # See which files changed
git diff            # See exactly what changed in files
```

## If you want to undo uncommitted changes:
```bash
git checkout -- filename.astro    # Undo changes to one file
git reset --hard                   # Undo ALL uncommitted changes (careful!)
```

---

**Note:** Every push to GitHub triggers an automatic Netlify deployment (2-3 minutes).
Watch progress at: https://app.netlify.com
