# 🎯 HOST DEPLOYMENT QUICK START

## What You Need

1. **Web Host with:**
   - Linux (Ubuntu/Debian recommended)
   - Terminal/SSH access
   - Always running 24/7
   - Python 3.8+

2. **Your Discord Bot Token**
   - From Discord Developer Portal

---

## 🚀 Deploy in 10 Minutes

### Step 1: SSH Into Your Server

```bash
ssh user@your-host.com
```

### Step 2: Download Bot Files

If you have Git:
```bash
git clone https://github.com/your-username/WeenieHutDiscordBot.git
cd WeenieHutDiscordBot
```

Or upload files via SFTP/FileZilla to your home folder.

### Step 3: Run Auto-Deployment

```bash
chmod +x deploy.sh
./deploy.sh
```

This will:
- ✅ Check Python version
- ✅ Create virtual environment
- ✅ Install dependencies
- ✅ Set up `.env` file
- ✅ Configure process manager
- ✅ Test bot

### Step 4: Set Up Process Manager (Choose One)

**Option A: Systemd (Easiest)**
```bash
sudo cp weeniebot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable weeniebot
sudo systemctl start weeniebot
```

**Option B: Bash Script (Simplest)**
```bash
chmod +x run.sh
nohup ./run.sh > bot.log 2>&1 &
```

**Option C: PM2**
```bash
npm install -g pm2
pm2 start main.py --name "WeenieBot"
pm2 save
pm2 startup
```

### Step 5: Verify It's Running

```bash
ps aux | grep main.py
```

You should see your bot process running!

### Step 6: Check Logs

```bash
tail -f bot.log
# Or if using systemd:
sudo journalctl -u weeniebot -f
```

Bot should appear **online in Discord** now! 🎉

---

## 📋 Quick Commands

```bash
# Check if bot is running
ps aux | grep main.py

# View logs
tail -f bot.log

# Stop bot
pkill -f main.py

# Start again
nohup ./run.sh > bot.log 2>&1 &

# Restart (systemd)
sudo systemctl restart weeniebot

# View bot status
sudo systemctl status weeniebot
```

---

## ⚙️ Configuration

Edit `.env` file:
```bash
nano .env
```

Set:
```
DISCORD_TOKEN=your_token_here
COMMAND_PREFIX=!
```

Then restart bot.

---

## 🔍 Troubleshooting

**Bot won't start:**
```bash
# Check error
python3 main.py

# Check token
cat .env | grep DISCORD_TOKEN

# Check dependencies
pip list | grep discord
```

**Can't find bot online:**
- Make sure token is correct
- Verify bot invited to your server
- Check bot has permissions

**Commands don't work:**
- Check prefix (default: `!`)
- Make sure bot has message permissions
- Restart bot: `pkill -f main.py`

---

## 📚 Full Documentation

- `HOSTING.md` - Complete hosting guide
- `DEPLOY_CHECKLIST.md` - Full deployment checklist
- `WEB_HOSTING.md` - Web API & monitoring
- `README.md` - Bot features

---

## 💡 Next Steps

1. ✅ Deploy bot
2. ✅ Verify it works
3. ✅ Invite friends
4. ✅ Try commands
5. ✅ Enjoy 24/7 bot!

---

**Your bot is now running 24/7! 🚀**
