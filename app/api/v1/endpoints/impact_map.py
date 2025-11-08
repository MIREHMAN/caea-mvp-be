from fastapi import APIRouter
from app.services import agency_service

router = APIRouter()

@router.get("/map/layers")
async def get_map_layers():
    """Get map layers (FAI, CO2, jobs, water stress)"""
    layers = await agency_service.get_map_layers()
    return {"success": True, "data": layers}
