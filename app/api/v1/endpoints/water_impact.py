from fastapi import APIRouter
from app.services import community_service

router = APIRouter()

@router.get("/water/levels")
async def get_water_levels():
    """Get water levels by zone"""
    levels = await community_service.get_water_levels()
    return {"success": True, "data": levels}

@router.get("/water/alerts")
async def get_water_alerts():
    """Get water-related alerts"""
    levels = await community_service.get_water_levels()
    alerts = [w for w in levels if w.get("alert")]
    return {"success": True, "data": alerts}
