from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.services import community_service
from app.core.security import verify_community_role
from app.schemas.auth import TokenData

router = APIRouter()

class EnergyTransferRequest(BaseModel):
    recipient_id: int
    credits: float

@router.get("/energyshare/credits")
async def get_credits(token: TokenData = Depends(verify_community_role)):
    """Get user energy credits"""
    credits = await community_service.get_user_energy_credits(token.user_id)
    if not credits:
        return {"success": True, "data": {"credits": 0}}
    return {"success": True, "data": credits}

@router.post("/energyshare/transfer")
async def transfer_credits(req: EnergyTransferRequest, token: TokenData = Depends(verify_community_role)):
    """Transfer energy credits to another user"""
    return {
        "success": True,
        "data": {
            "transaction_id": 123,
            "from_user": token.user_id,
            "to_user": req.recipient_id,
            "credits": req.credits
        }
    }
