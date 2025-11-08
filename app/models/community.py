from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.session import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    role = Column(String)  # community, agency
    reputation_score = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    jobs = relationship("Job", back_populates="user")
    wallet = relationship("Wallet", back_populates="user", uselist=False)

class Wallet(Base):
    __tablename__ = "wallets"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    balance = Column(Float, default=0.0)
    credits = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="wallet")

class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    description = Column(Text)
    status = Column(String, default="active")  # active, completed, pending
    reward = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    
    user = relationship("User", back_populates="jobs")

class SkillsCourse(Base):
    __tablename__ = "skills_courses"
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    duration_hours = Column(Float)
    certification_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class ClimateVoiceReport(Base):
    __tablename__ = "climate_voice_reports"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    description = Column(Text)
    location = Column(String)
    status = Column(String, default="submitted")
    created_at = Column(DateTime, default=datetime.utcnow)

class Reputation(Base):
    __tablename__ = "reputations"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    score = Column(Float, default=0.0)
    badges = Column(String)  # JSON string
    created_at = Column(DateTime, default=datetime.utcnow)

class Campaign(Base):
    __tablename__ = "campaigns"
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    status = Column(String, default="upcoming")
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

class WaterLevel(Base):
    __tablename__ = "water_levels"
    
    id = Column(Integer, primary_key=True)
    zone = Column(String, unique=True)
    level_percentage = Column(Float)
    status = Column(String)  # normal, low, critical
    alert = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class EnergyCredit(Base):
    __tablename__ = "energy_credits"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    credits = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
