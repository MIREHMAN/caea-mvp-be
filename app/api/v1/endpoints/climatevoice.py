from fastapi import APIRouter, UploadFile, File, Form
from pydantic import BaseModel
from typing import List, Optional
from app.services import community_service

router = APIRouter()

# Request model for submitting report via form data
class ClimateReportResponse(BaseModel):
    id: int
    title: str
    description: str
    location: str
    status: str

# Submit a report (with optional photo)
@router.post("/climatevoice/report", response_model=dict)
async def submit_report(
    title: str = Form(...),
    description: str = Form(...),
    location: str = Form(...),
    photo: Optional[UploadFile] = File(None),
    user_id: int = 1  # Replace with auth dependency later
):
    """
    Submit climate voice report with optional photo.
    """
    # Handle the report submission in service layer
    result = await community_service.submit_climate_report(
        user_id, title, description, location, photo
    )
    return {"success": True, "data": result}

# Get report history and stats
@router.get("/climatevoice/history", response_model=dict)
async def get_history(user_id: int = 1):
    """
    Get user report history, total submitted, resolved, and reputation points.
    """
    reports = await community_service.get_user_reports(user_id)
    
    total_reports = len(reports)
    resolved_reports = len([r for r in reports if r["status"] == "resolved"])
    reputation_points = total_reports * 5  # Example logic
    
    return {
        "success": True,
        "data": {
            "reports": reports,
            "stats": {
                "total_reports": total_reports,
                "resolved_reports": resolved_reports,
                "reputation_points": reputation_points
            }
        }
    }
