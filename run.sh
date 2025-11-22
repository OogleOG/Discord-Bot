#!/bin/bash

# WeenieHut Discord Bot - Production Run Script
# Makes bot run continuously and restart on crash

echo "🤖 Starting WeenieHut Discord Bot..."
echo "📅 Start time: $(date)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "❌ ERROR: .env file not found!"
    echo "Please create .env with your DISCORD_TOKEN"
    exit 1
fi

# Check if requirements are installed
if ! python3 -c "import discord" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
fi

# Run bot with auto-restart on crash
while true; do
    echo ""
    echo "▶️  Bot starting at $(date)"
    python3 main.py
    
    EXIT_CODE=$?
    
    if [ $EXIT_CODE -eq 0 ]; then
        echo "✅ Bot stopped cleanly"
        break
    else
        echo "❌ Bot crashed with exit code $EXIT_CODE"
        echo "🔄 Restarting in 5 seconds..."
        sleep 5
    fi
done

echo "👋 Bot stopped"
