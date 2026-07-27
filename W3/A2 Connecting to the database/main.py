# FastAPI app for the task API with SQLite database integration.
import sqlite3
from pathlib import Path

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


# FastAPI app for the task API.
app = FastAPI()

# Database path for SQLite.
DB_PATH = Path(__file__).with_name("tasks.db")

# Function to get a database connection.
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# Function to convert a database row to a task dictionary.
def row_to_task(row):
    return {
        "id": row["id"],
        "title": row["title"],
        "done": bool(row["done"]),
    }

# Starter data used on first boot and whenever /reset is called.
# We removed id from the seed data. SQLite will create ids automatically.

def seed_tasks() -> list[dict]:
    return [
        {"title": "Buy milk", "done": False},
        {"title": "Walk the dog", "done": True},
        {"title": "Read FastAPI docs", "done": False},
    ]


# Initialize the database and seed it with starter tasks if empty.
def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    done INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        row_count = conn.execute("SELECT COUNT(*) AS count FROM tasks").fetchone()["count"]

        if row_count == 0:
            conn.executemany(
                "INSERT INTO tasks (title, done) VALUES (?, ?)",
                [(task["title"], int(task["done"])) for task in seed_tasks()],
            )

# What this does:

# CREATE TABLE IF NOT EXISTS creates the tasks table only if it is missing.

# SELECT COUNT(*) checks how many tasks already exist.

# If there are 0 tasks, insert the 3 starter tasks.

# If there are already tasks, do not seed again.



# Call init_db() when the app starts to ensure the database is ready.
init_db()



class TaskCreate(BaseModel):
    # Request body for creating a task.
    title: str


class TaskUpdate(BaseModel):
    # Request body for updating a task.
    title: str | None = None
    done: bool | None = None


def next_task_id() -> int:
    # Find the next available task id.
    with get_connection() as conn:
        result = conn.execute("SELECT MAX(id) AS max_id FROM tasks").fetchone()
        return (result["max_id"] or 0) + 1


@app.get("/", summary="API info")
def root():
    # Return basic API details.
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks", "/stats", "/reset"],
    }


@app.get("/health", summary="Health check")
def health():
    # Simple server health check.
    return {"status": "ok"}

@app.get("/tasks", summary="List tasks (with optional filtering/search)")
def get_tasks(done: bool | None = None, search: str | None = None):
    query = "SELECT * FROM tasks"
    params = []
    conditions = []

    if done is not None:
        conditions.append("done = ?")
        params.append(int(done))

    if search is not None and search.strip():
        conditions.append("LOWER(title) LIKE ?")
        params.append(f"%{search.strip().lower()}%")

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    with get_connection() as conn:
        rows = conn.execute(query, params).fetchall()

    return [row_to_task(row) for row in rows]


@app.get("/tasks/{task_id}", summary="Get one task")
def get_task(task_id: int):
    with get_connection() as conn:
        row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

    return row_to_task(row)


#Ok so this will be my STAGE 2 COMMIT : "Stage 2: insert into database" as it worked

@app.post("/tasks", status_code=status.HTTP_201_CREATED, summary="Create a task")
def create_task(payload: TaskCreate):
    # Reject empty titles before saving.
    if not payload.title.strip():
        raise HTTPException(status_code=400, detail="Title is required")

    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            (payload.title, 0),
        )
        task_id = cursor.lastrowid
        row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()

    return row_to_task(row)


@app.put("/tasks/{task_id}", summary="Update a task")
def update_task(task_id: int, payload: TaskUpdate):
    with get_connection() as conn:
        existing = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()

        if existing is None:
            raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

        title = existing["title"]
        done = existing["done"]

        if payload.title is not None:
            if not payload.title.strip():
                raise HTTPException(status_code=400, detail="Title must not be empty")
            title = payload.title

        if payload.done is not None:
            done = int(payload.done)

        conn.execute(
            "UPDATE tasks SET title = ?, done = ? WHERE id = ?",
            (title, done, task_id),
        )
        updated = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()

    return row_to_task(updated)


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a task")
def delete_task(task_id: int):
    with get_connection() as conn:
        existing = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()

        if existing is None:
            raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

    return None

#Updated even these endpoints to use the database instead of in-memory list. Now all CRUD operations are persistent.
@app.get("/stats", summary="Task stats")
def get_stats():
    with get_connection() as conn:
        total = conn.execute("SELECT COUNT(*) AS count FROM tasks").fetchone()["count"]
        done = conn.execute("SELECT COUNT(*) AS count FROM tasks WHERE done = 1").fetchone()["count"]

    open_tasks = total - done
    return {"total": total, "done": done, "open": open_tasks}


#including this endpoint to reset the database to the starter set of tasks. This is useful for testing and development.
@app.post("/reset", summary="Reset tasks to the starter set")
def reset_tasks():
    with get_connection() as conn:
        conn.execute("DELETE FROM tasks")
        conn.executemany(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            [(task["title"], int(task["done"])) for task in seed_tasks()],
        )
        total = conn.execute("SELECT COUNT(*) AS count FROM tasks").fetchone()["count"]

    return {"message": "Tasks reset to starter data", "total": total}




