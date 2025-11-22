# 🎯 Quick Reference Card - WeenieHut Bot

## 📍 What You Just Got

A **complete, professional Discord bot** with **70+ commands** across **7 modules**, **fully documented**, and **ready to use today**.

---

## ⚡ 60-Second Setup

```powershell
# 1. Get token from Discord Developer Portal
# 2. Create .env file with token
# 3. Run these commands:

pip install -r requirements.txt
python main.py

# 4. Invite bot to your Discord server
# 5. Type: !ping
```

---

## 🎮 Most Popular Commands

**Fun:**
```
!meme          - Get a random meme
!darkjoke      - Dark humor jokes
!fact          - Random facts
!8ball         - Ask the magic 8 ball
```

**Games:**
```
!roll 2d6      - Roll dice
!rps rock      - Play rock paper scissors
!trivia        - Trivia question
!riddle        - Solve a riddle
```

**Social:**
```
!ship @user1 @user2  - Ship two people
!hug @user           - Give someone a hug
!roast @user         - Playful roast
!dance               - Dance with friends
```

**Utility:**
```
!ping          - Check if bot works
!help          - See all commands
!userinfo      - Get user info
!avatar @user  - Get user's avatar
```

**Admin:**
```
!warn @user reason       - Warn someone
!kick @user reason       - Kick from server
!ban @user reason        - Ban from server
!timeout @user 10 reason - Mute for 10 minutes
```

---

## 📁 File Guide

| File | What It Does |
|------|-------------|
| `main.py` | Start the bot here |
| `config/config.py` | Customize settings |
| `.env` | Store your token (create this!) |
| `cogs/*.py` | 7 command modules |
| `README.md` | Full documentation |
| `QUICKSTART.md` | Quick setup guide |
| `COMMANDS.md` | All commands listed |
| `ADVANCED.md` | How to add features |

---

## 🚨 Common Issues & Fixes

| Problem | Solution |
|---------|----------|
| `Import error` | Run `pip install -r requirements.txt` |
| Bot won't start | Check token in `.env` is correct |
| Commands don't work | Make sure prefix is `!` |
| No permissions | Add bot to server with admin role |

---

## 🔧 Customize In 2 Minutes

Edit `config/config.py`:

```python
BOT_STATUS = "with your feelings ♡"  # Change this
BOT_COLOR = 0xFF1493                  # Change color

# Change prefix in .env:
COMMAND_PREFIX=?                      # Use ? instead of !
```

---

## 🌟 Pro Tips

💡 **Type `!help` in Discord** to see all commands
💡 **Use `@mention`** to mention people
💡 **New commands auto-load** - just add files to `cogs/`
💡 **Embeds look beautiful** - all responses formatted nicely
💡 **Data resets** on bot restart (add database if needed)

---

## 📚 Documentation Files

Start here → `START_HERE.md`
Quick setup → `QUICKSTART.md`  
All commands → `COMMANDS.md`
Deep dive → `README.md`
Expand it → `ADVANCED.md`

---

## 📊 What You Have

```
✅ 70+ Working Commands
✅ 7 Complete Modules
✅ 8+ API Integrations
✅ Full Error Handling
✅ Permission System
✅ Admin Tools
✅ Music System
✅ Game System
✅ Social Commands
✅ Mod Tools
```

---

## 🎯 Next Steps

**TODAY:**
1. Add Discord token to `.env`
2. Run bot with `python main.py`
3. Try commands: `!ping`, `!meme`

**THIS WEEK:**
1. Invite all friends
2. Try all 70+ commands
3. Customize the bot

**THIS MONTH:**
1. Add custom commands
2. Build economy system
3. Create leveling system

---

## 💡 Easy Feature Ideas

- Add weather command
- Create economy/coins
- Build leveling system
- Add welcome messages
- Create reaction roles
- Add scheduled announcements

See `ADVANCED.md` for code examples!

---

## 🔗 Resources

- **Discord.py**: https://discordpy.readthedocs.io/
- **Discord Dev**: https://discord.com/developers/
- **Python**: https://docs.python.org/3/
- **APIs Used**: See `config/config.py`

---

## ✅ You're Ready!

```
Your bot is 100% complete.
Just add your token and run it.
Have fun with your friends! 🎉
```

---

## 📞 Help

**Setup Help:** See `QUICKSTART.md`
**Commands:** See `COMMANDS.md`
**Advanced:** See `ADVANCED.md`
**Architecture:** See `STRUCTURE.md`

---

**Made with ❤️ for you and your friends**

*Status: COMPLETE & READY TO USE ✅*
