from fastapi import APIRouter, Depends
from app.services import agency_service
from app.core.security import verify_agency_role
from app.schemas.auth import TokenData

router = APIRouter()

@router.get("/funds/ledger")
async def get_funds_ledger(token: TokenData = Depends(verify_agency_role)):
    """Get transaction ledger"""
    data = await agency_service.get_payout_data()
    return {"success": True, "data": data}

@router.get("/funds/summary")
async def get_funds_summary(token: TokenData = Depends(verify_agency_role)):
    """Get funding summary"""
    data = await agency_service.get_funds_summary()
    return {"success": True, "data": data}
