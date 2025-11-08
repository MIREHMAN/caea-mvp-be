from fastapi import APIRouter, Depends
from app.services import community_service
from app.core.security import verify_community_role
from app.schemas.auth import TokenData

router = APIRouter()

@router.get("/greenskills/courses")
async def get_courses(token: TokenData = Depends(verify_community_role)):
    """Get available green skills courses"""
    courses = await community_service.get_green_skills_courses()
    return {"success": True, "data": courses}

@router.get("/greenskills/progress")
async def get_progress(token: TokenData = Depends(verify_community_role)):
    """Get user course progress"""
    return {
        "success": True,
        "data": {
            "completed_courses": 2,
            "in_progress": 1,
            "certificates": ["Solar Basics", "Water Conservation"]
        }
    }
