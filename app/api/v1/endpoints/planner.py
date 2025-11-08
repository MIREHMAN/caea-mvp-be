from fastapi import APIRouter
from app.services import agency_service
from app.schemas.agency import SimulateWeatherRequest

router = APIRouter()

@router.post("/planner/simulate")
async def simulate_scenario(req: SimulateWeatherRequest):
    """Simulate drought/flood and get AI recommendations"""
    result = await agency_service.simulate_weather(req.scenario, req.intensity)
    return {"success": True, "data": result}
