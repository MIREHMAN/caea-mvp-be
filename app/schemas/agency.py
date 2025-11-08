from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class FAIMetricResponse(BaseModel):
    month: str
    score: float

class WorkerStatsResponse(BaseModel):
    name: str
    jobs_done: int
    reputation: float
    group: str

class TransactionResponse(BaseModel):
    id: int
    type: str
    amount: float
    source_or_destination: str

class ReportResponse(BaseModel):
    id: int
    title: str
    content: str
    submitted_by: str
    status: str

class MapLayerResponse(BaseModel):
    layer_type: str
    data: dict

class SimulateWeatherRequest(BaseModel):
    scenario: str  # drought, flood
    intensity: Optional[float] = 0.5
