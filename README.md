# FlyRank AI Backend Engineering Internship

<p align="center">
  <img src="assets/flyrank-header.png" alt="FlyRank header" width="100%" />
</p>

<p align="center">
  <b>Backend systems, AI engineering fundamentals, API design, databases, containers, testing, and production-grade thinking.</b>
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,fastapi,postgres,docker,sqlite&theme=dark" alt="Python, FastAPI, PostgreSQL, Docker, and SQLite logos" />
</p>

<p align="center">
  <img alt="AI Systems" src="https://img.shields.io/badge/AI%20Systems-Production%20Grade-FF3D8B?style=for-the-badge&logo=openai&logoColor=white" />
  <img alt="Backend Engineering" src="https://img.shields.io/badge/Backend%20Engineering-From%20Scratch%20to%20Prod-7C3AED?style=for-the-badge" />
</p>

---

## Table Of Contents

- [What This Repo Is](#what-this-repo-is)
- [Internship Mission](#internship-mission)
- [Learning Roadmap](#learning-roadmap)
- [Repository Map](#repository-map)
- [Current Projects](#current-projects)
- [Backend AI Engineering Track](#backend-ai-engineering-track)
- [Testing Philosophy](#testing-philosophy)
- [Production Mindset](#production-mindset)
- [Quick Start](#quick-start)
- [Tech Stack](#tech-stack)
- [Progress Log](#progress-log)

---

## What This Repo Is

This repository documents my journey as a **Backend AI Engineering Intern at FlyRank**.

It starts with the basics: building clean APIs, understanding request and response flow, writing CRUD endpoints, connecting persistent storage, and containerizing services. From there, the goal is to keep leveling up toward backend systems that can support real AI products: reliable APIs, database-backed workflows, automated tests, containerized environments, observability, and production-ready deployment habits.

Think of this repo as my engineering lab:

```text
small backend ideas -> tested services -> database-backed systems -> containerized stacks -> production-grade AI infrastructure
```

---

## Internship Mission

The mission is to build backend systems from scratch and understand every layer instead of treating production AI apps like magic.

I am documenting:

- How APIs are designed, built, tested, and improved.
- How backend services evolve from in-memory demos to persistent database systems.
- How to use FastAPI, SQLite, PostgreSQL, Docker, and Docker Compose.
- How to think about reliability, validation, errors, environment variables, and deployment.
- How AI engineering fits into backend architecture: data flow, model-facing APIs, task queues, retrieval systems, evaluation, monitoring, and safe production behavior.

---

## Learning Roadmap

| Stage | Focus | What I Am Building Toward |
| --- | --- | --- |
| 1 | Backend basics | Python APIs, HTTP methods, JSON, request bodies, status codes |
| 2 | CRUD systems | Create, read, update, delete, validation, Swagger docs |
| 3 | Persistence | SQLite databases, schemas, SQL queries, durable storage |
| 4 | Production databases | PostgreSQL, environment variables, container networking |
| 5 | Containers | Dockerfiles, Docker Compose, reproducible local stacks |
| 6 | Testing | Unit tests, integration tests, API tests, database reset flows |
| 7 | AI backend systems | Model APIs, RAG services, background jobs, evaluation pipelines |
| 8 | Production readiness | Logging, monitoring, CI/CD, secrets, deployment, reliability |

---

## Repository Map

```text
FlyRank AI/
|-- README.md
|-- .gitignore
|-- assets/
|   |-- flyrank-header.png
|   |-- classic-dark.png
|   `-- flyrank-internship-confirmation-...pdf
|-- W2-A1-Building_my_first_CRUD_API/
|   |-- README.md
|   |-- main.py
|   |-- AI-GEN-CRUD/
|   |   |-- README.md
|   |   `-- ai_gen.py
|   `-- assets/
|       `-- swagger ui screenshots/
|-- W3/
|   |-- A2 Connecting to the database/
|   |   |-- README.md
|   |   |-- main.py
|   |   `-- assets/
|   |       `-- swagger ui screenshots/
|   `-- A3 Containerize your Stack/
|       |-- README.md
|       |-- main.py
|       |-- requirements.txt
|       |-- Dockerfile
|       |-- compose.yaml
|       `-- Stage_0.txt
```

---

## Current Projects

| Folder | What It Does | Main Lesson |
| --- | --- | --- |
| `W2-A1-Building_my_first_CRUD_API/` | A FastAPI task API using an in-memory Python list. Includes health checks, task CRUD, filtering, search, stats, reset behavior, and Swagger screenshots. | Learn how HTTP APIs work before adding database complexity. |
| `W2-A1-Building_my_first_CRUD_API/AI-GEN-CRUD/` | A small AI-generated CRUD experiment. | Compare generated backend code with hand-built backend understanding. |
| `W3/A2 Connecting to the database/` | The same Task API upgraded from memory to SQLite persistence. | Separate API behavior from storage implementation. |
| `W3/A3 Containerize your Stack/` | A containerized FastAPI + PostgreSQL stack using Docker Compose. | Run a backend service and database together like a real development environment. |
| `assets/` | Repo-level images and internship proof assets. | Keep visual identity and documentation assets organized. |

---

## Backend AI Engineering Track

This repo is not only about CRUD APIs. CRUD is the foundation.

The bigger direction is backend AI engineering:

- Build APIs that can serve AI features cleanly.
- Store and retrieve data safely.
- Design services that can later support embeddings, retrieval, model calls, async jobs, and evaluation.
- Test backend behavior before trusting it.
- Package systems so they run consistently on another machine.
- Learn production habits early: environment config, secret hygiene, database migrations, logs, observability, and failure handling.

The long-term target is to go from:

```text
Hello FastAPI
```

to:

```text
Production AI backend with APIs, databases, queues, model integrations, evaluations, monitoring, and deployment.
```

---

## Testing Philosophy

Every backend system should earn trust.

My testing checklist as this repo grows:

- **Smoke tests:** Does the app start?
- **Health tests:** Does `/health` return a clean response?
- **CRUD tests:** Can I create, read, update, and delete data?
- **Validation tests:** Do invalid requests fail correctly?
- **Persistence tests:** Does data survive restarts when using a database?
- **Integration tests:** Does the API talk to the database correctly?
- **Container tests:** Does the whole stack run from a clean Docker Compose setup?
- **AI tests:** Are prompts, model outputs, retrieval results, and evaluation metrics checked instead of guessed?

---

## Production Mindset

Production-grade AI systems need more than a working demo.

This repo will keep moving toward:

- Clear API contracts.
- Database-backed state.
- Repeatable local setup.
- Dockerized services.
- Testable behavior.
- Safe environment variable handling.
- Useful logs and debugging signals.
- Error responses that help clients recover.
- Future AI workflows that can be evaluated, monitored, and improved.

---

## Quick Start

### Run The Week 2 In-Memory API

```powershell
cd "W2-A1-Building_my_first_CRUD_API"
pip install fastapi uvicorn
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

### Run The Week 3 SQLite API

```powershell
cd "W3\A2 Connecting to the database"
pip install fastapi uvicorn
uvicorn main:app --reload
```

### Run The Week 3 Docker + PostgreSQL Stack

```powershell
cd "W3\A3 Containerize your Stack"
docker compose up --build
```

Open:

```text
http://localhost:8000/docs
```

---

## Tech Stack

| Area | Tools |
| --- | --- |
| Language | Python |
| API framework | FastAPI |
| Local server | Uvicorn |
| Validation | Pydantic |
| Databases | SQLite, PostgreSQL |
| Database driver | sqlite3, psycopg |
| Containers | Docker, Docker Compose |
| Documentation | Markdown, Swagger UI |
| Testing direction | curl, Swagger UI, future pytest/API integration tests |

---

## Progress Log

- [x] Built a basic FastAPI CRUD API.
- [x] Added endpoint documentation through Swagger UI.
- [x] Tested API behavior with curl and browser-based docs.
- [x] Upgraded in-memory storage to SQLite persistence.
- [x] Verified database state with SQLite tooling.
- [x] Containerized the backend with Docker.
- [x] Connected FastAPI to PostgreSQL through Docker Compose.
- [ ] Add automated tests with pytest.
- [ ] Add CI checks.
- [ ] Add structured logging.
- [ ] Add AI-focused backend services.
- [ ] Add evaluation and monitoring patterns for AI outputs.

---

<p align="center">
  <b>Built from first principles. Tested like it matters. Documented as the system grows.</b>
</p>
