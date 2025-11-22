# 🚀 QUICK START GUIDE

## Step 1: Get Your Bot Token

1. Go to https://discord.com/developers/applications
2. Click "New Application" 
3. Name it "WeenieHut Bot" (or whatever you want)
4. Go to "Bot" in the left menu
5. Click "Add Bot"
6. Click "Copy" under TOKEN to copy your bot token
7. **Keep this token SECRET!** Never share it!

## Step 2: Enable Required Intents

In Developer Portal:
1. Scroll down to "Intents" section
2. Turn ON:
   - ✅ Message Content Intent
   - ✅ Server Members Intent  
   - ✅ Moderation Intent

## Step 3: Create .env File

1. Open the folder `WeenieHutDiscordBot`
2. Create a new file named `.env` (not `.env.example`)
3. Paste this into it:
```
DISCORD_TOKEN=your_actual_token_here
COMMAND_PREFIX=!
```
4. Replace `your_actual_token_here` with your copied token
5. Save the file

## Step 4: Install Dependencies

Open PowerShell or Command Prompt in the bot folder:
```powershell
pip install -r requirements.txt
```

Wait for it to finish installing all packages.

## Step 5: Invite Bot to Your Server

1. In Developer Portal, go to "OAuth2" → "URL Generator"
2. Select these SCOPES:
   - ✅ bot
3. Select these PERMISSIONS:
   - ✅ Send Messages
   - ✅ Embed Links
   - ✅ Manage Messages
   - ✅ Manage Members
   - ✅ Moderate Members
4. Copy the generated URL at the bottom
5. Paste it in your browser and select your server to invite

## Step 6: Run the Bot!

In PowerShell/Command Prompt:
```powershell
python main.py
```

You should see:
```
✅ YourBotName#0000 is now running!
✨ Synced X command(s) globally
```

## Step 7: Test It!

In your Discord server, try:
```
!ping
!help
!meme
!fact
```

---

## 📋 Command Prefixes

All commands start with `!` (or whatever you set in `COMMAND_PREFIX`)

Examples:
- `!ping` - Check bot is working
- `!meme` - Get a random meme
- `!darkjoke` - Get a dark joke
- `!help` - See all commands
- `!roll 2d6` - Roll dice

## 🆘 Troubleshooting

**Bot doesn't start?**
- Check the error message in console
- Make sure token is correct in `.env`
- Make sure you're in the bot folder

**Bot doesn't respond to commands?**
- Check prefix is `!` (or what you set)
- Make sure bot has Message permissions
- Try `!ping` first

**ImportError?**
- Run: `pip install -r requirements.txt` again
- Make sure Python 3.8+ is installed

**Commands say "not found"?**
- Make sure bot has permissions in the channel
- Check command spelling

---

## 🎮 Must-Try Commands

**Fun:**
- `!meme` - Random meme
- `!darkjoke` - Dark humor
- `!fact` - Random fact
- `!8ball` - Ask a question
- `!roast` - Good-natured roast

**Games:**
- `!roll` - Roll dice
- `!rps` - Rock paper scissors
- `!trivia` - Trivia question
- `!riddle` - Solve a riddle

**Cool Stuff:**
- `!dog` / `!cat` - Cute pictures
- `!quote` - Inspirational quote
- `!ship @user1 @user2` - Ship your friends
- `!userinfo` - User stats

---

## 📝 Adding More Features

The bot auto-loads all Python files in the `cogs/` folder. To add features:

1. Create a new `.py` file in `cogs/`
2. Copy structure from existing cogs
3. Restart the bot - it auto-loads!

---

**Happy botting! Have fun with your new Discord bot! 🎉**
