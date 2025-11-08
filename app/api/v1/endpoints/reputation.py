from fastapi import APIRouter, Depends
from app.services import community_service
from app.core.security import verify_community_role
from app.schemas.auth import TokenData

router = APIRouter()

@router.get("/reputation/score")
async def get_reputation(token: TokenData = Depends(verify_community_role)):
    """Get user reputation score"""
    rep = await community_service.get_user_reputation(token.user_id)
    if not rep:
        return {"success": True, "data": {"score": 50, "badges": []}}
    return {"success": True, "data": rep}

@router.get("/reputation/badges")
async def get_badges(token: TokenData = Depends(verify_community_role)):
    """Get user badges"""
    return {
        "success": True,
        "data": {
            "earned": ["Climate Warrior", "Water Guardian"],
            "next_badge": "Green Entrepreneur"
        }
    }
