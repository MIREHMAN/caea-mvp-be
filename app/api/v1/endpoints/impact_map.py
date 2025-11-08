from fastapi import APIRouter, Depends
from app.services import agency_service
from app.core.security import verify_agency_role
from app.schemas.auth import TokenData

router = APIRouter()

@router.get("/map/layers")
async def get_map_layers(token: TokenData = Depends(verify_agency_role)):
    """Get map layers (FAI, CO2, jobs, water stress)"""
    layers = await agency_service.get_map_layers()
    return {"success": True, "data": layers}
