from fastapi import APIRouter
from app.services import agency_service

router = APIRouter()

@router.get("/funds/ledger")
async def get_funds_ledger():
    """Get transaction ledger"""
    data = await agency_service.get_payout_data()
    return {"success": True, "data": data}

@router.get("/funds/summary")
async def get_funds_summary():
    """Get funding summary"""
    data = await agency_service.get_funds_summary()
    return {"success": True, "data": data}
