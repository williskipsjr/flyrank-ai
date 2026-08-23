from fastapi import FastAPI, HTTPException, Header
from app.schemas import AuthRequest
from app.auth import supabase

app = FastAPI()

@app.post("/auth/signup", status_code=201)
def signup(data: AuthRequest):

    if not data.email or not data.password:
        raise HTTPException(
            status_code=400,
            detail="Email and password required"
        )

    try:
        response = supabase.auth.sign_up(
            {
                "email": data.email,
                "password": data.password
            }
        )

        return response.user

    except Exception as e:
        print("========== SUPABASE SIGNUP ERROR ==========")
        print(type(e).__name__)
        print(str(e))
        print("============================================")

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.post("/auth/login")
def login(data: AuthRequest):

    if not data.email or not data.password:
        raise HTTPException(
            status_code=400,
            detail="Email and password required"
        )

    try:
        response = supabase.auth.sign_in_with_password(
            {
                "email": data.email,
                "password": data.password
            }
        )

        return {
            "access_token": response.session.access_token,
            "refresh_token": response.session.refresh_token
        }

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid login credentials"
        )

    #    
@app.get("/public/info")
def public_info():
    return {
        "message": "Welcome Stranger! This info is public."
    }

@app.get("/protected/profile")
def profile(
    authorization: str = Header(None)
):
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Access Token required"
        )
    try:
        token = authorization.split(" ")[1]
        response = supabase.auth.get_user(token)

        user = response.user

        return {"id": user.id,
                "email": user.email
                }
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

