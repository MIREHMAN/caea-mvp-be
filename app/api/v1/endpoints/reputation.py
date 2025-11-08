from fastapi import APIRouter
from app.services import community_service

router = APIRouter()

@router.get("/reputation/score")
async def get_reputation(user_id: int = 1):
    """Get user reputation score"""
    rep = await community_service.get_user_reputation(user_id)
    if not rep:
        return {"success": True, "data": {"score": 50, "badges": []}}
    return {"success": True, "data": rep}

@router.get("/reputation/badges")
async def get_badges():
    """Get user badges"""
    return {
        "success": True,
        "data": {
            "earned": ["Climate Warrior", "Water Guardian"],
            "next_badge": "Green Entrepreneur"
        }
    }
