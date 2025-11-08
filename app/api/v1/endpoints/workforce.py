from fastapi import APIRouter, Depends
from app.services import agency_service
from app.core.security import verify_agency_role
from app.schemas.auth import TokenData

router = APIRouter()

@router.get("/workforce/list")
async def get_workforce_list(token: TokenData = Depends(verify_agency_role)):
    """Get all workers and contributors"""
    workers = await agency_service.get_top_workers()
    return {"success": True, "data": workers}

@router.get("/workforce/top")
async def get_top_workers(token: TokenData = Depends(verify_agency_role)):
    """Get top contributors"""
    workers = await agency_service.get_top_workers()
    return {"success": True, "data": workers[:5]}
