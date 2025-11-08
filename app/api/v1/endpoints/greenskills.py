from fastapi import APIRouter
from app.services import community_service

router = APIRouter()

@router.get("/greenskills/courses")
async def get_courses():
    """Get available green skills courses"""
    courses = await community_service.get_green_skills_courses()
    return {"success": True, "data": courses}

@router.get("/greenskills/progress")
async def get_progress(user_id: int = 1):
    """Get user course progress"""
    return {
        "success": True,
        "data": {
            "completed_courses": 2,
            "in_progress": 1,
            "certificates": ["Solar Basics", "Water Conservation"]
        }
    }
