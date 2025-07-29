#!/bin/bash
echo "Starting backend server..."
uvicorn backend.main:app --reload &
sleep 2
echo "Starting monitoring agent..."
python agent/monitor_agent.py
