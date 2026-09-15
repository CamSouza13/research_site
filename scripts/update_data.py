"""Refresh site data for GitHub Pages.

1. Medium: reads assets/data/config.json -> medium_user, fetches the public
   RSS feed and writes assets/data/medium.json (latest 6 posts).
2. CO2: downloads NOAA GML Mauna Loa monthly means and writes
   assets/data/co2.json.

Standard library only. Run locally with `python scripts/update_data.py`.
"""
import csv
import html
import io
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "assets" / "data"
UA = {"User-Agent": "Mozilla/5.0 (personal site data refresh)"}
NOAA_URL = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv"


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def strip_tags(text: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", text))).strip()


def update_medium() -> None:
    cfg = json.loads((DATA / "config.json").read_text())
    user = cfg.get("medium_user", "").strip().lstrip("@")
    if not user:
        print("medium: no medium_user set, skipping")
        return
    root = ET.fromstring(fetch(f"https://medium.com/feed/@{user}"))
    ns = {"content": "http://purl.org/rss/1.0/modules/content/"}
    posts = []
    for item in root.iter("item"):
        body = item.findtext("content:encoded", default="", namespaces=ns)
        img = re.search(r'<img[^>]+src="([^"]+)"', body)
        text = strip_tags(body)
        date = parsedate_to_datetime(item.findtext("pubDate", default=""))
        posts.append({
            "title": item.findtext("title", default="").strip(),
            "link": item.findtext("link", default="").split("?")[0],
            "date": date.date().isoformat(),
            "excerpt": (text[:200].rsplit(" ", 1)[0] + "...") if len(text) > 200 else text,
            "image": img.group(1) if img else "",
        })
    (DATA / "medium.json").write_text(json.dumps(posts[:6], indent=2) + "\n")
    print(f"medium: wrote {len(posts[:6])} posts for @{user}")


def update_co2() -> None:
    raw = fetch(NOAA_URL).decode("utf-8")
    rows = [r for r in csv.reader(io.StringIO(raw)) if r and not r[0].startswith("#")]
    rows = rows[1:]  # drop header
    out = {
        "start": [int(rows[0][0]), int(rows[0][1])],
        "avg": [round(float(r[3]), 2) for r in rows],
        "trend": [round(float(r[4]), 2) for r in rows],
    }
    (DATA / "co2.json").write_text(json.dumps(out, separators=(",", ":")) + "\n")
    print(f"co2: wrote {len(rows)} months through {rows[-1][0]}-{rows[-1][1]}")


if __name__ == "__main__":
    failed = False
    for job in (update_medium, update_co2):
        try:
            job()
        except Exception as exc:  # keep one failure from blocking the other
            print(f"{job.__name__} failed: {exc}", file=sys.stderr)
            failed = True
    sys.exit(1 if failed else 0)
