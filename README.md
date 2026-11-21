# Site starter

A small, plain starting point for a website you own. One HTML page, one `llms.txt`, and the steps to host it free with GitHub and Cloudflare.

The idea: one site under your own name, on a domain you control, that people and AI assistants can both read.

## What is in this repo

| File | What it is |
| --- | --- |
| `index.html` | A one-page site. Plain HTML and CSS, no build step, no frameworks. Edit the words and publish. |
| `llms.txt` | A short guide for AI assistants, so they can find and describe your site correctly. |
| `robots.txt` | Lets search engines and AI crawlers read the site, and points to the sitemap. |
| `sitemap.xml` | The list of pages on your site. Add a line for each new page. |
| `AGENTS.md` | Instructions for an AI assistant that is helping you edit this site. |

Every name, address and sentence in these files is a placeholder. Replace `Your Name` and `example.com` with your own.

## Why this setup

- **You own it.** The files are in your GitHub account and the domain is registered to you. Moving to another host later means pointing the domain somewhere else.
- **It is free to host.** Cloudflare serves static sites at no cost. You pay only for the domain, usually about $10 a year.
- **One site, not many.** One site under your own name is easier to keep up and easier for people and search engines to find than many small ones. If you already own several domains, pick one as the main site and forward the others to it.
- **AI can find it.** A plain HTML page with real text is easy for search engines and AI assistants to read. The `llms.txt` file gives them a short summary and a list of your best pages.

## Set it up

### 1. Put the files in your own GitHub repo

1. Make a free account at https://github.com if you do not have one.
2. Use this repo as a template (the green **Use this template** button, if it is enabled), or download the files and upload them to a new repository.
3. Make the new repository public or private. Cloudflare can read either one.

### 2. Edit the page

Open `index.html` and change the text between the tags: your name, a one-line description, a short "about" paragraph and a few links. Do the same in `llms.txt`, `robots.txt` and `sitemap.xml`, replacing `example.com` with your real domain.

You can edit files on github.com by opening a file and pressing the pencil icon, or ask an AI assistant to make the edits for you (see `AGENTS.md`).

### 3. Host it on Cloudflare

1. Make a free account at https://dash.cloudflare.com.
2. In the dashboard, go to **Workers & Pages** and create a new project from a GitHub repository. Pick the repository from step 1 and let Cloudflare connect to GitHub.
3. This site has no build step. Leave the build command empty and set the output (or assets) folder to the root of the repository, `/` or `.`.
4. Save and deploy. Cloudflare gives you a free address ending in `.pages.dev` or `.workers.dev`. Open it to check that your page loads.

Cloudflare changes the names of buttons and menus now and then. If a step looks different, the current guides are at https://developers.cloudflare.com/pages/ and https://developers.cloudflare.com/workers/static-assets/.

From now on, every change you save to GitHub is published automatically within a minute or so.

### 4. Use your own domain

1. Register a domain under your own name. Cloudflare Registrar sells domains at cost, and any other registrar works too.
2. If the domain is registered somewhere else, add it to Cloudflare and change its nameservers to the two Cloudflare gives you. The registrar's help pages explain how.
3. In your Cloudflare project, open the **Custom domains** setting and add the domain. Cloudflare sets up the records and the HTTPS certificate for you.
4. To send other domains you own to the main one, add them to Cloudflare as well and create a redirect rule that forwards every address to your main domain.

### 5. Tell search engines and AI where to look

- Make sure `https://your-domain/llms.txt`, `https://your-domain/robots.txt` and `https://your-domain/sitemap.xml` open in a browser.
- Add your domain in Google Search Console at https://search.google.com/search-console and submit the sitemap.
- Keep `llms.txt` current. When you add an important page, add a line for it.

## Keeping it simple

- One folder per page. A page at `/about/` is the file `about/index.html`.
- Write real sentences on the page, not text inside images. Both people and AI read the text.
- Give every page its own title and description.
- Do not put passwords, keys or private information in the repository. Anything in a public repository is public, and anything on the live site is public too.

## Adapting it

The files are meant to be changed, copied and reused. There is no license restriction on this starter: use it however you like.
