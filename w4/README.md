# Week 4 - Auth Login and Protected Routes

This folder contains the Week 4 FlyRank backend assignment for building a FastAPI authentication API with Supabase Auth.

The attached PDF and guide are assignment reference material. This README records the current implementation status and the Swagger UI evidence for the API that has been built locally.

## Project Folder

```text
w4/
|-- HANDS_ON_GUIDE.md
|-- W4 - Auth - Login & protect.pdf
|-- Swagger UI Screenshots/
`-- flyrank-auth-api/
```

## Current Progress

| Stage | Commit | Status |
| --- | --- | --- |
| Stage 0 | `e6dad32` - `Stage 0: setup server and supabase client` | Completed |
| Stage 1 | `4da2fa1` - `Stage 1: signup and login routes working` | Completed |
| Stage 2 | `2813426` - `Stage 2: public route and protected route skeleton` | Completed |
| Stage 3 | `5fdef1b` - `Stage 3: profile route token verification` | Completed |
| Stage 4 | `b7bb365` - `Stage 4: auth dependency and logout endpoint` | Completed |
| Stage 5 | In progress | Swagger UI screenshots added to this README |
| Stage 6 | Pending | GitHub publishing and final documentation |

Current implementation includes:

- `POST /auth/signup`
- `POST /auth/login`
- `POST /auth/logout`
- `GET /public/info`
- `GET /protected/profile`
- `GET /protected/dashboard`
- reusable `HTTPBearer` authentication dependency
- Swagger Authorize support through FastAPI security integration

## Setup

From the API project folder:

```bash
cd flyrank-auth-api
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

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

| Method | Endpoint | Auth Required | Purpose |
| --- | --- | --- | --- |
| `POST` | `/auth/signup` | No | Create a Supabase Auth user |
| `POST` | `/auth/login` | No | Return access and refresh tokens |
| `POST` | `/auth/logout` | Yes | Sign out the authenticated user |
| `GET` | `/public/info` | No | Public test route |
| `GET` | `/protected/profile` | Yes | Return authenticated user id and email |
| `GET` | `/protected/dashboard` | Yes | Return authenticated dashboard message |

## Swagger UI Evidence

Screenshots are stored in:

```text
Swagger UI Screenshots/
```

The screenshots mainly show responses. For clarity, each response screenshot below is preceded by the Swagger UI execute parameters used to produce it.

### 1. Swagger UI

Execute parameter:

```text
Open http://127.0.0.1:8000/docs after starting the FastAPI server.
```

![Swagger UI](<Swagger UI Screenshots/Swagger UI.png>)

### 2. Auth SignUp

Execute parameter:

```json
{
  "email": "mactahoe12@gmail.com",
  "password": "password123"
}
```

![Auth SignUp](<Swagger UI Screenshots/Auth SignUp.png>)

### 3. SignUp Response

Execute parameter:

```json
{
  "email": "mactahoe12@gmail.com",
  "password": "password123"
}
```

Expected status:

```http
201 Created
```

Verified response summary:

```json
{
  "id": "abd445a8-5398-45f4-b702-9080f5710c60",
  "email": "mactahoe12@gmail.com",
  "role": "authenticated",
  "email_verified": true,
  "is_anonymous": false,
  "created_at": "2026-08-24T06:33:53.764886Z"
}
```

![SignUp Response](<Swagger UI Screenshots/SignUp Response.png>)

### 4. Login Response

Execute parameter:

```json
{
  "email": "mactahoe12@gmail.com",
  "password": "password123"
}
```

Expected status:

```http
200 OK
```

Expected response fields:

```json
{
  "access_token": "<JWT access token>",
  "refresh_token": "<refresh token>"
}
```

![Login Response](<Swagger UI Screenshots/Login Response.png>)

### 5. Public Info Response

Execute parameter:

```text
No request body.
No Authorization header required.
```

Expected status:

```http
200 OK
```

Expected response:

```json
{
  "message": "Welcome Stranger! This info is public."
}
```

![public info response](<Swagger UI Screenshots/public info response.png>)

### 6. Protected Profile Response

Execute parameter:

```text
No request body.
Authorization is required for a successful response.
```

Expected unauthenticated status:

```http
403 Forbidden
```

Swagger returns this before a bearer token is authorized because `HTTPBearer()` rejects missing credentials.

![Protected-Profile Response](<Swagger UI Screenshots/Protected-Profile Response.png>)

### 7. HTTPBearer Auth

Execute parameter:

```text
Click Authorize in Swagger UI.
Paste the access_token returned by POST /auth/login.
Authorize using the HTTPBearer security field.
```

Token format:

```text
<access_token>
```

Do not include `Bearer ` when Swagger's HTTPBearer modal asks for the token value.

![HTTPBearer Auth](<Swagger UI Screenshots/HTTPBearer Auth.png>)

### 8. Protected Profile Authorized

Execute parameter:

```text
No request body.
Authorize first with the login access_token in Swagger UI.
```

Expected status:

```http
200 OK
```

Expected response shape:

```json
{
  "id": "abd445a8-5398-45f4-b702-9080f5710c60",
  "email": "mactahoe12@gmail.com"
}
```

![Protected-Profile Authorized](<Swagger UI Screenshots/Protected-Profile Authorized.png>)

### 9. Protected Dashboard Authorized

Execute parameter:

```text
No request body.
Authorize first with the login access_token in Swagger UI.
```

Expected status:

```http
200 OK
```

Expected response shape:

```json
{
  "message": "Welcome to your dashboard! mactahoe12@gmail.com"
}
```

![Protected-Dashboard Authorized](<Swagger UI Screenshots/Protected-Dashboard Authorized.png>)

### 10. Auth LogOut

Execute parameter:

```text
No request body.
Authorize first with the login access_token in Swagger UI.
```

Expected status:

```http
204 No Content
```

![Auth LogOut](<Swagger UI Screenshots/Auth - LogOut.png>)

## Curl Verification Reference

Signup:

```bash
curl -X POST http://127.0.0.1:8000/auth/signup \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"mactahoe12@gmail.com\",\"password\":\"password123\"}"
```

Login:

```bash
curl -X POST http://127.0.0.1:8000/auth/login \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"mactahoe12@gmail.com\",\"password\":\"password123\"}"
```

Public info:

```bash
curl http://127.0.0.1:8000/public/info
```

Protected profile:

```bash
curl http://127.0.0.1:8000/protected/profile \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Protected dashboard:

```bash
curl http://127.0.0.1:8000/protected/dashboard \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

Logout:

```bash
curl -X POST http://127.0.0.1:8000/auth/logout \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Final Notes

- `.env` is used locally and must stay out of git.
- `.env.example` documents the required Supabase environment variables.
- Tokens shown by Swagger or curl should not be committed directly.
- Stage 5 evidence is now documented with screenshots in the requested order.
- Stage 6 still requires final GitHub publishing steps.
