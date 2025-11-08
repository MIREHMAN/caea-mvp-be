import json
import os
from app.db.session import SessionLocal
from app.models.agency import FAIMetric, WorkerStats, Transaction, Report, ImpactMapLayer
from app.models.community import User, Wallet, Job, SkillsCourse, Campaign, WaterLevel, EnergyCredit

def seed_database():
    db = SessionLocal()
    try:
        # Clear existing data
        db.query(FAIMetric).delete()
        db.query(WorkerStats).delete()
        db.query(Transaction).delete()
        db.query(Report).delete()
        db.query(ImpactMapLayer).delete()
        db.query(User).delete()
        db.query(Job).delete()
        db.query(SkillsCourse).delete()
        db.query(Campaign).delete()
        db.query(WaterLevel).delete()
        db.query(EnergyCredit).delete()
        
        # Seed FAI Metrics
        fai_data = [
            FAIMetric(month="Jan", score=72),
            FAIMetric(month="Feb", score=75),
            FAIMetric(month="Mar", score=80),
            FAIMetric(month="Apr", score=78),
            FAIMetric(month="May", score=82),
        ]
        db.add_all(fai_data)
        
        # Seed Worker Stats
        workers_data = [
            WorkerStats(name="Ali Raza", jobs_done=12, reputation=88, group="Top"),
            WorkerStats(name="Sana Noor", jobs_done=5, reputation=67, group="Vulnerable"),
            WorkerStats(name="Haris Khan", jobs_done=18, reputation=95, group="Top"),
            WorkerStats(name="Zainab Ahmed", jobs_done=8, reputation=72, group="Active"),
        ]
        db.add_all(workers_data)
        
        # Seed Transactions
        transactions_data = [
            Transaction(type="inflow", amount=2000, source_or_destination="Donor A"),
            Transaction(type="inflow", amount=5000, source_or_destination="Government Grant"),
            Transaction(type="outflow", amount=500, source_or_destination="Worker 1"),
            Transaction(type="outflow", amount=750, source_or_destination="Worker 2"),
        ]
        db.add_all(transactions_data)
        
        # Seed Reports
        reports_data = [
            Report(title="Water Shortage Zone A", content="Severe water shortage reported", submitted_by="Community", status="pending"),
            Report(title="Air Quality Issue", content="Low air quality in industrial area", submitted_by="Community", status="acknowledged"),
        ]
        db.add_all(reports_data)
        
        # Seed Map Layers
        layers_data = [
            ImpactMapLayer(layer_type="fai", data={"regions": [{"id": 1, "score": 75}]}),
            ImpactMapLayer(layer_type="co2", data={"zones": [{"zone": "A", "level": 120}]}),
            ImpactMapLayer(layer_type="jobs", data={"active": 45, "completed": 120}),
            ImpactMapLayer(layer_type="water_stress", data={"zones": [{"zone": "A", "level": 35}]}),
        ]
        db.add_all(layers_data)
        
        # Seed Users
        users_data = [
            User(name="Ayesha", email="ayesha@example.com", role="community", reputation_score=85),
            User(name="Agency Officer", email="officer@example.com", role="agency", reputation_score=95),
            User(name="Ali", email="ali@example.com", role="community", reputation_score=75),
        ]
        db.add_all(users_data)
        db.commit()
        
        # Seed Wallets
        users = db.query(User).all()
        for user in users:
            wallet = Wallet(user_id=user.id, balance=1000.0, credits=500.0)
            db.add(wallet)
        
        # Seed Jobs
        jobs_data = [
            Job(user_id=1, title="Clean Community Park", description="Clean and maintain the community park", status="active", reward=50),
            Job(user_id=1, title="Plant Trees", description="Plant trees in degraded area", status="completed", reward=75),
            Job(user_id=3, title="Water Conservation", description="Repair water leakage", status="active", reward=100),
        ]
        db.add_all(jobs_data)
        
        # Seed Green Skills Courses
        courses_data = [
            SkillsCourse(title="Solar Basics", description="Learn solar energy fundamentals", duration_hours=10),
            SkillsCourse(title="Water Conservation", description="Water management techniques", duration_hours=8),
            SkillsCourse(title="Green Entrepreneurship", description="Start a green business", duration_hours=15),
        ]
        db.add_all(courses_data)
        
        # Seed Campaigns
        campaigns_data = [
            Campaign(title="Water Tank Installation", description="Install 100 water tanks", status="active", start_date="2024-01-01", end_date="2024-03-01"),
            Campaign(title="Tree Planting Drive", description="Plant 5000 trees", status="upcoming", start_date="2024-02-01", end_date="2024-04-01"),
        ]
        db.add_all(campaigns_data)
        
        # Seed Water Levels
        water_data = [
            WaterLevel(zone="Zone A", level_percentage=35, status="low", alert="Water level below 40%"),
            WaterLevel(zone="Zone B", level_percentage=65, status="normal", alert=None),
            WaterLevel(zone="Zone C", level_percentage=15, status="critical", alert="Critical: Water level below 20%"),
        ]
        db.add_all(water_data)
        
        # Seed Energy Credits
        for user in users:
            energy = EnergyCredit(user_id=user.id, credits=100.0)
            db.add(energy)
        
        db.commit()
        print("[v0] Database seeded successfully with mock data")
    except Exception as e:
        db.rollback()
        print(f"[v0] Error seeding database: {str(e)}")
    finally:
        db.close()
