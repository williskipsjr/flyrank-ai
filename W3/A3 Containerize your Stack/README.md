# Containerized Task API

A REST Task API built with FastAPI, PostgreSQL, Docker, and Docker Compose.

This project continues the same Task API across three storage approaches:

| Assignment | Storage |
|---|---|
| A1 | In-memory Python list |
| A2 | SQLite database |
| A3 | PostgreSQL running in Docker |

The API contract stays the same while the storage layer changes underneath it.

## Tech Stack

- Python
- FastAPI
- Uvicorn
- PostgreSQL 16
- psycopg
- python-dotenv
- Docker
- Docker Compose

## Project Structure

```text
.
├── main.py
├── requirements.txt
├── Dockerfile
├── compose.yaml
├── .env.example
├── .dockerignore
└── README.md
```

The real `.env` file is intentionally not listed because it is local-only and ignored by Git.

## Environment Variables

Create a local `.env` file from the example file:

```powershell
Copy-Item .env.example .env
```

Then edit `.env` with your real local password if needed:

```env
DATABASE_URL=postgresql://postgres:flyrankai@localhost:5432/tasks
```

The committed example file documents the required variable without exposing a real password:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/tasks
```

Inside Docker Compose, the API uses this connection string:

```text
postgresql://postgres:flyrankai@db:5432/tasks
```

The hostname is `db` because the FastAPI container connects to the PostgreSQL container through Docker Compose networking.

## Quick Start

Clone the repository:

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_REPOSITORY_DIRECTORY>
```

Create the environment file:

```powershell
Copy-Item .env.example .env
```

Start the full stack:

```bash
docker compose up --build
```

The API will be available at:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

## API Endpoints

| Method | Endpoint | Description | Success |
|---|---|---|---:|
| GET | `/` | API information | 200 |
| GET | `/health` | Health check | 200 |
| GET | `/tasks` | List all tasks | 200 |
| GET | `/tasks?done=true` | Filter tasks by completion status | 200 |
| GET | `/tasks?search=milk` | Search tasks by title | 200 |
| GET | `/tasks/{id}` | Get one task | 200 |
| POST | `/tasks` | Create a task | 201 |
| PUT | `/tasks/{id}` | Update a task | 200 |
| DELETE | `/tasks/{id}` | Delete a task | 204 |
| GET | `/stats` | Return task counts | 200 |
| POST | `/reset` | Reset starter tasks | 200 |

## Error Responses

| Situation | Status |
|---|---:|
| Empty task title on create | 400 |
| Empty task title on update | 400 |
| Task ID does not exist | 404 |

## Example Request

```bash
curl -i http://localhost:8000/tasks
```

Example response:

```text
HTTP/1.1 200 OK
content-type: application/json

[
  {
    "id": 1,
    "title": "Buy milk",
    "done": false
  },
  {
    "id": 2,
    "title": "Walk the dog",
    "done": true
  },
  {
    "id": 3,
    "title": "Read FastAPI docs",
    "done": false
  }
]
```

## Verify PostgreSQL Data

Open a PostgreSQL shell inside the database container:

```bash
docker compose exec db psql -U postgres -d tasks
```

List tables:

```sql
\dt
```

Read the seeded tasks:

```sql
SELECT * FROM tasks;
```

Expected starter rows:

```text
 id |       title       | done
----+-------------------+------
  1 | Buy milk          | f
  2 | Walk the dog      | t
  3 | Read FastAPI docs | f
```

Exit PostgreSQL:

```sql
\q
```

You can also verify the rows with one command:

```bash
docker compose exec db psql -U postgres -d tasks -c "SELECT * FROM tasks;"
```

## Database Screenshot

Add a screenshot showing the PostgreSQL `tasks` table after running:

```sql
\dt
SELECT * FROM tasks;
```

Recommended path:

```text
docs/postgres-tasks.png
```

Then include it in this README:

```markdown
![PostgreSQL tasks table](docs/postgres-tasks.png)
```

## Persistence

PostgreSQL data is stored in a Docker named volume:

```yaml
volumes:
  taskdata:
```

That means task data survives normal container restarts:

```bash
docker compose down
docker compose up
```

Do not run this unless you intentionally want to delete the development database volume:

```bash
docker compose down -v
```

## Parameterized SQL

The app uses psycopg placeholders instead of building SQL strings with user input.

Example:

```python
conn.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
```

Avoid string interpolation in SQL queries:

```python
f"SELECT * FROM tasks WHERE id = {task_id}"
```

Parameterized queries separate SQL instructions from user-provided values and help protect against SQL injection.

## Round-Trip Check

A clean setup should work with:

```powershell
Copy-Item .env.example .env
docker compose up --build
```

Then, in another terminal:

```bash
curl -i http://localhost:8000/tasks
```

Expected result: `200 OK` with starter tasks returned in under a few minutes, with no manual PostgreSQL installation or table creation.
