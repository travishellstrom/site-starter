# Ask Jim: a search page for your Reddit comments

This folder is a small search page over your own Reddit comments. Visitors type a word or question and see the comments that match, with a link to each original thread. It uses no AI and no outside services. The search runs in the visitor's browser over one file, `comments.json`.

Rename the folder and the page to suit (the sample uses `/ask/`). Replace "Your Name" in `index.html` with your name.

## Step 1: Ask Reddit for your data

1. Sign in to Reddit in a browser.
2. Open the data request page: https://www.reddit.com/settings/data-request
3. Choose to request your data and submit the request. Reddit says it can take up to 30 days, and often arrives sooner.
4. Reddit emails you a link when it is ready. Download the zip file and unzip it.

Inside is a `comments.csv` file. It contains every comment on your account.

## Step 2: Turn it into `comments.json`

You need Python 3.9 or newer, which most computers have or can install from https://www.python.org/downloads/.

From this folder, run:

```
python3 convert.py path/to/comments.csv
```

This writes `comments.json` next to the page. It keeps only the comment text, date, subreddit and link. The IP address and other private columns in Reddit's file are dropped, and `[deleted]` and `[removed]` comments are skipped.

Useful options:

- `--min-length 80` skips short replies such as "Thanks!" (the default is 40 characters).
- `--skip-subreddit name` leaves out a subreddit. Repeat it for more than one.

## Step 3: Read it before you publish it

`comments.json` will be public once it is on your site. Open it and read through it. Take out anything you would not want attached to your name: private details, comments about other people, old posts you have changed your mind about. You can delete entries from the file by hand, or skip a whole subreddit with `--skip-subreddit`. A comment that is deleted on Reddit but still in your export will reappear on your site, so check for those too.

## Step 4: Look at it on your computer

Browsers do not let a page read a file from your disk, so serve the folder:

```
cd ask-jim
python3 -m http.server 8000
```

Then open http://localhost:8000 in a browser. Search for a few words you know you used.

## Step 5: Publish it

Put the folder in the same GitHub repository as the rest of your site (for example as `ask/`) and let Cloudflare publish it. Add the page to `sitemap.xml` and a line for it in `llms.txt`.

## Keeping it current

Export again every few months, run the converter and replace `comments.json`.

## Good to know

- Search matches words, not meaning. Searching "giving" will not find a comment that only says "donate".
- Results are your own words from Reddit. Nothing is generated or summarized.
- Reddit's terms and your own comfort set the limits on what to publish. Comments are your own writing, but check Reddit's current terms if you plan to do more than show them.
