# 🔧 Advanced Hosting - Web API & Monitoring

Run bot alongside a web interface for monitoring and control!

---

## 📡 Option 1: FastAPI with Dashboard

### Setup Web API

Create `web_api.py`:

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import asyncio
import discord
from datetime import datetime
import psutil
import os

app = FastAPI(title="WeenieBot API")

# Store bot reference globally
bot_instance = None

@app.get("/")
async def home():
    return {
        "status": "WeenieBot API Running",
        "version": "1.0",
        "uptime": get_uptime()
    }

@app.get("/status")
async def bot_status():
    if not bot_instance or not bot_instance.user:
        return {"status": "offline", "error": "Bot not connected"}
    
    return {
        "status": "online",
        "bot_name": str(bot_instance.user),
        "bot_id": bot_instance.user.id,
        "guilds": len(bot_instance.guilds),
        "members": sum(g.member_count for g in bot_instance.guilds),
        "commands": len(bot_instance.commands),
        "uptime": get_uptime(),
        "latency": round(bot_instance.latency * 1000)
    }

@app.get("/stats")
async def bot_stats():
    process = psutil.Process(os.getpid())
    return {
        "cpu_percent": process.cpu_percent(interval=1),
        "memory_mb": process.memory_info().rss / 1024 / 1024,
        "memory_percent": process.memory_percent(),
        "uptime_seconds": (datetime.now() - start_time).total_seconds()
    }

@app.get("/guilds")
async def list_guilds():
    if not bot_instance:
        return {"error": "Bot not ready"}
    
    return {
        "count": len(bot_instance.guilds),
        "guilds": [
            {
                "name": g.name,
                "id": g.id,
                "members": g.member_count,
                "owner": str(g.owner)
            }
            for g in bot_instance.guilds
        ]
    }

@app.get("/commands")
async def list_commands():
    if not bot_instance:
        return {"error": "Bot not ready"}
    
    return {
        "total": len(bot_instance.commands),
        "commands": [
            {
                "name": cmd.name,
                "description": cmd.help or "No description"
            }
            for cmd in bot_instance.commands
        ]
    }

def get_uptime():
    return (datetime.now() - start_time).total_seconds()

start_time = datetime.now()

# Run with: uvicorn web_api.py --host 0.0.0.0 --port 8000
```

### Install Dependencies

```bash
pip install fastapi uvicorn psutil
```

### Run Both Bot and API

In a new terminal:

```bash
# Terminal 1: Run bot
python3 main.py

# Terminal 2: Run API
uvicorn web_api:app --host 0.0.0.0 --port 8000
```

### Access Dashboard

Visit: `http://your-host.com:8000/`

Endpoints:
- `GET /` - Status
- `GET /status` - Bot online status
- `GET /stats` - CPU/Memory usage
- `GET /guilds` - List servers
- `GET /commands` - List all commands

---

## 🌐 Option 2: Simple HTML Dashboard

Create `dashboard.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>WeenieBot Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #2C2F33;
            color: #fff;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        .card {
            background: #23272A;
            border-radius: 8px;
            padding: 20px;
            margin: 10px 0;
            border-left: 4px solid #7289DA;
        }
        .stat {
            display: inline-block;
            margin: 10px 20px 10px 0;
        }
        .stat-value {
            font-size: 24px;
            font-weight: bold;
            color: #7289DA;
        }
        .stat-label {
            font-size: 12px;
            color: #999;
        }
        .status-online {
            color: #43B581;
        }
        .status-offline {
            color: #F04747;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 WeenieBot Dashboard</h1>
        
        <div class="card">
            <div id="status"></div>
            <div id="stats"></div>
            <div id="info"></div>
        </div>
    </div>

    <script>
        async function updateDashboard() {
            try {
                const response = await fetch('/api/status');
                const data = await response.json();
                
                document.getElementById('status').innerHTML = `
                    <div class="stat">
                        <div class="stat-value status-${data.status}">● ${data.status.toUpperCase()}</div>
                        <div class="stat-label">Bot Status</div>
                    </div>
                    <div class="stat">
                        <div class="stat-value">${data.latency}ms</div>
                        <div class="stat-label">Latency</div>
                    </div>
                `;
                
                document.getElementById('info').innerHTML = `
                    <p>Bot: ${data.bot_name}</p>
                    <p>Servers: ${data.guilds}</p>
                    <p>Commands: ${data.commands}</p>
                `;
            } catch (error) {
                console.error('Error:', error);
            }
        }
        
        updateDashboard();
        setInterval(updateDashboard, 5000);
    </script>
</body>
</html>
```

