#!/usr/bin/env python3
"""Turn Reddit's comments.csv export into comments.json for the search page.

Usage:
    python3 convert.py path/to/comments.csv
    python3 convert.py path/to/comments.csv --min-length 60 --skip-subreddit privatesub

Only these fields are kept: id, date, subreddit, link, text.
Reddit's export also has an IP address column and other fields. They are dropped
on purpose and never written to the output file.
"""
import argparse
import csv
import json
import sys


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("csv_file", help="comments.csv from the Reddit data export")
    p.add_argument("-o", "--output", default="comments.json", help="output file (default: comments.json)")
    p.add_argument("--min-length", type=int, default=40,
                   help="skip comments shorter than this many characters (default: 40)")
    p.add_argument("--skip-subreddit", action="append", default=[],
                   help="leave out a subreddit (repeat the flag for more than one)")
    args = p.parse_args()

    skip = {s.lower().removeprefix("r/") for s in args.skip_subreddit}
    kept, dropped = [], 0

    with open(args.csv_file, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            text = (row.get("body") or "").strip()
            sub = (row.get("subreddit") or "").strip()
            if (len(text) < args.min_length
                    or text.lower() in ("[deleted]", "[removed]")
                    or sub.lower() in skip):
                dropped += 1
                continue
            kept.append({
                "id": row.get("id", ""),
                "date": (row.get("date") or "")[:10],
                "subreddit": sub,
                "link": row.get("permalink", ""),
                "text": text,
            })

    kept.sort(key=lambda c: c["date"], reverse=True)
    with open(args.output, "w", encoding="utf-8") as out:
        json.dump(kept, out, ensure_ascii=False, indent=1)

    print(f"Kept {len(kept)} comments, left out {dropped}. Wrote {args.output}.")
    print("Read through the file before you publish it. Remove anything you would not want public.")


if __name__ == "__main__":
    sys.exit(main())
