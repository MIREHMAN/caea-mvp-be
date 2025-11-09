from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.core.config import settings
from app.api.v1.endpoints import (
    auth, insights, planner, funds, feed, impact_map, workforce, admin, reports,
    jobs, wallet, greenskills, climatevoice, reputation, campaigns, water_impact, energyshare, community_impact
)
from app.db.session import engine, Base
from app.db.seed_data import seed_database

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("Seeding mock data...")
    seed_database()
    logger.info("Database initialized successfully")
    yield
    # Shutdown
    logger.info("Application shutting down...")

app = FastAPI(
    title="CAEA Platform API",
    description="Climate Action & Equity Agent Platform Backend",
    version="1.0.0",
    lifespan=lifespan
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001","http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Auth Routes
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])

# Agency Routes
app.include_router(insights.router, prefix="/api/v1/agency", tags=["Agency - Insights"])
app.include_router(planner.router, prefix="/api/v1/agency", tags=["Agency - Planner"])
app.include_router(funds.router, prefix="/api/v1/agency", tags=["Agency - Funds"])
app.include_router(feed.router, prefix="/api/v1/agency", tags=["Agency - Feed"])
app.include_router(impact_map.router, prefix="/api/v1/agency", tags=["Agency - Impact Map"])
app.include_router(workforce.router, prefix="/api/v1/agency", tags=["Agency - Workforce"])
app.include_router(admin.router, prefix="/api/v1/agency", tags=["Agency - Admin"])
app.include_router(reports.router, prefix="/api/v1/agency", tags=["Agency - Reports"])

# Community Routes
app.include_router(jobs.router, prefix="/api/v1/community", tags=["Community - Jobs"])
app.include_router(wallet.router, prefix="/api/v1/community", tags=["Community - Wallet"])
app.include_router(greenskills.router, prefix="/api/v1/community", tags=["Community - Green Skills"])
app.include_router(climatevoice.router, prefix="/api/v1/community", tags=["Community - Climate Voice"])
app.include_router(reputation.router, prefix="/api/v1/community", tags=["Community - Reputation"])
app.include_router(campaigns.router, prefix="/api/v1/community", tags=["Community - Campaigns"])
app.include_router(water_impact.router, prefix="/api/v1/community", tags=["Community - Water"])
app.include_router(energyshare.router, prefix="/api/v1/community", tags=["Community - Energy"])
app.include_router(community_impact.community_impact_router, prefix="/api/v1/community", tags=["Community - Impact Map"])

@app.get("/")
async def root():
    return {
        "message": "CAEA Platform API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
