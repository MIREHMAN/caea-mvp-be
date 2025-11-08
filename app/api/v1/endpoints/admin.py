from fastapi import APIRouter

router = APIRouter()

@router.get("/admin/settings")
async def get_settings():
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
async def trigger_action(action: str):
    """Trigger system actions"""
    return {"success": True, "message": f"Action '{action}' triggered"}