---

## 📊 Option 3: PM2 Plus Monitoring

Track bot with PM2+ (commercial):

```bash
# Install PM2
npm install -g pm2

# Link to PM2+
pm2 link <secret_key> <public_key>

# Start with monitoring
pm2 start main.py --name "WeenieBot"

# View dashboard
pm2 web  # Access at localhost:9615
```

Features:
- Real-time CPU/memory
- Crash detection
- Auto-restart
- Email alerts
- Historical stats

---

## 📈 Option 4: Prometheus + Grafana

Professional monitoring (advanced):

### Install

```bash
# Prometheus
wget https://github.com/prometheus/prometheus/releases/download/...
tar xvfz prometheus-*.tar.gz

# Grafana
sudo apt-get install grafana-server
```

### Create Metrics Exporter

```python
from prometheus_client import Counter, Gauge, start_http_server

# Metrics
commands_executed = Counter('commands_executed', 'Total commands executed')
bot_latency = Gauge('bot_latency_ms', 'Bot latency in ms')
connected_guilds = Gauge('connected_guilds', 'Number of guilds')

# Start metrics server
start_http_server(8001)

# In your command handler:
# commands_executed.inc()
```

### Configure Prometheus

Edit `prometheus.yml`:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'weeniebot'
    static_configs:
      - targets: ['localhost:8001']
```

### Access Dashboards

- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000

---

## 🔔 Option 5: Alerting & Notifications

### Email Alerts on Crash

Add to main.py:

```python
import smtplib
from email.mime.text import MIMEText

async def send_alert(subject, message):
    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = 'bot@example.com'
        msg['To'] = 'your-email@example.com'
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login('your-email@gmail.com', 'app_password')
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send alert: {e}")

# In error handler:
@bot.event
async def on_error(event, *args, **kwargs):
    await send_alert("WeenieBot Error", f"Error in {event}")
```

### Discord Webhook Alert

```python
import aiohttp

async def send_webhook_alert(message):
    webhook_url = "your_webhook_url"
    
    async with aiohttp.ClientSession() as session:
        async with session.post(webhook_url, json={"content": message}) as resp:
            return resp.status == 204

# Send to Discord channel
await send_webhook_alert("⚠️ Bot restarted!")
```

---

## 📝 Running Both Web API and Bot

### Option A: Separate Processes

Terminal 1:
```bash
python3 main.py
```

Terminal 2:
```bash
uvicorn web_api:app --host 0.0.0.0 --port 8000
```

### Option B: Single Process with Threading

```python
import threading
from uvicorn import run

# In main.py, add:
def run_web_api():
    run(app, host="0.0.0.0", port=8000)

# Start web API in background
api_thread = threading.Thread(target=run_web_api, daemon=True)
api_thread.start()

# Then start bot normally
bot.run(TOKEN)
```

### Option C: Docker (Advanced)

Create `Dockerfile`:

```dockerfile
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose API port
EXPOSE 8000

# Run bot
CMD ["python3", "main.py"]
```

Run:
```bash
docker build -t weeniebot .
docker run -e DISCORD_TOKEN=your_token weeniebot
```

---

## 🔐 Nginx Reverse Proxy

Secure your API behind Nginx:

```nginx
server {
    listen 80;
    server_name bot.example.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable:
```bash
sudo ln -s /etc/nginx/sites-available/bot /etc/nginx/sites-enabled/
sudo systemctl restart nginx
```

---

## ✅ Production Checklist

- [x] Bot runs 24/7
- [x] Logs are accessible
- [x] Auto-restart on crash
- [x] Monitoring in place
- [x] Alerts set up
- [x] Backups automated
- [x] Updates manageable
- [x] Security hardened

---

**Your bot is now production-ready! 🚀**
