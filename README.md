# FlyRank AI Backend Engineering Internship

<p align="center">
  <img src="assets/flyrank-header.png" alt="FlyRank AI backend internship header" width="100%" />
</p>

<p align="center">
  <b>FastAPI backends, CRUD APIs, databases, Docker, Supabase Auth, polite scraping, Swagger documentation, and production-minded learning.</b>
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,fastapi,sqlite,postgres,docker,supabase&theme=dark" alt="Python, FastAPI, SQLite, PostgreSQL, Docker, and Supabase logos" />
</p>

<p align="center">
  <img alt="Backend Engineering" src="https://img.shields.io/badge/Backend%20Engineering-FastAPI-00E5FF?style=for-the-badge" />
  <img alt="Databases" src="https://img.shields.io/badge/Databases-SQLite%20%2B%20PostgreSQL-FF2BD6?style=for-the-badge" />
  <img alt="Supabase Auth" src="https://img.shields.io/badge/Supabase-%20Auth-39FF14?style=for-the-badge&logo=supabase&logoColor=000000&labelColor=050505" />
  <img alt="Beautiful Soup" src="https://img.shields.io/badge/Beautiful%20Soup-HTML%20Parsing-6DB33F?style=for-the-badge" />
</p>

---

## Table Of Contents

- [FlyRank AI Backend Engineering Internship](#flyrank-ai-backend-engineering-internship)
  - [Table Of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Repository Map](#repository-map)
  - [Weekly Work](#weekly-work)
  - [What I Built](#what-i-built)
    - [Week 2 - First CRUD API](#week-2---first-crud-api)
    - [Week 3 - Databases And Containers](#week-3---databases-and-containers)
    - [Week 4 - Supabase Authentication](#week-4---supabase-authentication)
    - [Week 5 - The Polite Scraper](#week-5---the-polite-scraper)
  - [Tech Stack](#tech-stack)
  - [Quick Start](#quick-start)
  - [Progress](#progress)

---

## Overview

This repository documents my FlyRank AI backend engineering internship work from Week 2 through Week 5.

The learning path moved step by step:

```text
in-memory API -> SQLite persistence -> PostgreSQL in Docker -> Supabase authentication -> polite scraping pipeline
```

Each assignment builds on the previous one: first understanding API behavior, then adding persistence, then containerizing the stack, then protecting routes with real authentication, then collecting and validating web data responsibly.

## Repository Map

```text
FlyRank AI/
|-- README.md
|-- assets/
|-- W2-A1-Building_my_first_CRUD_API/
|   |-- README.md
|   |-- main.py
|   `-- AI-GEN-CRUD/
|-- W3/
|   |-- A2 Connecting to the database/
|   `-- A3 Containerize your Stack/
|-- W4/
|   |-- README.md
|   |-- Swagger UI Screenshots/
|   `-- flyrank-auth-api/
`-- W5/
    |-- HANDS_ON_GUIDE.md
    |-- W5 - The polite scraper.pdf
    `-- scraper/
        |-- README.md
        |-- src/
        |-- tests/
        `-- output/
```

## Weekly Work

| Week | Folder | Focus | Result |
| --- | --- | --- | --- |
| W2 | `W2-A1-Building_my_first_CRUD_API/` | FastAPI CRUD basics | Built a task API with in-memory storage, health checks, filters, search, stats, reset, curl examples, and Swagger screenshots. |
| W3 A2 | `W3/A2 Connecting to the database/` | SQLite persistence | Replaced temporary Python-list storage with `tasks.db`, added schema creation, seed data, SQL queries, persistence checks, and DB Browser evidence. |
| W3 A3 | `W3/A3 Containerize your Stack/` | Docker + PostgreSQL | Containerized the FastAPI task API, connected it to PostgreSQL 16 through Docker Compose, added environment variables and database verification steps. |
| W4 | `W4/flyrank-auth-api/` | Supabase Auth | Built signup, login, logout, public routes, protected profile/dashboard routes, reusable `HTTPBearer` dependency, and Swagger authorization evidence. |
| W5 | `W5/scraper/` | Polite scraping pipeline | Built a Books to Scrape pipeline with target classification, caching, polite requests, HTML parsing, normalization, Pydantic validation, failure handling, tests, and run reports. |

## What I Built

### Week 2 - First CRUD API

The Week 2 project is a small task manager API built with FastAPI. It supports creating, reading, updating, deleting, filtering, searching, resetting, and counting tasks. Data is intentionally stored in memory, which made it easier to understand HTTP methods, request bodies, status codes, and Swagger UI before adding a database.

### Week 3 - Databases And Containers

Week 3 upgraded the same task API into more realistic backend systems.

In A2, task data moved into SQLite so it survives server restarts. In A3, the API moved to PostgreSQL running inside Docker Compose, with the FastAPI service and database service connected through container networking.

### Week 4 - Supabase Authentication

Week 4 added real authentication using Supabase Auth. The API now supports signup and login, returns access tokens, protects profile and dashboard routes, and uses a reusable FastAPI dependency with `HTTPBearer`. Swagger UI screenshots in `W4/Swagger UI Screenshots/` document signup, login, public responses, authorization, protected responses, and logout.

### Week 5 - The Polite Scraper

Week 5 built a polite scraping pipeline for Books to Scrape, a public practice sandbox. The scraper checks the target first, fetches only the first 3 catalogue pages, discovers 60 unique book URLs, caches HTML during development, extracts detail records, normalizes prices, validates output with Pydantic, skips a deliberately broken page without crashing, and writes `books.json`, `errors.json`, and `run-report.json`.

I also created a hands-on guide in `W5/HANDS_ON_GUIDE.md` so the assignment can be rebuilt stage by stage with code, checkpoints, tests, and commit messages.

## Tech Stack

| Area | Tools |
| --- | --- |
| Language | Python |
| API framework | FastAPI |
| Server | Uvicorn |
| Docs/testing UI | Swagger UI |
| Validation | Pydantic |
| Local database | SQLite |
| Production-style database | PostgreSQL |
| Containers | Docker, Docker Compose |
| Auth | Supabase Auth, JWT bearer tokens |
| Scraping | Requests, Beautiful Soup |
| Verification | curl, Swagger UI screenshots, database inspection, pytest, run reports |

## Quick Start

Run Week 2:

```powershell
cd "W2-A1-Building_my_first_CRUD_API"
pip install fastapi uvicorn
uvicorn main:app --reload
```

Run Week 3 SQLite:

```powershell
cd "W3\A2 Connecting to the database"
pip install fastapi uvicorn
uvicorn main:app --reload
```

Run Week 3 Docker + PostgreSQL:

```powershell
cd "W3\A3 Containerize your Stack"
docker compose up --build
```

Run Week 4 Auth API:

```powershell
cd "W4\flyrank-auth-api"
pip install fastapi uvicorn supabase python-dotenv pydantic
uvicorn app.main:app --reload
```

Run Week 5 Polite Scraper:

```powershell
cd "W5\scraper"
pip install -r requirements.txt
python src/main.py
pytest
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Progress

- [x] Built a FastAPI CRUD API from scratch.
- [x] Documented endpoints with Swagger UI and README examples.
- [x] Tested API behavior with curl.
- [x] Added SQLite persistence and database inspection.
- [x] Containerized FastAPI with Docker.
- [x] Connected FastAPI to PostgreSQL using Docker Compose.
- [x] Added Supabase signup and login.
- [x] Protected routes with JWT bearer authentication.
- [x] Documented Swagger UI auth flow with screenshots.
- [x] Built a polite scraper for the first 3 Books to Scrape catalogue pages.
- [x] Cached fetched HTML and used a clear user-agent, timeout, and request delay.
- [x] Extracted, normalized, and validated 60 unique book records.
- [x] Added failure handling and `run-report.json` evidence.
- [x] Added pytest coverage for scraper helpers.
- [x] Wrote a Week 5 hands-on guide with staged commits and checkpoints.
- [ ] Add CI checks.
- [ ] Add deployment notes.

---

<p align="center">
  <b>From simple endpoints to authenticated, database-backed systems and responsible data pipelines.</b>
</p>
