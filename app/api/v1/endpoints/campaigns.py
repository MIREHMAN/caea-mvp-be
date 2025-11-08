from fastapi import APIRouter
from app.services import community_service

router = APIRouter()

@router.get("/campaigns/list")
async def get_campaigns():
    """Get all campaigns"""
    campaigns = await community_service.get_active_campaigns()
    return {"success": True, "data": campaigns}

@router.get("/campaigns/upcoming")
async def get_upcoming_campaigns():
    """Get upcoming campaigns"""
    campaigns = await community_service.get_active_campaigns()
    upcoming = [c for c in campaigns if c["status"] == "upcoming"]
    return {"success": True, "data": upcoming}
