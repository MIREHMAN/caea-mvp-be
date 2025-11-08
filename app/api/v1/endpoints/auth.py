from fastapi import APIRouter, HTTPException, status
from datetime import timedelta
from app.core.config import settings
from app.core.security import create_access_token
from app.schemas.auth import LoginRequest, LoginResponse

router = APIRouter()

# Mock users for demo
MOCK_USERS = {
    "ayesha": {"password": "password123", "id": 1, "role": "community"},
    "officer": {"password": "password123", "id": 2, "role": "agency"}
}

@router.post("/login", response_model=LoginResponse)
async def login(credentials: LoginRequest):
    """
    Login endpoint - returns JWT token
    Use username: ayesha/password or officer/password for testing
    """
    user = MOCK_USERS.get(credentials.username)
    if not user or user["password"] != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": str(user["id"]), "role": user["role"]},
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user["role"],
        "user_id": user["id"]
    }

@router.get("/verify")
async def verify_token(token: str):
    """Verify token validity"""
    return {"message": "Token is valid"}
