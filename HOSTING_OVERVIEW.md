# 🌐 WeenieBot Hosting Guide - Complete Overview

## ✨ What You Now Have

A **production-ready Discord bot** that can run **24/7 on your web host** with:
- ✅ Auto-restart on crashes
- ✅ Easy deployment scripts
- ✅ Multiple hosting options
- ✅ Monitoring & logging
- ✅ Web API support
- ✅ Systemd/PM2/Supervisor support

---

## 🚀 Fastest Way to Get Running (5 Minutes)

### On Your Web Host:

```bash
# 1. SSH into server
ssh user@your-host.com

# 2. Download bot files
git clone <your-repo-url>
cd WeenieHutDiscordBot

# 3. Run deployment script
chmod +x deploy.sh
./deploy.sh

# 4. Follow prompts and choose process manager
# 5. Done! Bot runs 24/7
```

---

## 📁 New Hosting Files Created

| File | Purpose |
|------|---------|
| `run.sh` | Bash script for running bot with auto-restart |
| `weeniebot.service` | Systemd service file (Linux) |
| `ecosystem.config.js` | PM2 configuration |
| `supervisor.conf` | Supervisor configuration |
| `deploy.sh` | Automated deployment script |
| `HOSTING.md` | Complete hosting guide |
| `WEB_HOSTING.md` | Web API & monitoring guide |
| `DEPLOY_CHECKLIST.md` | Full deployment checklist |
| `HOST_QUICKSTART.md` | Quick 10-minute setup |

---

## 🔧 4 Ways to Run Bot 24/7

### Option 1: **Bash Script** (Simplest)

```bash
chmod +x run.sh
nohup ./run.sh > bot.log 2>&1 &
```

**Pros:** No dependencies, easy
**Cons:** No auto-start on reboot

---

### Option 2: **Systemd** (Recommended for Linux)

```bash
sudo cp weeniebot.service /etc/systemd/system/
sudo systemctl enable weeniebot
sudo systemctl start weeniebot
```

**Pros:** Auto-start on reboot, best for servers
**Cons:** Requires Linux

---

### Option 3: **PM2** (Best for DevOps)

```bash
npm install -g pm2
pm2 start main.py --name "WeenieBot"
pm2 startup
pm2 save
```

**Pros:** Professional, great monitoring
**Cons:** Requires Node.js

---

### Option 4: **Supervisor** (Alternative)

```bash
sudo apt-get install supervisor
sudo cp supervisor.conf /etc/supervisor/conf.d/
sudo supervisorctl update
sudo supervisorctl start weeniebot
```

**Pros:** Standard hosting solution
**Cons:** More setup

---

## 📊 Comparison Chart

```
┌─────────────┬──────────┬────────────┬──────────┬──────────┐
│ Method      │ Setup    │ Auto-Start │ Logs     │ Best For │
├─────────────┼──────────┼────────────┼──────────┼──────────┤
│ Bash        │ ⭐       │ ❌         │ File     │ Testing  │
│ Systemd     │ ⭐⭐     │ ✅         │ Journal  │ Linux    │
│ PM2         │ ⭐⭐⭐   │ ✅         │ PM2      │ DevOps   │
│ Supervisor  │ ⭐⭐     │ ✅         │ File     │ Hosting  │
└─────────────┴──────────┴────────────┴──────────┴──────────┘
```

---

## 🎯 Recommended Setup

**For most users on a web host:**

1. Use Bash script (`run.sh`) initially to test
2. Switch to Systemd if on Linux VPS
3. Use PM2 if managing multiple services
4. Use Supervisor if hosting provider uses it

---

## 📈 Hosting Tiers

### Budget ($5-10/month)
- Shared hosting with SSH
- Limited resources
- Use: Bash script or Supervisor

### Standard ($10-25/month)
- VPS (1-2GB RAM)
- Full root access
- Use: Systemd (recommended)

### Professional ($25-100/month)
- VPS (2-4GB RAM)
- Multiple services
- Use: PM2 or Docker

### Enterprise
- Dedicated server
- Kubernetes or Docker Swarm
- Multiple bot instances

---

## ⚡ Quick Start Commands

### Deploy Automatically
```bash
./deploy.sh
```

### Start Bot (Simple)
```bash
nohup ./run.sh > bot.log 2>&1 &
```

### Start Bot (Systemd)
```bash
sudo systemctl start weeniebot
```

### Check Status
```bash
ps aux | grep main.py
sudo systemctl status weeniebot
pm2 status
sudo supervisorctl status weeniebot
```

### View Logs
```bash
tail -f bot.log
sudo journalctl -u weeniebot -f
pm2 logs
tail -f /var/log/weeniebot/out.log
```

