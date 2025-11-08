from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials

from app.core.config import settings
from app.schemas.auth import TokenData

# Initialize the HTTPBearer scheme
security = HTTPBearer()

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Generate a JWT token with an optional expiry"""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> TokenData:
    """Verify JWT token and return TokenData"""
    token = credentials.credentials
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token: missing subject"
            )
        return TokenData(user_id=int(user_id), role=payload.get("role"))
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

def verify_agency_role(token: TokenData = Depends(verify_token)) -> TokenData:
    """Ensure token belongs to agency role"""
    if token.role != "agency":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Agency role required"
        )
    return token

def verify_community_role(token: TokenData = Depends(verify_token)) -> TokenData:
    """Ensure token belongs to community role"""
    if token.role != "community":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Community role required"
        )
    return token
