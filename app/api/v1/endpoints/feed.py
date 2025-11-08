from fastapi import APIRouter
from app.services import agency_service

router = APIRouter()

@router.get("/feed/reports")
async def get_community_reports():
    """Get all community-submitted reports"""
    reports = await agency_service.get_all_reports()
    return {"success": True, "data": reports}
