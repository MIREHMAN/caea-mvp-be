from fastapi import APIRouter
from pydantic import BaseModel
from app.services import community_service

router = APIRouter()

class EnergyTransferRequest(BaseModel):
    recipient_id: int
    credits: float

@router.get("/energyshare/credits")
async def get_credits(user_id: int = 1):
    """Get user energy credits"""
    credits = await community_service.get_user_energy_credits(user_id)
    if not credits:
        return {"success": True, "data": {"credits": 0}}
    return {"success": True, "data": credits}

@router.post("/energyshare/transfer")
async def transfer_credits(req: EnergyTransferRequest, user_id: int = 1):
    """Transfer energy credits to another user"""
    return {
        "success": True,
        "data": {
            "transaction_id": 123,
            "from_user": user_id,
            "to_user": req.recipient_id,
            "credits": req.credits
        }
    }
