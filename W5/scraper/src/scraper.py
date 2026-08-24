from __future__ import annotations

import hashlib
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse, urljoin

from bs4 import BeautifulSoup

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

def soup_from_html(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "html.parser")


def extract_book_urls(html: str, page_url: str) -> list[str]:
    soup = soup_from_html(html)
    urls: list[str] = []

    for article in soup.select("article.product_pod"):
        link = article.select_one("h3 a")
        if not link or not link.get("href"):
            continue
        urls.append(urljoin(page_url, link["href"]))

    return urls


def extract_next_page_url(html: str, page_url: str) -> str | None:
    soup = soup_from_html(html)
    next_link = soup.select_one("li.next a")
    if not next_link or not next_link.get("href"):
        return None
    return urljoin(page_url, next_link["href"])


def discover_book_urls(stats: dict[str, Any], max_pages: int = 3) -> tuple[list[str], dict[str, str]]:
    page_url: str | None = START_URL
    catalogue_pages = 0
    discovered: list[str] = []
    source_pages: dict[str, str] = {}

    while page_url and catalogue_pages < max_pages:
        html = fetch_html(page_url, stats)
        catalogue_pages += 1

        for book_url in extract_book_urls(html, page_url):
            discovered.append(book_url)
            source_pages[book_url] = page_url

        page_url = extract_next_page_url(html, page_url)

    unique_urls = list(dict.fromkeys(discovered))
    print(f"catalogue_pages={catalogue_pages}")
    print(f"discovered={len(discovered)}")
    print(f"unique_urls={len(unique_urls)}")
    return unique_urls, source_pages



def run() -> None:
    stats = {
        "pages_fetched": 0,
        "cache_hits": 0,
    }
    discover_book_urls(stats, max_pages=3)

