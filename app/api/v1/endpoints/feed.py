from fastapi import APIRouter, Depends
from app.services import agency_service
from app.core.security import verify_agency_role
from app.schemas.auth import TokenData

router = APIRouter()

@router.get("/feed/reports")
async def get_community_reports(token: TokenData = Depends(verify_agency_role)):
    """Get all community-submitted reports"""
    reports = await agency_service.get_all_reports()
    return {"success": True, "data": reports}
