from fastapi import FastAPI, HTTPException, Depends, Response

from app.schemas import AuthRequest
from app.auth import supabase
from app.dependencies import get_current_user


app = FastAPI()


# =========================
# AUTH - SIGNUP
# =========================

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


# =========================
# AUTH - LOGIN
# =========================

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


# =========================
# PUBLIC ROUTE
# =========================

@app.get("/public/info")
def public_info():

    return {
        "message": "Welcome Stranger! This info is public."
    }


# =========================
# PROTECTED PROFILE
# =========================

@app.get("/protected/profile")
def profile(
    current_user=Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "email": current_user.email
    }


# =========================
# PROTECTED DASHBOARD
# =========================

@app.get("/protected/dashboard")
def dashboard(
    current_user=Depends(get_current_user)
):

    return {
        "message": f"Welcome to your dashboard! {current_user.email}"
    }


# =========================
# LOGOUT
# =========================

@app.post("/auth/logout", status_code=204)
def logout(
    current_user=Depends(get_current_user)
):

    supabase.auth.sign_out()

    return Response(status_code=204)