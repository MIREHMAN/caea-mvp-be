from app.db.session import SessionLocal
from app.models.agency import FAIMetric, WorkerStats, Transaction, Report, ImpactMapLayer
from app.models.community import User, Job, Wallet
from sqlalchemy import desc
from typing import List, Dict

async def get_fai_data() -> List[Dict]:
    db = SessionLocal()
    try:
        metrics = db.query(FAIMetric).all()
        return [{"month": m.month, "score": m.score} for m in metrics]
    finally:
        db.close()

async def get_engagement_data() -> Dict:
    db = SessionLocal()
    try:
        jobs_active = db.query(Job).filter(Job.status == "active").count()
        jobs_completed = db.query(Job).filter(Job.status == "completed").count()
        return {
            "active_jobs": jobs_active,
            "completed_jobs": jobs_completed,
            "engagement_rate": round((jobs_completed / (jobs_completed + jobs_active + 1)) * 100, 2) if (jobs_completed + jobs_active) > 0 else 0
        }
    finally:
        db.close()

async def get_payout_data() -> List[Dict]:
    db = SessionLocal()
    try:
        transactions = db.query(Transaction).filter(Transaction.type == "outflow").all()
        return [{"amount": t.amount, "destination": t.source_or_destination} for t in transactions]
    finally:
        db.close()

async def get_co2_data() -> List[Dict]:
    db = SessionLocal()
    try:
        layer = db.query(ImpactMapLayer).filter(ImpactMapLayer.layer_type == "co2").first()
        return layer.data if layer else []
    finally:
        db.close()

async def get_top_workers() -> List[Dict]:
    db = SessionLocal()
    try:
        workers = db.query(WorkerStats).order_by(desc(WorkerStats.reputation)).limit(5).all()
        return [{"name": w.name, "jobs_done": w.jobs_done, "reputation": w.reputation} for w in workers]
    finally:
        db.close()

async def get_all_reports() -> List[Dict]:
    db = SessionLocal()
    try:
        reports = db.query(Report).all()
        return [{"id": r.id, "title": r.title, "submitted_by": r.submitted_by, "status": r.status} for r in reports]
    finally:
        db.close()

async def get_map_layers() -> Dict:
    db = SessionLocal()
    try:
        layers = db.query(ImpactMapLayer).all()
        return {layer.layer_type: layer.data for layer in layers}
    finally:
        db.close()

async def simulate_weather(scenario: str, intensity: float = 0.5) -> Dict:
    return {
        "scenario": scenario,
        "intensity": intensity,
        "recommendations": [
            "Increase water tank capacity",
            "Deploy emergency relief teams",
            "Alert community members in affected zones"
        ],
        "affected_zones": ["Zone A", "Zone B"],
        "estimated_impact": f"{intensity * 100}%"
    }

async def get_funds_summary() -> Dict:
    db = SessionLocal()
    try:
        inflows = db.query(Transaction).filter(Transaction.type == "inflow").all()
        outflows = db.query(Transaction).filter(Transaction.type == "outflow").all()
        total_in = sum(t.amount for t in inflows)
        total_out = sum(t.amount for t in outflows)
        return {
            "total_inflow": total_in,
            "total_outflow": total_out,
            "net": total_in - total_out,
            "transaction_count": len(inflows) + len(outflows)
        }
    finally:
        db.close()
