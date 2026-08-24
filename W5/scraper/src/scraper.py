from __future__ import annotations

import hashlib
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import requests


BASE_URL = "https://books.toscrape.com/"
START_URL = "https://books.toscrape.com/catalogue/page-1.html"
USER_AGENT = "FlyRankInternship-A9/1.0 (+https://github.com/your-username/polite-scraper)"
TIMEOUT_SECONDS = 8
REQUEST_DELAY_SECONDS = 0.5

ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = ROOT / "cache"
OUTPUT_DIR = ROOT / "output"


def now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def cache_path_for(url: str) -> Path:
    parsed = urlparse(url)
    slug = parsed.path.strip("/").replace("/", "__") or "index"
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
    return CACHE_DIR / f"{slug}__{digest}.html"


def fetch_html(url: str, stats: dict[str, Any], *, use_cache: bool = True) -> str:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path = cache_path_for(url)

    if use_cache and path.exists():
        html = path.read_text(encoding="utf-8")
        stats["cache_hits"] += 1
        print(f"CACHE HIT {url} size={len(html)}")
        return html

    print(f"FETCH {url}")
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(url, headers=headers, timeout=TIMEOUT_SECONDS)
    stats["pages_fetched"] += 1

    if response.status_code != 200:
        raise requests.HTTPError(f"status={response.status_code} url={url}", response=response)

    html = response.text
    path.write_text(html, encoding="utf-8")
    print(f"FETCHED {url} size={len(html)}")
    time.sleep(REQUEST_DELAY_SECONDS)
    return html


def run() -> None:
    stats = {
        "pages_fetched": 0,
        "cache_hits": 0,
    }
    html = fetch_html(START_URL, stats)
    print(f"response_size={len(html)}")
