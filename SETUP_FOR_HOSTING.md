# 🚀 Hosting Setup Guide - Follow This

This is your **MAIN** guide for hosting the bot on a web host. Follow the steps below exactly.

---

## ⚡ 5-Minute Quick Start

### Step 1: Connect to Your Server
```bash
ssh user@your-host.com
```

### Step 2: Download Bot Files
```bash
cd ~
git clone <your-repo-url>
cd WeenieHutDiscordBot
```

### Step 3: Create `.env` File
```bash
nano .env
```

**Add these lines:**
```
DISCORD_TOKEN=your_actual_bot_token_here
COMMAND_PREFIX=/
```

Save: Press `Ctrl+X`, then `Y`, then `Enter`

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Choose Your Hosting Method (Pick ONE)

---

## 🔧 Hosting Method Comparison

Choose based on your hosting type:

| Hosting Type | Use This | Command |
|---|---|---|
| **Shared Hosting** | Supervisor | `sudo supervisorctl start weeniebot` |
| **Linux VPS** | Systemd (Recommended) | `sudo systemctl start weeniebot` |
| **DevOps/Cloud** | PM2 | `pm2 start main.py` |
| **Testing/Simple** | Bash | `./run.sh` |

---

## 📋 Method 1: Systemd (Recommended for VPS)

**Best for: Linux VPS, DigitalOcean, Linode, AWS**

### Setup:
```bash
# Copy service file
sudo cp weeniebot.service /etc/systemd/system/

# Enable auto-start
sudo systemctl enable weeniebot

# Start bot
sudo systemctl start weeniebot
```

### Check Status:
```bash
sudo systemctl status weeniebot
```

### View Logs:
```bash
sudo journalctl -u weeniebot -f
```

### Restart:
```bash
sudo systemctl restart weeniebot
```

### Stop:
```bash
sudo systemctl stop weeniebot
```

---

## 📋 Method 2: Supervisor (Recommended for Shared Hosting)

**Best for: Shared hosting, cPanel, Plesk**

### Setup:
```bash
# Install supervisor
sudo apt-get update
sudo apt-get install supervisor

# Copy config
sudo cp supervisor.conf /etc/supervisor/conf.d/weeniebot.conf

# Update supervisor
sudo supervisorctl reread
sudo supervisorctl update

# Start bot
sudo supervisorctl start weeniebot
```

### Check Status:
```bash
sudo supervisorctl status weeniebot
```

### View Logs:
```bash
tail -f /var/log/weeniebot/out.log
```

### Restart:
```bash
sudo supervisorctl restart weeniebot
```

### Stop:
```bash
sudo supervisorctl stop weeniebot
```

---

## 📋 Method 3: PM2 (For DevOps/Multiple Services)

**Best for: Managing multiple services, cloud deployments**

### Setup:
```bash
# Install PM2
npm install -g pm2

# Start bot
pm2 start main.py --name "WeenieBot"

# Enable auto-start
pm2 startup
pm2 save
```

### Check Status:
```bash
pm2 status
```

### View Logs:
```bash
pm2 logs WeenieBot
```

### Restart:
```bash
pm2 restart WeenieBot
```

### Stop:
```bash
pm2 stop WeenieBot
```

---

## 📋 Method 4: Bash Script (Simple Testing)

**Best for: Quick testing, simple setups**

### Run:
```bash
chmod +x run.sh
nohup ./run.sh > bot.log 2>&1 &
```

### Check If Running:
```bash
ps aux | grep main.py
```

### View Logs:
```bash
tail -f bot.log
```

### Stop:
```bash
pkill -f main.py
```

---

## ✅ Verify Bot is Running

### Discord Check:
1. Go to your Discord server
2. Look for the bot name in member list
3. Should show as "Online" (green dot)
4. Try `/ping` command - should respond

### Terminal Check:
```bash
# Should show your bot process running
ps aux | grep main.py

# Should show messages in logs
tail bot.log
# or
sudo journalctl -u weeniebot
# or
pm2 logs
```

### Restart Check:
1. Stop the bot using method above
2. Wait 5 seconds
3. Bot should automatically restart
4. Verify it comes back online

---

## 🔍 Troubleshooting

### Bot Won't Start

**Check error message:**
```bash
# If using Systemd:
sudo systemctl status weeniebot

# If using Supervisor:
sudo supervisorctl status weeniebot

# If using Bash:
python main.py
```

**Common fixes:**

1. **"Token invalid"**
   - Check `.env` file has correct token
   - `cat .env`

2. **"Module not found"**
   - Install dependencies: `pip install -r requirements.txt`

3. **"Permission denied"**
   - Make `run.sh` executable: `chmod +x run.sh`

4. **"Port in use"**
   - Kill existing process: `pkill -f main.py`

---

### Bot Keeps Crashing

**View logs for error details:**
```bash
# Systemd logs:
sudo journalctl -u weeniebot -n 50

# Supervisor logs:
tail -50 /var/log/weeniebot/out.log

# Bash logs:
tail -50 bot.log
```

**Common causes:**
- Out of memory: `free -h`
- API rate limited: Wait a few minutes
- Invalid command: Check command syntax
- Permissions: Bot needs proper Discord permissions

---

### Restart Won't Auto-Trigger

**If using Bash script:**
- Edit `run.sh`: change `sleep 5` to `sleep 30`
- Bash script requires manual startup

**For Systemd/Supervisor/PM2:**
- Should auto-restart automatically
- Check logs to see if crashes happening

---

## 📊 File Reference

These files are used for hosting (don't delete!):

- `run.sh` - Bash startup script
- `weeniebot.service` - Systemd configuration
- `supervisor.conf` - Supervisor configuration
- `ecosystem.config.js` - PM2 configuration
- `.env` - Your token (YOU CREATE THIS)
- `main.py` - Bot code
- `requirements.txt` - Dependencies
- `cogs/` - Bot command modules
- `config/` - Bot configuration

---

## 🎯 Setup Checklist

- [ ] SSH into server
- [ ] Downloaded bot files
- [ ] Created `.env` with token
- [ ] Ran `pip install -r requirements.txt`
- [ ] Chose hosting method (Systemd/Supervisor/PM2/Bash)
- [ ] Set up using method above
- [ ] Started bot
- [ ] Verified bot online in Discord
- [ ] Tested `/ping` command
- [ ] Checked logs for errors

---

## 🎉 You're Done!

Your bot is now running 24/7!

**Next time you restart the server, the bot will:**
- ✅ Auto-start automatically (Systemd/Supervisor/PM2 only)
- ✅ Reconnect to Discord
- ✅ Be ready to use

---

## 📞 Quick Commands Reference

| Task | Command |
|------|---------|
| **Connect** | `ssh user@host.com` |
| **Check running** | `ps aux \| grep main.py` |
| **View logs** | `tail -f bot.log` or `sudo journalctl -u weeniebot -f` |
| **Stop bot** | `pkill -f main.py` or `sudo systemctl stop weeniebot` |
| **Restart bot** | `sudo systemctl restart weeniebot` |
| **Check status** | `sudo systemctl status weeniebot` |

---

**That's all you need! Your bot is hosting-ready! 🚀**
