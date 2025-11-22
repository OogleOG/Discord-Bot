# 🚀 Deployment Checklist

## Pre-Deployment

- [ ] Discord bot token created
- [ ] Bot permissions set up in Discord Developer Portal
- [ ] Bot invited to test server
- [ ] Bot works locally with `python main.py`
- [ ] All commands tested
- [ ] `.env` file created with token
- [ ] `requirements.txt` updated with all dependencies

## Server Setup

- [ ] Web host has SSH access
- [ ] Python 3.8+ installed on server
- [ ] SSH key or password configured
- [ ] Upload bot files via Git, SFTP, or SCP
- [ ] Create `.env` file on server with token
- [ ] Run `pip install -r requirements.txt`
- [ ] Test bot starts with `python3 main.py`

## Process Manager Setup (Choose One)

### Systemd (Linux - Recommended)
- [ ] Copy `weeniebot.service` to `/etc/systemd/system/`
- [ ] Edit path in service file to match your setup
- [ ] Run `sudo systemctl daemon-reload`
- [ ] Run `sudo systemctl enable weeniebot`
- [ ] Run `sudo systemctl start weeniebot`
- [ ] Verify: `sudo systemctl status weeniebot`

### Supervisor
- [ ] Install: `sudo apt-get install supervisor`
- [ ] Copy `supervisor.conf` to `/etc/supervisor/conf.d/`
- [ ] Edit paths in config file
- [ ] Run `sudo supervisorctl reread`
- [ ] Run `sudo supervisorctl update`
- [ ] Run `sudo supervisorctl start weeniebot`
- [ ] Verify: `sudo supervisorctl status`

### Bash Script
- [ ] Make executable: `chmod +x run.sh`
- [ ] Run: `nohup ./run.sh > bot.log 2>&1 &`
- [ ] Verify: `ps aux | grep main.py`

## Verification

- [ ] Bot appears online in Discord server
- [ ] Bot responds to test command: `!ping`
- [ ] Bot auto-restarts if crashed
- [ ] Logs are accessible and readable
- [ ] Bot persists after SSH disconnect
- [ ] Bot restarts after server reboot

## Monitoring

- [ ] View logs regularly
- [ ] Check bot status weekly
- [ ] Monitor resource usage
- [ ] Set up alerts (optional)
- [ ] Backup bot files monthly

## Maintenance

- [ ] Keep Discord token secure
- [ ] Update dependencies: `pip install -r requirements.txt --upgrade`
- [ ] Backup configuration and data
- [ ] Monitor for errors in logs
- [ ] Update Python if needed
- [ ] Test updates locally before deploying

## Security

- [ ] `.env` file is in `.gitignore`
- [ ] Token never hardcoded in files
- [ ] Using strong server passwords/keys
- [ ] Firewall configured properly
- [ ] SSH key-based auth used (not password)
- [ ] Regular backups created
- [ ] Server kept updated

---

## Quick Commands Reference

### Check Status
```bash
ps aux | grep main.py
sudo systemctl status weeniebot
sudo supervisorctl status weeniebot
```

### View Logs
```bash
tail -f bot.log
sudo journalctl -u weeniebot -f
tail -f /var/log/weeniebot/out.log
```

### Restart Bot
```bash
sudo systemctl restart weeniebot
sudo supervisorctl restart weeniebot
pkill -f main.py && ./run.sh
```

### Stop Bot
```bash
sudo systemctl stop weeniebot
sudo supervisorctl stop weeniebot
pkill -f main.py
```

### Update Bot
```bash
# Pull latest code
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Restart
sudo systemctl restart weeniebot
```

---

## Troubleshooting

**Bot won't start:**
- Check `.env` has correct token
- Check Python version >= 3.8
- Check dependencies installed
- View error logs

**Bot crashes randomly:**
- Check logs for errors
- Monitor memory/CPU usage
- Check API rate limits
- Increase restart delay

**Can't connect via SSH:**
- Check IP whitelisting
- Verify SSH key permissions
- Check firewall rules
- Try different SSH client

**Commands not working:**
- Verify bot permissions in Discord
- Check command prefix in `.env`
- Confirm bot has Message permissions
- Restart bot

---

## Performance Targets

- **Memory Usage:** < 200MB
- **CPU Usage:** < 5% idle
- **Uptime:** > 99.5%
- **Response Time:** < 100ms
- **Restart Time:** < 5 seconds

---

## Post-Deployment

1. ✅ Verify bot runs 24/7
2. ✅ Test all commands
3. ✅ Share bot with friends
4. ✅ Gather feedback
5. ✅ Add more features as needed
6. ✅ Keep monitoring logs
7. ✅ Update when needed

---

**Status: READY FOR DEPLOYMENT ✅**
