from app.db.session import SessionLocal
from app.models.community import (
    User, Wallet, Job, SkillsCourse, ClimateVoiceReport, Reputation,
    Campaign, WaterLevel, EnergyCredit, CommunityActivity
)
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

async def get_job_by_id(job_id: int) -> Optional[Dict]:
    """Fetch a single job by its ID"""
    db = SessionLocal()
    try:
        job = db.query(Job).filter(Job.id == job_id).first()
        if not job:
            return None
        return {
            "id": job.id,
            "user_id": job.user_id,
            "title": job.title,
            "description": job.description,
            "status": job.status,
            "reward": job.reward
        }
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

# ------------------- TOP CARDS -------------------

async def get_nearby_jobs_count(zone: str) -> int:
    db = SessionLocal()
    try:
        return db.query(Job).filter(Job.zone == zone, Job.status != "completed").count()
    finally:
        db.close()

async def get_jobs_completed_count(zone: str, timeframe_days: int = 30) -> int:
    from datetime import datetime, timedelta
    db = SessionLocal()
    try:
        since = datetime.utcnow() - timedelta(days=timeframe_days)
        return db.query(Job).filter(
            Job.zone == zone,
            Job.status == "completed",
            Job.completed_at >= since
        ).count()
    finally:
        db.close()

async def get_water_level_by_zone(zone: str) -> Optional[Dict]:
    db = SessionLocal()
    try:
        level = db.query(WaterLevel).filter(WaterLevel.zone == zone).first()
        if not level:
            return None
        return {
            "zone": level.zone,
            "level_percentage": level.level_percentage,
            "status": level.status,
            "alert": level.alert
        }
    finally:
        db.close()

async def get_community_score(zone: str) -> Optional[Dict]:
    db = SessionLocal()
    try:
        users = db.query(User).filter(User.zone == zone).all()
        if not users:
            return None
        avg_score = sum([u.reputation_score for u in users]) / len(users)
        # Optional: ranking logic could be added here
        return {"score": round(avg_score), "ranking": f"#{int(avg_score)}"}
    finally:
        db.close()

# ------------------- LOCAL IMPACT MAP -------------------

async def get_community_activities(zone: str) -> List[Dict]:
    db = SessionLocal()
    try:
        activities = db.query(CommunityActivity).filter(CommunityActivity.zone == zone).all()
        return [
            {
                "id": a.id,
                "title": a.title,
                "description": a.description,
                "status": a.status,
                "color": a.color,
                "lat": a.lat,
                "lng": a.lng,
                "start_date": a.start_date.isoformat() if a.start_date else None,
                "end_date": a.end_date.isoformat() if a.end_date else None,
                "assigned_users": a.assigned_users,
                "reward": a.reward,
                "impact_metric": a.impact_metric
            }
            for a in activities
        ]
    finally:
        db.close()

# ------------------- RECENT PROJECTS -------------------

async def get_recent_projects(zone: str, limit: int = 5) -> List[Dict]:
    db = SessionLocal()
    try:
        projects = db.query(CommunityActivity).filter(
            CommunityActivity.zone == zone,
            CommunityActivity.status.in_(["completed", "active"])
        ).order_by(CommunityActivity.created_at.desc()).limit(limit).all()
        return [
            {
                "id": p.id,
                "title": p.title,
                "location": p.description,
                "date": p.created_at.date().isoformat(),
                "reward": p.reward,
                "impact_metric": p.impact_metric
            }
            for p in projects
        ]
    finally:
        db.close()

# ------------------- TOP CONTRIBUTORS -------------------

async def get_top_contributors(zone: str, limit: int = 5) -> List[Dict]:
    db = SessionLocal()
    try:
        users = db.query(User).filter(User.zone == zone).order_by(User.reputation_score.desc()).limit(limit).all()
        result = []
        for u in users:
            badges = []
            if u.reputations:
                # Collect badges from latest reputation
                badges = u.reputations[-1].badges if u.reputations[-1].badges else []
            result.append({
                "id": u.id,
                "name": u.name,
                "jobs": len(u.jobs),
                "score": round(u.reputation_score),
                "badge": badges,
                "profile_image": u.profile_image
            })
        return result
    finally:
        db.close()