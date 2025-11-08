from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.services import community_service
from app.core.security import verify_community_role
from app.schemas.auth import TokenData

router = APIRouter()

class ClimateReportRequest(BaseModel):
    title: str
    description: str
    location: str

@router.post("/climatevoice/report")
async def submit_report(req: ClimateReportRequest, token: TokenData = Depends(verify_community_role)):
    """Submit climate voice report"""
    result = await community_service.submit_climate_report(
        token.user_id, req.title, req.description, req.location
    )
    return {"success": True, "data": result}

@router.get("/climatevoice/history")
async def get_history(token: TokenData = Depends(verify_community_role)):
    """Get user report history"""
    return {
        "success": True,
        "data": [
            {"id": 1, "title": "Water shortage in Zone A", "status": "acknowledged"}
        ]
    }
