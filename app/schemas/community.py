from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class WalletResponse(BaseModel):
    balance: float
    credits: float

class JobResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    reward: float

class JobUpdateRequest(BaseModel):
    status: str

class SkillsCourseResponse(BaseModel):
    id: int
    title: str
    description: str
    duration_hours: float

class ReputationResponse(BaseModel):
    score: float
    badges: List[str]

class CampaignResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    start_date: datetime
    end_date: datetime

class WaterLevelResponse(BaseModel):
    zone: str
    level_percentage: float
    status: str
    alert: Optional[str]

class EnergyCreditsResponse(BaseModel):
    credits: float
