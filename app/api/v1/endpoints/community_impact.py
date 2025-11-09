from fastapi import APIRouter, Query
from typing import List, Dict
from app.services import community_service

community_impact_router = APIRouter()

# --- Stats cards (Nearby Jobs, Jobs Completed, Water Tank, Community Score) ---
@community_impact_router.get("/stats", response_model=Dict)
async def get_community_stats(zone: str = Query(..., description="Community zone")):
    """
    Return community stats for the dashboard cards
    """
    nearby_jobs = await community_service.get_nearby_jobs_count(zone)
    jobs_completed = await community_service.get_jobs_completed_count(zone)
    water_level = await community_service.get_water_level_by_zone(zone)
    community_score = await community_service.get_community_score(zone)

    return {
        "nearby_jobs": nearby_jobs,
        "jobs_completed": jobs_completed,
        "water_level": water_level,
        "community_score": community_score
    }

# --- Map activities ---
@community_impact_router.get("/activities", response_model=List[Dict])
async def get_community_activities(zone: str = Query(..., description="Community zone")):
    """
    Return community project activities with location info
    """
    activities = await community_service.get_community_activities(zone)
    return activities

# --- Recent projects ---
@community_impact_router.get("/recent-projects", response_model=List[Dict])
async def get_recent_projects(zone: str = Query(..., description="Community zone")):
    """
    Return recently completed community projects
    """
    projects = await community_service.get_recent_projects(zone)
    return projects

# --- Top contributors ---
@community_impact_router.get("/top-contributors", response_model=List[Dict])
async def get_top_contributors(zone: str = Query(..., description="Community zone")):
    """
    Return leading contributors in the community
    """
    contributors = await community_service.get_top_contributors(zone)
    return contributors
