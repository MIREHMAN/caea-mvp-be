from fastapi import APIRouter
from app.services import community_service
from app.schemas.community import JobUpdateRequest

router = APIRouter()

@router.get("/jobs/active")
async def get_active_jobs(user_id: int = 1):
    """Get active jobs for user"""
    jobs = await community_service.get_user_jobs(user_id)
    active = [j for j in jobs if j["status"] == "active"]
    return {"success": True, "data": active}

@router.get("/jobs/completed")
async def get_completed_jobs(user_id: int = 1):
    """Get completed jobs for user"""
    jobs = await community_service.get_user_jobs(user_id)
    completed = [j for j in jobs if j["status"] == "completed"]
    return {"success": True, "data": completed}

@router.put("/jobs/{job_id}/status")
async def update_job_status(job_id: int, req: JobUpdateRequest):
    """Update job status"""
    result = await community_service.update_job_status(job_id, req.status)
    return {"success": True, "data": result}
