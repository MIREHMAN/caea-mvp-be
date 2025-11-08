from app.db.session import SessionLocal
from app.models.community import User, Wallet, Job, SkillsCourse, ClimateVoiceReport, Reputation, Campaign, WaterLevel, EnergyCredit
from sqlalchemy import desc
from typing import List, Dict, Optional

async def get_user_wallet(user_id: int) -> Optional[Dict]:
    db = SessionLocal()
    try:
        wallet = db.query(Wallet).filter(Wallet.user_id == user_id).first()
        if not wallet:
            return None
        return {"balance": wallet.balance, "credits": wallet.credits}
    finally:
        db.close()

async def get_user_jobs(user_id: int) -> List[Dict]:
    db = SessionLocal()
    try:
        jobs = db.query(Job).filter(Job.user_id == user_id).all()
        return [
            {"id": j.id, "title": j.title, "status": j.status, "reward": j.reward}
            for j in jobs
        ]
    finally:
        db.close()

async def update_job_status(job_id: int, status: str) -> Dict:
    db = SessionLocal()
    try:
        job = db.query(Job).filter(Job.id == job_id).first()
        if not job:
            return {"error": "Job not found"}
        job.status = status
        db.commit()
        return {"id": job.id, "status": status}
    finally:
        db.close()

async def get_green_skills_courses() -> List[Dict]:
    db = SessionLocal()
    try:
        courses = db.query(SkillsCourse).all()
        return [
            {"id": c.id, "title": c.title, "description": c.description, "duration_hours": c.duration_hours}
            for c in courses
        ]
    finally:
        db.close()

async def submit_climate_report(user_id: int, title: str, description: str, location: str) -> Dict:
    db = SessionLocal()
    try:
        report = ClimateVoiceReport(user_id=user_id, title=title, description=description, location=location)
        db.add(report)
        db.commit()
        return {"id": report.id, "status": "submitted"}
    finally:
        db.close()

async def get_user_reputation(user_id: int) -> Optional[Dict]:
    db = SessionLocal()
    try:
        rep = db.query(Reputation).filter(Reputation.user_id == user_id).first()
        if not rep:
            return None
        badges = rep.badges.split(",") if rep.badges else []
        return {"score": rep.score, "badges": badges}
    finally:
        db.close()

async def get_active_campaigns() -> List[Dict]:
    db = SessionLocal()
    try:
        campaigns = db.query(Campaign).filter(Campaign.status.in_(["active", "upcoming"])).all()
        return [
            {"id": c.id, "title": c.title, "status": c.status}
            for c in campaigns
        ]
    finally:
        db.close()

async def get_water_levels() -> List[Dict]:
    db = SessionLocal()
    try:
        levels = db.query(WaterLevel).all()
        return [
            {"zone": w.zone, "level_percentage": w.level_percentage, "status": w.status, "alert": w.alert}
            for w in levels
        ]
    finally:
        db.close()

async def get_user_energy_credits(user_id: int) -> Optional[Dict]:
    db = SessionLocal()
    try:
        energy = db.query(EnergyCredit).filter(EnergyCredit.user_id == user_id).first()
        if not energy:
            return None
        return {"credits": energy.credits}
    finally:
        db.close()
