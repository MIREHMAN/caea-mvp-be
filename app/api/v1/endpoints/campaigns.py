from fastapi import APIRouter, Depends
from app.services import community_service
from app.core.security import verify_community_role
from app.schemas.auth import TokenData

router = APIRouter()

@router.get("/campaigns/list")
async def get_campaigns(token: TokenData = Depends(verify_community_role)):
    """Get all campaigns"""
    campaigns = await community_service.get_active_campaigns()
    return {"success": True, "data": campaigns}

@router.get("/campaigns/upcoming")
async def get_upcoming_campaigns(token: TokenData = Depends(verify_community_role)):
    """Get upcoming campaigns"""
    campaigns = await community_service.get_active_campaigns()
    upcoming = [c for c in campaigns if c["status"] == "upcoming"]
    return {"success": True, "data": upcoming}
