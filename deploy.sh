#!/bin/bash

# WeenieHut Bot - Automated Deployment Script
# Run this on your web host to deploy automatically

set -e  # Exit on error

echo "╔════════════════════════════════════════════╗"
echo "║  WeenieHut Bot - Automated Deployment      ║"
echo "╚════════════════════════════════════════════╝"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if running as root
if [ "$EUID" -eq 0 ]; then 
   echo -e "${RED}❌ Don't run this script as root!${NC}"
   exit 1
fi

# Get bot directory
read -p "📁 Enter bot directory path (default: ~/WeenieHutDiscordBot): " BOT_DIR
BOT_DIR=${BOT_DIR:-~/WeenieHutDiscordBot}

# Create directory
if [ ! -d "$BOT_DIR" ]; then
    echo -e "${YELLOW}📂 Creating directory: $BOT_DIR${NC}"
    mkdir -p "$BOT_DIR"
fi

cd "$BOT_DIR"
echo -e "${GREEN}✅ Working in: $BOT_DIR${NC}"
echo ""

# Step 1: Check Python
echo -e "${YELLOW}[1/6] Checking Python...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 not found! Install with: sudo apt-get install python3 python3-pip${NC}"
    exit 1
fi
PYTHON_VERSION=$(python3 --version)
echo -e "${GREEN}✅ $PYTHON_VERSION${NC}"
echo ""

# Step 2: Create Virtual Environment
echo -e "${YELLOW}[2/6] Setting up virtual environment...${NC}"
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✅ Virtual environment created${NC}"
else
    echo -e "${GREEN}✅ Virtual environment already exists${NC}"
fi

source venv/bin/activate
echo -e "${GREEN}✅ Virtual environment activated${NC}"
echo ""

# Step 3: Install Dependencies
echo -e "${YELLOW}[3/6] Installing dependencies...${NC}"
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo -e "${GREEN}✅ Dependencies installed${NC}"
else
    echo -e "${RED}❌ requirements.txt not found!${NC}"
    exit 1
fi
echo ""

# Step 4: Configure .env
echo -e "${YELLOW}[4/6] Configuring .env file...${NC}"
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}Enter your Discord bot token:${NC}"
    read -s DISCORD_TOKEN
    
    cat > .env << EOF
DISCORD_TOKEN=$DISCORD_TOKEN
COMMAND_PREFIX=!
EOF
    
    echo -e "${GREEN}✅ .env file created${NC}"
else
    echo -e "${GREEN}✅ .env file already exists${NC}"
fi
echo ""

# Step 5: Choose Process Manager
echo -e "${YELLOW}[5/6] Choose process manager:${NC}"
echo "1) Systemd (Recommended)"
echo "2) Supervisor"
echo "3) Simple bash script"
read -p "Choose (1-3): " MANAGER_CHOICE

case $MANAGER_CHOICE in
    1)
        echo -e "${YELLOW}Setting up Systemd...${NC}"
        
        # Create service file
        SERVICE_FILE="/tmp/weeniebot.service"
        cat > "$SERVICE_FILE" << EOF
[Unit]
Description=WeenieHut Discord Bot
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
User=$USER
WorkingDirectory=$BOT_DIR
Environment="PATH=$BOT_DIR/venv/bin"
ExecStart=$BOT_DIR/venv/bin/python3 $BOT_DIR/main.py
Restart=always
RestartSec=5
KillMode=process
StandardOutput=journal
StandardError=journal
SyslogIdentifier=weeniebot

[Install]
WantedBy=multi-user.target
EOF
        
        echo -e "${YELLOW}To complete setup, run:${NC}"
        echo "  sudo cp $SERVICE_FILE /etc/systemd/system/weeniebot.service"
        echo "  sudo systemctl daemon-reload"
        echo "  sudo systemctl enable weeniebot"
        echo "  sudo systemctl start weeniebot"
        ;;
    2)
        echo -e "${YELLOW}Setting up Supervisor...${NC}"
        echo "1. Install: sudo apt-get install supervisor"
        echo "2. Copy supervisor.conf: sudo cp supervisor.conf /etc/supervisor/conf.d/weeniebot.conf"
        echo "3. Update paths in the config file"
        echo "4. Run: sudo supervisorctl reread && sudo supervisorctl update && sudo supervisorctl start weeniebot"
        ;;
    3)
        echo -e "${YELLOW}Using bash script...${NC}"
        chmod +x run.sh
        echo -e "${GREEN}✅ Run with: ./run.sh${NC}"
        ;;
esac
echo ""

# Step 6: Test Bot
echo -e "${YELLOW}[6/6] Testing bot connection...${NC}"
echo -e "${YELLOW}Starting bot for 10 seconds to verify...${NC}"
timeout 10 python3 main.py || true
echo ""

echo "╔════════════════════════════════════════════╗"
echo "║       ✅ Deployment Complete!              ║"
echo "╚════════════════════════════════════════════╝"
echo ""
echo -e "${GREEN}Next steps:${NC}"
echo "1. Set up process manager (see above)"
echo "2. Start the bot with your chosen method"
echo "3. Check bot status: ps aux | grep main.py"
echo "4. View logs in Discord"
echo ""
echo -e "${YELLOW}Useful commands:${NC}"
echo "  tail -f bot.log              # View logs"
echo "  ps aux | grep main.py        # Check if running"
echo "  pkill -f main.py             # Stop bot"
echo ""
