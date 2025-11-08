from fastapi import APIRouter
from app.services import agency_service

router = APIRouter()

@router.get("/insights/fai")
async def get_fai_insights():
    """Get Fair Action Index (FAI) trend data"""
    data = await agency_service.get_fai_data()
    return {"success": True, "data": data}

@router.get("/insights/engagement")
async def get_engagement():
    """Get community engagement metrics"""
    data = await agency_service.get_engagement_data()
    return {"success": True, "data": data}

@router.get("/insights/payouts")
async def get_payouts():
    """Get payout analytics"""
    data = await agency_service.get_payout_data()
    return {"success": True, "data": data}

@router.get("/insights/co2")
async def get_co2():
    """Get CO2 emission data"""
    data = await agency_service.get_co2_data()
    return {"success": True, "data": data}
