from fastapi import APIRouter, Depends
from app.services import community_service
from app.core.security import verify_community_role
from app.schemas.auth import TokenData

router = APIRouter()

@router.get("/wallet/balance")
async def get_wallet_balance(token: TokenData = Depends(verify_community_role)):
    """Get user wallet balance"""
    wallet = await community_service.get_user_wallet(token.user_id)
    return {"success": True, "data": wallet}

@router.get("/wallet/transactions")
async def get_transactions(token: TokenData = Depends(verify_community_role)):
    """Get wallet transaction history"""
    return {
        "success": True,
        "data": [
            {"date": "2024-01-15", "type": "credit", "amount": 500},
            {"date": "2024-01-10", "type": "debit", "amount": 200}
        ]
    }
