#!/bin/bash
# Start the FastAPI server

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Starting CAEA Platform API..."
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
