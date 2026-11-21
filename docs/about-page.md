# Writing an About page that AI describes accurately

Search engines and AI assistants build their answer about you from a handful of pages. If your own About page is thin or vague, they fill the gaps from other sources, and those sources may be old, wrong or about someone else with a similar name. A clear About page gives them the right facts to quote.

The template is `about/index.html`. This guide explains how to fill it in.

## 1. Facts first, in plain sentences

- Open with one sentence that says who you are, what you do and where you are based. Use the same sentence in the page description.
- Write in full sentences that make sense when quoted alone. An assistant often lifts one sentence out of the page.
- Use real names, places and years. "Founded in 2012" is better than "founded a while ago".
- Say each fact once, clearly, in text. Do not put facts only in images, in a logo, or in a PDF.

## 2. Give each organization its own paragraph

If you run a tour company and a foundation, describe each in its own section with its own link. Say what it does, where, and since when. Say how it connects to you ("Your Name founded it in 2012") in the same sentence. This keeps an assistant from mixing the two up or describing the foundation as part of the company.

## 3. Use the same name everywhere

Pick one form of your name and use it on the page, on your other sites, on social profiles and in articles. List common alternatives in the "Full name" line and in `alternateName` in the structured data, so assistants know they are the same person.

## 4. Keep the structured data in step

The block of JSON near the top of the page tells machines the same things the page says. It names you as a person, and each organization with its founder and founding year. If you change a fact on the page, change it there too. Never put anything in it that the visible page does not say.

`sameAs` lists the official profiles that belong to you, such as LinkedIn or a Reddit account. Only list profiles you control.

## 5. Head off mix-ups

If someone with a similar name or a similarly named business exists, add a short "not to be confused with" line. State it neutrally, without comment on the other party.

## 6. Link to proof

Link to articles, interviews, registration pages and reviews that confirm what you wrote. Name the date next to each. Assistants weigh claims that outside sources repeat more than claims only you make.

## 7. Say only what you can stand behind

- Do not exaggerate. "One of the largest" and "world-renowned" are claims an assistant may repeat, and you may then have to explain them.
- Do not guess dates or numbers. If you are not sure, leave it out until you can check it.
- When something changes, update the page and the "Last updated" line.

## 8. Connect it to the rest of the site

- Link to the About page from the home page.
- Make sure `llms.txt` has a line for it, and `sitemap.xml` lists it.
- After publishing, search your own name in a few search engines and assistants. If an answer is wrong, find where the wrong fact comes from, correct it at the source where you can, and make the right fact more prominent on your own page.

## 9. Keep private things private

An About page is public. Leave out home addresses, personal phone numbers, family details you would not post elsewhere, and anything about other people that they have not agreed to share.