### Stop Bot
```bash
pkill -f main.py
sudo systemctl stop weeniebot
pm2 stop main
sudo supervisorctl stop weeniebot
```

### Restart Bot
```bash
pkill -f main.py && nohup ./run.sh &
sudo systemctl restart weeniebot
pm2 restart main
sudo supervisorctl restart weeniebot
```

---

## 🔍 Monitoring Bot Health

### Check If Running
```bash
ps aux | grep main.py
```

### View Logs for Errors
```bash
tail -100 bot.log | grep ERROR
```

### Check Resource Usage
```bash
# Memory
ps aux | grep main.py | awk '{print $6}'

# CPU
top -p $(pgrep -f main.py)
```

### Discord Status
- Look for bot in your server
- Should show as "Online"
- Respond to `!ping` command

---

## 🚨 Troubleshooting

### Bot Won't Start
```bash
# Check error
python3 main.py

# Common issues:
# 1. Token missing/wrong in .env
cat .env

# 2. Dependencies not installed
pip install -r requirements.txt

# 3. Python version too old
python3 --version  # Should be 3.8+
```

### Bot Keeps Crashing
```bash
# View recent logs
tail -50 bot.log

# Check memory
free -h

# Increase restart delay
# Edit run.sh: sleep 30 (instead of 5)
```

### Can't Connect to Server
```bash
# Check SSH access
ssh -v user@host

# Check firewall
sudo ufw status

# Check port availability
netstat -tulpn
```

---

## 📝 Setup Workflow

```
1. Create Discord Bot Token
   ↓
2. Upload Bot Files to Host
   ↓
3. Create .env with Token
   ↓
4. Install Dependencies (pip install -r requirements.txt)
   ↓
5. Test Bot (python3 main.py)
   ↓
6. Choose Process Manager
   ↓
7. Start Bot with Selected Method
   ↓
8. Verify Bot Online in Discord
   ↓
9. Test Commands (!ping, !help, etc)
   ↓
10. Set Up Monitoring (optional)
   ↓
11. Enjoy 24/7 Bot! 🎉
```

---

## 💡 Advanced Features

### Web API Dashboard
```bash
pip install fastapi uvicorn
# See WEB_HOSTING.md for details
```

### Monitoring & Alerts
- PM2 Plus (commercial)
- Prometheus + Grafana
- Email/Discord alerts

### Backup & Recovery
```bash
# Backup bot files
tar -czf bot_backup.tar.gz WeenieHutDiscordBot/

# Download
scp user@host:bot_backup.tar.gz ./

# Restore
tar -xzf bot_backup.tar.gz
```

---

## 🔐 Security Checklist

- [x] `.env` file created with token
- [x] `.env` in `.gitignore` (not on GitHub)
- [x] Use SSH keys (not password)
- [x] Keep token secret
- [x] Use firewall rules
- [x] Regular backups
- [x] Monitor logs for errors
- [x] Update packages regularly

---

## 📚 Documentation Files

| File | What It Covers |
|------|---|
| `HOST_QUICKSTART.md` | 10-minute setup guide |
| `HOSTING.md` | Complete hosting guide with 4 methods |
| `WEB_HOSTING.md` | Web API, dashboards, monitoring |
| `DEPLOY_CHECKLIST.md` | Pre/during/post deployment checklist |
| `deploy.sh` | Automated deployment script |

---

## ✅ Success Indicators

Your bot is working correctly when:
- ✅ Process running: `ps aux | grep main.py` shows output
- ✅ Logs clean: No errors in logs
- ✅ Discord online: Bot shows "Online" in server
- ✅ Commands work: `!ping` gets response
- ✅ Survives reboot: Bot still runs after server restart
- ✅ No crashes: Stays up for hours without restart

---

## 🎯 Next Steps

1. **This week:**
   - Deploy bot to host
   - Verify it runs 24/7
   - Test all commands

2. **This month:**
   - Set up monitoring
   - Create backups
   - Invite friends to bot

3. **Ongoing:**
   - Monitor logs
   - Update packages
   - Add new features

---

## 🆘 Need Help?

1. Check `HOSTING.md` for detailed guide
2. See `DEPLOY_CHECKLIST.md` for step-by-step
3. View logs: `tail -f bot.log`
4. Test locally: `python3 main.py`

---

## 🎉 You're Ready!

Your bot is **fully configured** for 24/7 hosting!

**Next: Follow one of the methods above to deploy**

---

## 📊 Final Summary

```
Current Status:
✅ Bot code: Complete
✅ Deployment scripts: Ready
✅ Hosting guides: Comprehensive
✅ Process managers: 4 options
✅ Monitoring: Available
✅ Backups: Supported

Ready to deploy: YES ✅
```

---

**Happy hosting! Your bot will be online 24/7! 🚀**

*For support, check the documentation files or view logs*
