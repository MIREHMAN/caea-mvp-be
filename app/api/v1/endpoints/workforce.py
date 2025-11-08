from fastapi import APIRouter
from app.services import agency_service

router = APIRouter()

@router.get("/workforce/list")
async def get_workforce_list():
    """Get all workers and contributors"""
    workers = await agency_service.get_top_workers()
    return {"success": True, "data": workers}

@router.get("/workforce/top")
async def get_top_workers():
    """Get top contributors"""
    workers = await agency_service.get_top_workers()
    return {"success": True, "data": workers[:5]}
