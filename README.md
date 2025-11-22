# 🎉 WeenieHut Discord Bot

A feature-rich, expandable Discord bot designed for small friend groups with lots of fun commands and utilities!

## 📋 Features

### 🎮 **Fun & Games**
- `/darkmeme` - Dark humor memes
- `/meme` - Random memes from Reddit
- `/darkjoke` - Dark humor jokes
- `!fact` - Random interesting facts
- `!8ball` - Magic 8 ball predictions
- `!roll` - Roll dice (format: `!roll 2d6`)
- `!coinflip` - Flip a coin
- `!rps` - Play rock paper scissors
- `!riddle` - Solve riddles with a timer
- `!trivia` - Random trivia questions
- `!guess` - Number guessing game
- `!compliment` - Give someone a nice compliment
- `!roast` - Good-natured roasting
- `!truth` - Truth or dare questions

### 😂 **Creative & Entertainment**
- `!quote` - Inspirational quotes
- `!poem` - Random poems
- `!dog` - Random dog images
- `!cat` - Random cat images
- `!rate` - Rate something out of 10
- `!reverse` - Reverse text
- `!emojify` - Convert text to emoji

### 👥 **Utility & Info**
- `!userinfo` - Get user information
- `!serverinfo` - Get server information
- `!ping` - Check bot latency
- `!avatar` - Get user's avatar
- `!stats` - Bot statistics
- `!help` - Help command

### 🛡️ **Moderation** (Admin Only)
- `!warn` - Warn a user
- `!warnings` - Check user warnings
- `!clearwarnings` - Clear user warnings
- `!kick` - Kick a user from the server
- `!ban` - Ban a user from the server
- `!unban` - Unban a user by ID
- `!timeout` - Timeout a user (in minutes)
- `!untimeout` - Remove timeout
- `!purge` - Delete recent messages (max 100)

### 🎵 **Music** (Queue System)
- `!join` - Bot joins your voice channel
- `!leave` - Bot leaves voice channel
- `!play` - Add song to queue
- `!queue` - Show music queue
- `!nowplaying` - Show current song
- `!skip` - Skip to next song
- `!pause` - Pause music
- `!resume` - Resume music
- `!clear` - Clear entire queue
- `!shuffle` - Shuffle the queue

## 🚀 Quick Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation Steps

1. **Clone or download the bot files**
   ```
   cd WeenieHutDiscordBot
   ```

2. **Install required packages**
   ```
   pip install -r requirements.txt
   ```

3. **Create a Discord Bot**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application"
   - Go to "Bot" section and click "Add Bot"
   - Under "TOKEN", click "Copy" to copy your bot token
   - Enable these intents:
     - Message Content Intent
     - Server Members Intent
     - Moderation Intent

4. **Set up environment variables**
   - Rename `.env.example` to `.env`
   - Replace `your_bot_token_here` with your actual bot token:
     ```
     DISCORD_TOKEN=your_actual_token_here
     COMMAND_PREFIX=!
     ```

5. **Invite bot to your server**
   - In Developer Portal, go to OAuth2 → URL Generator
   - Select scopes: `bot`
   - Select permissions:
     - Send Messages
     - Embed Links
     - Manage Messages
     - Manage Members
     - Moderate Members
   - Copy the generated URL and open it to invite the bot

6. **Run the bot**
   ```
   python main.py
   ```

## 📚 Project Structure

```
WeenieHutDiscordBot/
├── main.py                 # Main bot file
├── requirements.txt        # Dependencies
├── .env.example           # Example environment file
├── .env                   # Your actual environment (DO NOT SHARE!)
├── config/
│   └── config.py          # Configuration settings
└── cogs/
    ├── fun.py             # Fun commands
    ├── games.py           # Games and entertainment
    ├── utility.py         # Utility commands
    ├── moderation.py      # Moderation commands
    ├── music.py           # Music queue system
    └── creative.py        # Creative and fun extras
```

## 🔧 Configuration

Edit `config/config.py` to customize:
- Bot token and prefix
- Bot name and status
- Bot color for embeds
- Feature toggles
- API endpoints for memes/jokes

## 🛠️ Development & Expansion

### Adding New Commands

1. Create a new `.py` file in the `cogs/` folder
2. Use the structure from existing cogs:
   ```python
   import discord
   from discord.ext import commands

   class YourCog(commands.Cog):
       def __init__(self, bot):
           self.bot = bot
       
       @commands.command(name="yourcommand")
       async def your_command(self, ctx):
           """Your command description"""
           await ctx.send("Hello!")

   async def setup(bot):
       await bot.add_cog(YourCog(bot))
   ```

3. The bot will automatically load it!

### Popular APIs to Integrate
- **Memes**: meme-api.com
- **Jokes**: v2.jokeapi.dev
- **Facts**: uselessfacts.jsoup.com
- **Quotes**: api.quotable.io
- **Trivia**: opentdb.com
- **Images**: dog.ceo, thecatapi.com
- **Weather**: openweathermap.org (requires API key)
- **Music**: yt-dlp for YouTube integration

## 🐛 Troubleshooting

**Bot isn't responding?**
- Check that `DISCORD_TOKEN` is correct
- Make sure bot has proper permissions in server
- Verify the command prefix is correct

**Import errors?**
- Run `pip install -r requirements.txt` again
- Check Python version is 3.8+

**Commands not working?**
- Ensure bot has message permissions
- Check that embeds are enabled
- Verify command syntax with `!help`

## 📝 Notes

- The music feature is a queue system. For actual audio playback, you'd need `discord.py[voice]` and a music source (YouTube via yt-dlp)
- Dark jokes/memes are intentionally edgy - adjust APIs in config if needed
- All moderation commands require proper permissions
- Bot stores data in memory - data resets on restart (no database)

## 🎨 Customization Ideas

- Add custom commands for your friend group inside jokes
- Create guild-specific settings in database
- Add reaction roles system
- Create a leveling/XP system
- Add fun text-to-speech commands
- Create economy/currency system
- Add reminder/scheduling commands
- Create minigame tournaments

## 📜 License

This is a personal bot project. Feel free to modify and use however you like!

## ❓ Support

If commands aren't working:
1. Check the console output for error messages
2. Verify all required parameters are provided
3. Make sure bot has necessary Discord permissions
4. Check that your Python version is 3.8+

---

**Enjoy your new Discord bot! Add more features whenever inspiration strikes! 🚀**
