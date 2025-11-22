# 🚀 Hosting Guide - Run Bot 24/7 on Web Host

Your Discord bot can run continuously on a web host with terminal access. Here's how!

---

## 📋 Prerequisites

✅ Web host with:
- Linux (Ubuntu/Debian recommended)
- Terminal/SSH access
- Python 3.8+
- 24/7 uptime
- Stable internet

---

## 🚀 Quick Deploy (5 Minutes)

### Step 1: Connect to Your Server

```bash
ssh user@your-host.com
```

### Step 2: Download Bot

Option A - Using Git:
```bash
cd /home/discord
git clone https://github.com/your-repo/WeenieHutDiscordBot.git
cd WeenieHutDiscordBot
```

Option B - Using SFTP:
- Upload all bot files to `/home/discord/WeenieHutDiscordBot`
- Upload via FileZilla or scp

### Step 3: Set Up Environment

```bash
# Create .env with your token
nano .env

# Add these lines:
DISCORD_TOKEN=your_actual_token_here
COMMAND_PREFIX=!

# Save: Ctrl+X, Y, Enter
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Choose Your Process Manager

---

## 🔧 Option 1: Simple Bash Script (Easiest)

### Setup
```bash
chmod +x run.sh
nohup ./run.sh > bot.log 2>&1 &
```

### Check Status
```bash
ps aux | grep main.py
tail -f bot.log
```

### Stop Bot
```bash
pkill -f main.py
```

**Pros:** Simple, no dependencies
**Cons:** Manual restart needed if server reboots

---

## 🔧 Option 2: Systemd Service (Recommended for Linux)

Best for production - auto-starts on reboot!

### Setup

1. **Copy service file**
   ```bash
   sudo cp weeniebot.service /etc/systemd/system/
   ```

2. **Edit service file**
   ```bash
   sudo nano /etc/systemd/system/weeniebot.service
   ```
   - Change `User=discord` to your username
   - Change path `/home/discord/...` to your bot path

3. **Enable service**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable weeniebot
   sudo systemctl start weeniebot
   ```

### Manage Bot

```bash
# Check status
sudo systemctl status weeniebot

# View logs
sudo journalctl -u weeniebot -f

# Restart
sudo systemctl restart weeniebot

# Stop
sudo systemctl stop weeniebot
```

**Pros:** Auto-restart on reboot, easy to manage
**Cons:** Requires sudo access

---

## 🔧 Option 3: PM2 (Best for Node.js users)

If you're familiar with PM2:

### Setup
```bash
npm install -g pm2
pm2 start ecosystem.config.js
pm2 save
pm2 startup
```

### Manage Bot
```bash
pm2 status
pm2 logs WeenieBot
pm2 restart WeenieBot
pm2 stop WeenieBot
```

---

## 🔧 Option 4: Supervisor (Alternative)

### Setup
```bash
sudo apt-get install supervisor
sudo cp supervisor.conf /etc/supervisor/conf.d/weeniebot.conf

# Edit the file
sudo nano /etc/supervisor/conf.d/weeniebot.conf
# Update paths to match your setup

# Apply changes
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start weeniebot
```

### Manage Bot
```bash
sudo supervisorctl status weeniebot
sudo supervisorctl restart weeniebot
sudo supervisorctl stop weeniebot
```

---

## 📊 Comparison Table

| Method | Setup | Auto-Start | Restart | Best For |
|--------|-------|-----------|---------|----------|
| run.sh | ⭐ Easy | ❌ No | Manual | Testing |
| Systemd | ⭐⭐ Medium | ✅ Yes | Auto | Linux VPS |
| PM2 | ⭐⭐⭐ Hard | ✅ Yes | Auto | DevOps |
| Supervisor | ⭐⭐ Medium | ✅ Yes | Auto | Hosting |

---

## 🔍 Monitoring & Troubleshooting

### Check If Bot Is Running

```bash
# Method 1: Check process
ps aux | grep main.py

# Method 2: Check port (if using web API)
netstat -tulpn | grep python

# Method 3: Check Discord
# See if bot appears online in your server
```

### View Logs

```bash
# Systemd
sudo journalctl -u weeniebot -n 100 -f

# PM2
pm2 logs WeenieBot

# Supervisor
tail -f /var/log/weeniebot/out.log

# Bash script
tail -f bot.log
```

### Common Issues

**Bot won't start:**
```bash
# Check token
cat .env

# Check Python
python3 --version

# Check dependencies
pip list | grep discord
```

**Bot crashes after a few hours:**
```bash
# Check memory usage
top -p $(pgrep -f main.py)

# Check logs for errors
tail -100 bot.log
```

**Token not found:**
```bash
# Make sure .env exists
ls -la .env

# Verify token is in .env
cat .env | grep DISCORD_TOKEN
```

---

## 💾 Backup & Updates

### Backup Your Bot

```bash
# Create backup
tar -czf weeniebot_backup.tar.gz WeenieHutDiscordBot/

# Download backup
scp user@host:weeniebot_backup.tar.gz ./
```

### Update Bot Code

```bash
# If using git
cd WeenieHutDiscordBot
git pull origin main

# Restart bot
sudo systemctl restart weeniebot
```

### Update Dependencies

```bash
pip install -r requirements.txt --upgrade
```

---

## 🔐 Security Tips

✅ **Do This:**
- Keep `.env` file secure (don't share)
- Use strong SSH password or SSH keys
- Keep Python updated
- Monitor bot logs for errors
- Use firewall rules

❌ **Don't Do This:**
- Share your `.env` file
- Hardcode token in code
- Run as root
- Disable firewall
- Ignore security updates

---

## 📈 Scaling Up

As bot grows, you might need:

```bash
# Increase resource limits
ulimit -n 4096

# Use multiple instances (PM2)
pm2 start main.py -i 4

# Set up load balancing
# (for multiple servers)

# Monitor with New Relic or Datadog
npm install newrelic
```

---

## 🎯 Quick Command Reference

### Systemd (Recommended)

```bash
sudo systemctl start weeniebot    # Start
sudo systemctl stop weeniebot     # Stop
sudo systemctl restart weeniebot  # Restart
sudo systemctl status weeniebot   # Status
sudo journalctl -u weeniebot -f   # Logs
sudo systemctl enable weeniebot   # Auto-start on reboot
```

### PM2

```bash
pm2 start main.py                 # Start
pm2 stop main.py                  # Stop
pm2 restart main.py               # Restart
pm2 status                         # Status
pm2 logs                           # Logs
pm2 save && pm2 startup           # Save & auto-start
```

### Supervisor

```bash
sudo supervisorctl start weeniebot    # Start
sudo supervisorctl stop weeniebot     # Stop
sudo supervisorctl restart weeniebot  # Restart
sudo supervisorctl status             # Status
tail -f /var/log/weeniebot/out.log   # Logs
```

---

## 🌐 Advanced: Run Web API with Bot

Want to expose bot stats via web?

See `WEB_HOSTING.md` for Flask/FastAPI setup!

---

## ✅ Verification Checklist

- [x] Bot files uploaded
- [x] `.env` created with token
- [x] Dependencies installed
- [x] Process manager configured
- [x] Bot starts successfully
- [x] Bot appears online in Discord
- [x] Commands work
- [x] Auto-restart configured
- [x] Logs accessible
- [x] Can restart without SSH

---

## 🚀 Next Steps

1. Choose your deployment method above
2. Follow the setup instructions
3. Test by restarting server
4. Set up monitoring (optional)
5. Enjoy 24/7 bot!

---

**Your bot will now run 24/7! 🎉**

For questions, check bot logs with the commands above.
