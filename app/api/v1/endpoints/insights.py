from fastapi import APIRouter, Depends
from app.services import agency_service
from app.core.security import verify_agency_role
from app.schemas.auth import TokenData

router = APIRouter()

@router.get("/insights/fai")
async def get_fai_insights(token: TokenData = Depends(verify_agency_role)):
    """Get Fair Action Index (FAI) trend data"""
    data = await agency_service.get_fai_data()
    return {"success": True, "data": data}

@router.get("/insights/engagement")
async def get_engagement(token: TokenData = Depends(verify_agency_role)):
    """Get community engagement metrics"""
    data = await agency_service.get_engagement_data()
    return {"success": True, "data": data}

@router.get("/insights/payouts")
async def get_payouts(token: TokenData = Depends(verify_agency_role)):
    """Get payout analytics"""
    data = await agency_service.get_payout_data()
    return {"success": True, "data": data}

@router.get("/insights/co2")
async def get_co2(token: TokenData = Depends(verify_agency_role)):
    """Get CO2 emission data"""
    data = await agency_service.get_co2_data()
    return {"success": True, "data": data}
