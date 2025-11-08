from fastapi import APIRouter, Depends
from app.services import community_service
from app.core.security import verify_community_role
from app.schemas.auth import TokenData

router = APIRouter()

@router.get("/water/levels")
async def get_water_levels(token: TokenData = Depends(verify_community_role)):
    """Get water levels by zone"""
    levels = await community_service.get_water_levels()
    return {"success": True, "data": levels}

@router.get("/water/alerts")
async def get_water_alerts(token: TokenData = Depends(verify_community_role)):
    """Get water-related alerts"""
    levels = await community_service.get_water_levels()
    alerts = [w for w in levels if w.get("alert")]
    return {"success": True, "data": alerts}
