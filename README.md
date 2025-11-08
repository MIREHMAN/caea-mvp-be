# CAEA Platform API

Climate Action & Equity Agent (CAEA) Platform Backend

## Quick Start

### Installation
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### Running the Server
\`\`\`bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
\`\`\`

Or use the convenience script:
\`\`\`bash
bash scripts/run.sh
\`\`\`

### Access Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Authentication

### Test Credentials
- **Community User**: username=`ayesha`, password=`password123`
- **Agency User**: username=`officer`, password=`password123`

### Login
\`\`\`bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d "{\"username\": \"ayesha\", \"password\": \"password123\"}"
\`\`\`

Response includes `access_token` - use in Authorization header:
\`\`\`bash
Authorization: Bearer {access_token}
\`\`\`

## Database

### SQLite (MVP Phase)
- Database file: `caea.db`
- Auto-created on first run
- Mock data automatically seeded

### PostgreSQL Migration
To migrate to PostgreSQL:
1. Update `DATABASE_URL` in `.env`:
   \`\`\`
   DATABASE_URL=postgresql://user:password@localhost/caea
   \`\`\`
2. Install: `pip install psycopg2-binary`
3. Run migrations: `alembic upgrade head`

## Project Structure

\`\`\`
app/
├── main.py                 # FastAPI application entry
├── core/
│   ├── config.py          # Settings and configuration
│   └── security.py        # JWT authentication
├── api/
│   └── v1/
│       └── endpoints/     # All API endpoints
├── models/
│   ├── agency.py          # Agency data models
│   └── community.py       # Community data models
├── schemas/               # Pydantic request/response models
├── services/              # Business logic layer
└── db/
    ├── session.py         # Database connection
    └── seed_data.py       # Mock data seeding
\`\`\`

## API Endpoints

### Agency Endpoints (require `agency` role)
- `GET /api/v1/agency/insights/fai` - FAI trends
- `GET /api/v1/agency/insights/engagement` - Engagement metrics
- `GET /api/v1/agency/insights/payouts` - Payout data
- `GET /api/v1/agency/insights/co2` - CO2 metrics
- `POST /api/v1/agency/planner/simulate` - Weather simulation
- `GET /api/v1/agency/funds/ledger` - Transaction ledger
- `GET /api/v1/agency/funds/summary` - Funding summary
- `GET /api/v1/agency/feed/reports` - Community reports
- `GET /api/v1/agency/map/layers` - Map data layers
- `GET /api/v1/agency/workforce/list` - All workers
- `GET /api/v1/agency/workforce/top` - Top contributors
- `GET /api/v1/agency/admin/settings` - System settings
- `POST /api/v1/agency/admin/trigger` - Trigger actions
- `GET /api/v1/agency/reports/impact` - Impact summary
- `GET /api/v1/agency/reports/download` - Download reports

### Community Endpoints (require `community` role)
- `GET /api/v1/community/jobs/active` - Active jobs
- `GET /api/v1/community/jobs/completed` - Completed jobs
- `PUT /api/v1/community/jobs/{job_id}/status` - Update job status
- `GET /api/v1/community/wallet/balance` - Wallet balance
- `GET /api/v1/community/wallet/transactions` - Transaction history
- `GET /api/v1/community/greenskills/courses` - Available courses
- `GET /api/v1/community/greenskills/progress` - Course progress
- `POST /api/v1/community/climatevoice/report` - Submit report
- `GET /api/v1/community/climatevoice/history` - Report history
- `GET /api/v1/community/reputation/score` - Reputation score
- `GET /api/v1/community/reputation/badges` - Badges
- `GET /api/v1/community/campaigns/list` - All campaigns
- `GET /api/v1/community/campaigns/upcoming` - Upcoming campaigns
- `GET /api/v1/community/water/levels` - Water levels by zone
- `GET /api/v1/community/water/alerts` - Water alerts
- `GET /api/v1/community/energyshare/credits` - Energy credits
- `POST /api/v1/community/energyshare/transfer` - Transfer credits

## Development

### Running Tests
\`\`\`bash
pytest tests/
\`\`\`

### Database Migrations (Future)
With Alembic setup:
\`\`\`bash
alembic revision --autogenerate -m "Description"
alembic upgrade head
\`\`\`

## Next Steps

1. **Frontend Integration**: Connect Next.js frontend to these endpoints
2. **Real-time Updates**: Implement WebSocket support
3. **AI Integration**: Add agent simulation background tasks
4. **Advanced Analytics**: Implement complex reporting features
5. **Geospatial Data**: Add PostGIS support for map features
