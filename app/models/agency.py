from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.session import Base

class FAIMetric(Base):
    __tablename__ = "fai_metrics"
    
    id = Column(Integer, primary_key=True)
    month = Column(String, unique=True)
    score = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class WorkerStats(Base):
    __tablename__ = "worker_stats"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    jobs_done = Column(Integer, default=0)
    reputation = Column(Float, default=50.0)
    group = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True)
    type = Column(String)  # inflow, outflow
    amount = Column(Float)
    source_or_destination = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Report(Base):
    __tablename__ = "reports"
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    submitted_by = Column(String)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)

class ImpactMapLayer(Base):
    __tablename__ = "impact_map_layers"
    
    id = Column(Integer, primary_key=True)
    layer_type = Column(String)  # fai, co2, jobs, water_stress
    data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
