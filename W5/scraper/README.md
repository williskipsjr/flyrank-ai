# Polite Scraper

## Target Classification

Target site: Books to Scrape - https://books.toscrape.com/

Why this target is appropriate: Books to Scrape is a public sandbox designed for scraping practice.

Scope: only the first 3 catalogue pages.

Data collected: book title, product URL, price text, availability text, rating text, description, source page, fetched timestamp, and normalized GBP price.

Robots check: visited https://books.toscrape.com/robots.txt and recorded the result here: <write your observed result>.

I will not reuse this code on another site without checking its rules and terms first.

## Run

```powershell
python src/main.py
```

## Install

This project uses the Python lane.

Requirements:

- Python 3.10+
- `requests`
- `beautifulsoup4`
- `pydantic`
- `pytest`

Install:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Test

```powershell
pytest
```

## Publish Evidence

The project should be pushed to a public GitHub repository with the code and one sample output. Cached HTML files should not be committed, because `cache/` can contain many saved pages that are only used during local development.

Before committing, make sure `.gitignore` includes:

```gitignore
cache/
__pycache__/
.pytest_cache/
.venv/
```

Sample output to commit:

- `output/books.json`
- `output/run-report.json`

## Record Schema

Each valid record in `output/books.json` has this shape:

```json
{
  "title": "A Light in the Attic",
  "product_url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
  "price_text": "\u00a351.77",
  "price_gbp": 51.77,
  "availability_text": "In stock (22 available)",
  "rating_text": "Three",
  "description": "Optional description text or null",
  "source_page": "https://books.toscrape.com/catalogue/page-1.html",
  "fetched_at": "2026-08-24T14:02:13Z"
}
```

Field summary:

- `title`: book title as text.
- `product_url`: canonical absolute HTTPS URL for the book.
- `price_text`: original price string from the page.
- `price_gbp`: normalized numeric price.
- `availability_text`: original availability text.
- `rating_text`: rating text from the page.
- `description`: product description, or `null` when missing.
- `source_page`: catalogue page where the book was discovered.
- `fetched_at`: UTC timestamp for when the record was fetched.

## Politeness Rules

This scraper follows these rules:

- Sends an identifying user-agent.
- Uses a request timeout.
- Checks the HTTP status code before parsing.
- Waits at least 500 ms between real requests.
- Uses cached HTML during development.
- Scrapes only the first 3 catalogue pages.
- Does not retry `404` or `403` responses.
- Logs failed pages instead of crashing the full run.

## Why No Browser Is Needed

This assignment does not need a browser because the data is already present in the HTML that the server sends. A browser would only add extra cost and complexity for this target.

## Ethics Note

Use an official API when one exists. Never bypass logins, paywalls, access blocks, or rate limits. Collect only what the task needs, identify your scraper honestly, and check the site's rules before scraping anything.

## Limitation

This scraper is intentionally written for Books to Scrape only. It should not be reused on another website without first checking that site's rules, robots policy, terms, and expected traffic limits.

## Sample Run Report

This is one real `output/run-report.json` from a successful run:

```json
{
  "started_at": "2026-08-24T14:02:13Z",
  "duration_seconds": 6.39,
  "pages_fetched": 1,
  "cache_hits": 63,
  "valid_records": 60,
  "invalid_records": 0,
  "failed_pages": 1,
  "failed_page_details": [
    {
      "url": "https://books.toscrape.com/catalogue/this-page-does-not-exist/index.html",
      "reason": "status=404 url=https://books.toscrape.com/catalogue/this-page-does-not-exist/index.html"
    }
  ]
}
```

## Checkpoint

A stranger should be able to clone the repository, install dependencies, run one documented command, and get:

- `output/books.json`
- `output/run-report.json`

Expected result:

- `output/books.json` contains 60 validated records.
- `output/run-report.json` reports counts, cache hits, duration, and failed pages.
- `git log --oneline` shows 7+ meaningful stage commits.

## Stage 6 Commit

After updating this README and verifying the run, commit with:

```powershell
git add README.md output/books.json output/run-report.json
git commit -m "Stage 6: publish scraper evidence"
```
