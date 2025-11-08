from fastapi import APIRouter, Depends
from app.services import agency_service
from app.core.security import verify_agency_role
from app.schemas.agency import SimulateWeatherRequest
from app.schemas.auth import TokenData

router = APIRouter()

@router.post("/planner/simulate")
async def simulate_scenario(req: SimulateWeatherRequest, token: TokenData = Depends(verify_agency_role)):
    """Simulate drought/flood and get AI recommendations"""
    result = await agency_service.simulate_weather(req.scenario, req.intensity)
    return {"success": True, "data": result}
