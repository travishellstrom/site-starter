# Instructions for an AI assistant

This repository is a small personal website: plain HTML and CSS, no build step, hosted as static files on Cloudflare from this GitHub repository. The owner may ask you to edit it, add pages or explain how it works. Read `README.md` first.

## How the site is laid out

- `index.html` is the home page.
- A page at `/about/` is the file `about/index.html`. Use one folder per page.
- `llms.txt`, `robots.txt` and `sitemap.xml` sit at the root and must list every important page.

## When you add or change a page

1. Give the page its own `<title>`, meta description and canonical link, using the real domain.
2. Put the words in real HTML text, with one `<h1>` per page.
3. Add the page to `sitemap.xml` and, if it matters, to `llms.txt` with one plain line saying what it contains.
4. Keep the page working with no JavaScript. Use no frameworks and no build tools unless the owner asks for them.
5. Check that every link on the page opens a real address.

## Rules

- Write plain, factual copy in the owner's own voice. Do not add slogans, jokes or claims the owner has not given you.
- Never invent biography details, quotes, dates, awards or links. Ask the owner when something is missing.
- Keep secrets out of the repository: no passwords, API keys, private emails or personal details. Everything committed here may be public.
- Make small changes and tell the owner what changed and why.
- Do not publish or send anything on the owner's behalf without their approval.
