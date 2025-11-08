from fastapi import APIRouter, Depends
from app.core.security import verify_agency_role
from app.schemas.auth import TokenData

router = APIRouter()

@router.get("/admin/settings")
async def get_settings(token: TokenData = Depends(verify_agency_role)):
    """Get system settings"""
    return {
        "success": True,
        "data": {
            "fai_alert_threshold": 65,
            "water_level_critical": 25,
            "co2_target": 50,
            "reward_multiplier": 1.0
        }
    }

@router.post("/admin/trigger")
async def trigger_action(action: str, token: TokenData = Depends(verify_agency_role)):
    """Trigger system actions"""
    return {"success": True, "message": f"Action '{action}' triggered"}
