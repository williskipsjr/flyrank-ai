# Week 4 - Auth Login and Protected Routes

This folder contains the Week 4 FlyRank backend assignment files for building a FastAPI authentication API with Supabase Auth.

## Source Files

- `HANDS_ON_GUIDE.md` - assignment guide and staged implementation checklist.
- `W4 - Auth - Login & protect.pdf` - assignment brief in PDF form.
- `flyrank-auth-api/` - FastAPI project.

The files above contain assignment instructions. The verification notes below record what was actually checked in the local project.

## Current Progress

Current Week 4 commits:

| Stage | Commit | Status |
| --- | --- | --- |
| Stage 0 | `e6dad32` - `Stage 0: setup server and supabase client` | Completed |
| Stage 1 | `4da2fa1` - `Stage 1: signup and login routes working` | Completed and curl-verified |
| Stage 2 | Not committed yet | Pending |
| Stage 3 | Not committed yet | Pending |
| Stage 4 | Not committed yet | Pending |
| Stage 5 | Not committed yet | Pending |
| Stage 6 | Not committed yet | Pending |

Current `HEAD` is `4da2fa1`.

## Local Setup

From this folder:

```bash
cd flyrank-auth-api
```

Install dependencies:

```bash
pip install fastapi uvicorn supabase python-dotenv pydantic
```

Create `.env`:

```env
SUPABASE_URL=your_project_url
SUPABASE_KEY=your_anon_key
```

Run the API:

```bash
uvicorn app.main:app --reload
```

Verified local run used this equivalent command because the Windows sandbox reloader hit a named-pipe permission issue:

```bash
python -m uvicorn app.main:app --port 8001
```

## Endpoint Status at Stage 1

| Method | Endpoint | Auth Required | Current Status |
| --- | --- | --- | --- |
| GET | `/` | No | Removed by current Stage 1 code, returns `404` at `HEAD` |
| POST | `/auth/signup` | No | Implemented |
| POST | `/auth/login` | No | Implemented |
| POST | `/auth/logout` | Yes | Pending Stage 4 |
| GET | `/public/info` | No | Pending Stage 2 |
| GET | `/protected/profile` | Yes | Pending Stage 2/3/4 |
| GET | `/protected/dashboard` | Yes | Pending Stage 4 |

## Curl Verification Log

Verification date: 2026-08-23

Server used:

```bash
python -m uvicorn app.main:app --port 8001
```

Base URL used:

```text
http://127.0.0.1:8001
```

### Stage 0 - Root Route

Stage 0 commit `e6dad32` contains:

```python
@app.get("/")
def root():
    return {
        "message": "API running successfully"
    }
```

Expected Stage 0 curl:

```bash
curl -i http://127.0.0.1:8001/
```

Expected Stage 0 output:

```http
HTTP/1.1 200 OK
content-type: application/json

{"message":"API running successfully"}
```

Current Stage 1 `HEAD` output for the same command:

```http
HTTP/1.1 404 Not Found
content-type: application/json

{"detail":"Not Found"}
```

Note: this is because the current Stage 1 `app/main.py` no longer includes the Stage 0 root route.

### Stage 1 - Signup

Request body used:

```json
{"email":"codex.w4.20260823.005@example.com","password":"password123"}
```

Curl command verified:

```bash
curl.exe -i -X POST http://127.0.0.1:8001/auth/signup -H "Content-Type: application/json" -d @tmp_signup.json
```

Verified output:

```http
HTTP/1.1 201 Created
content-type: application/json

{
  "id": "562d9d03-6bcb-4f00-bb56-5e512cf1ae69",
  "email": "codex.w4.20260823.005@example.com",
  "role": "authenticated",
  "is_anonymous": false
}
```

The full Supabase response also included `app_metadata`, `user_metadata`, timestamps, and identity details.

### Stage 1 - Login

Curl command verified:

```bash
curl.exe -i -X POST http://127.0.0.1:8001/auth/login -H "Content-Type: application/json" -d @tmp_signup.json
```

Verified output:

```http
HTTP/1.1 200 OK
content-type: application/json

{
  "access_token": "<JWT returned>",
  "refresh_token": "<refresh token returned>"
}
```

Tokens were intentionally redacted from this README.

### Stage 1 - Login Before Signup or Wrong Credentials

Observed while testing before the verified signup completed:

```http
HTTP/1.1 401 Unauthorized
content-type: application/json

{"detail":"Invalid login credentials"}
```

## Pending Verification Commands

Run these after the matching stages are implemented and committed.

### Stage 2 - Public Route

```bash
curl -i http://127.0.0.1:8001/public/info
```

Expected:

```http
HTTP/1.1 200 OK

{"message":"Welcome stranger! This info is public."}
```

### Stage 2 - Protected Profile Without Token

```bash
curl -i http://127.0.0.1:8001/protected/profile
```

Expected:

```http
HTTP/1.1 401 Unauthorized
```

### Stage 3 - Protected Profile With Valid Token

```bash
curl -i http://127.0.0.1:8001/protected/profile -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Expected:

```http
HTTP/1.1 200 OK
```

### Stage 3 - Protected Profile With Invalid Token

```bash
curl -i http://127.0.0.1:8001/protected/profile -H "Authorization: Bearer INVALID_TOKEN"
```

Expected:

```http
HTTP/1.1 401 Unauthorized
```

### Stage 4 - Protected Dashboard

```bash
curl -i http://127.0.0.1:8001/protected/dashboard -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Expected:

```http
HTTP/1.1 200 OK
```

### Stage 4 - Logout

```bash
curl -i -X POST http://127.0.0.1:8001/auth/logout -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Expected:

```http
HTTP/1.1 204 No Content
```

## Notes

- `.env` is present locally and `.env.example` is committed.
- `.env` must not be committed because it contains the Supabase anon key.
- `requirements.txt` is not currently present in `flyrank-auth-api/`; the assignment guide expects one before final submission.
- Swagger verification is pending until Stage 5.
- GitHub publishing is pending until Stage 6.
