from fastapi import APIRouter
from pydantic import BaseModel
from app.services import community_service

router = APIRouter()

class ClimateReportRequest(BaseModel):
    title: str
    description: str
    location: str

@router.post("/climatevoice/report")
async def submit_report(req: ClimateReportRequest, user_id: int = 1):
    """Submit climate voice report"""
    result = await community_service.submit_climate_report(
        user_id, req.title, req.description, req.location
    )
    return {"success": True, "data": result}

@router.get("/climatevoice/history")
async def get_history():
    """Get user report history"""
    return {
        "success": True,
        "data": [
            {"id": 1, "title": "Water shortage in Zone A", "status": "acknowledged"}
        ]
    }
