#!/bin/bash

# Activate virtual environment if it exists
if [ -d "venv" ]; then
  source venv/bin/activate
fi

# Start monitoring agent in background
echo "Starting Monitor Agent..."
python monitor_agent.py &

# Start FastAPI backend
echo "Starting FastAPI backend on http://localhost:8000"
uvicorn main:app --reload
