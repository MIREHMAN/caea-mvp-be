from fastapi import APIRouter
from app.services import community_service

router = APIRouter()

@router.get("/wallet/balance")
async def get_wallet_balance(user_id: int = 1):
    """Get user wallet balance"""
    wallet = await community_service.get_user_wallet(user_id)
    return {"success": True, "data": wallet}

@router.get("/wallet/transactions")
async def get_transactions():
    """Get wallet transaction history"""
    return {
        "success": True,
        "data": [
            {"date": "2024-01-15", "type": "credit", "amount": 500},
            {"date": "2024-01-10", "type": "debit", "amount": 200}
        ]
    }
