# 🚀 Advanced Features & Expansion Guide

## 🎯 Feature Overview

Your WeenieHut Discord Bot comes with:

### ✅ Implemented Features
- **7 Cog Modules** (Fun, Games, Utility, Moderation, Music, Creative, Interactive)
- **70+ Commands** ready to use
- **Auto-loading System** - just drop new cogs in `cogs/` folder
- **Error Handling** - graceful error messages
- **Embed-based Responses** - beautiful formatted messages
- **API Integration** - Memes, Jokes, Facts, Trivia, Quotes, Poems, etc.
- **Admin/Mod Tools** - Warning system, timeouts, bans, kicks
- **Interactive Games** - Riddles, trivia, guessing games
- **Music Queue System** - Ready for audio integration

---

## 🛠️ How to Add Features

### Method 1: Add Commands to Existing Cog

Edit an existing `.py` file in `cogs/` and add:

```python
@commands.command(name="mycommand")
async def my_command(self, ctx, arg: str):
    """Do something cool"""
    embed = discord.Embed(
        title="My Feature",
        description=f"You said: {arg}",
        color=0xFF6B9D
    )
    await ctx.send(embed=embed)
```

### Method 2: Create New Cog

Create `cogs/mycog.py`:

```python
import discord
from discord.ext import commands

class MyCog(commands.Cog):
    """My new features"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="newcommand")
    async def new_command(self, ctx):
        """Do something new"""
        await ctx.send("Hello!")

async def setup(bot):
    await bot.add_cog(MyCog(bot))
```

The bot **automatically loads it** on restart!

---

## 🌟 Popular Expansion Ideas

### 1. **Leveling System**
```python
# Add to moderation.py or create levels.py
self.xp = {}  # {user_id: xp_count}

# Award XP for messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    user_id = message.author.id
    self.xp[user_id] = self.xp.get(user_id, 0) + 10
```

### 2. **Economy System**
```python
self.coins = {}  # {user_id: coin_count}

@commands.command(name="balance")
async def check_balance(self, ctx):
    balance = self.coins.get(ctx.author.id, 0)
    await ctx.send(f"💰 Your balance: {balance} coins")
```

### 3. **Daily Rewards**
```python
self.daily_claimed = {}  # {user_id: last_claimed_date}

@commands.command(name="daily")
async def daily_reward(self, ctx):
    user_id = ctx.author.id
    today = datetime.date.today()
    
    if self.daily_claimed.get(user_id) != today:
        self.coins[user_id] = self.coins.get(user_id, 0) + 100
        self.daily_claimed[user_id] = today
        await ctx.send("✅ Claimed 100 coins!")
```

### 4. **Reaction Roles**
```python
@commands.command(name="reactrole")
@commands.has_permissions(administrator=True)
async def setup_reaction_roles(self, ctx):
    msg = await ctx.send("React for roles!")
    await msg.add_reaction("🔴")
    await msg.add_reaction("🟢")
    # Store message ID and roles
```

### 5. **Custom Prefix Per Server**
```python
# Create server_prefixes.py
import json

def get_prefix(bot, message):
    try:
        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        return prefixes.get(str(message.guild.id), "!")
    except:
        return "!"

# In main.py, change:
# bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)
# To:
# bot = commands.Bot(command_prefix=get_prefix, intents=intents)
```

### 6. **Persistent Data (JSON/Database)**
```python
import json

def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

# Use in commands:
data = load_data()
data['users'] = data.get('users', {})
save_data(data)
```

### 7. **Scheduled Tasks**
```python
from discord.ext import tasks

@tasks.loop(hours=24)
async def daily_announcement(self):
    channel = self.bot.get_channel(YOUR_CHANNEL_ID)
    await channel.send("Good morning!")

@daily_announcement.before_loop
async def before_daily_announcement(self):
    await self.bot.wait_until_ready()

# Start in __init__:
def __init__(self, bot):
    self.bot = bot
    self.daily_announcement.start()
```

### 8. **Logging System**
```python
@commands.Cog.listener()
async def on_message_delete(self, message):
    log_channel = self.bot.get_channel(YOUR_LOG_CHANNEL_ID)
    embed = discord.Embed(
        title="Message Deleted",
        description=f"{message.author}: {message.content}",
        color=0xFF0000
    )
    await log_channel.send(embed=embed)
```

### 9. **Ticket System**
```python
@commands.command(name="ticket")
async def create_ticket(self, ctx):
    # Create private channel
    channel = await ctx.guild.create_text_channel(
        name=f"ticket-{ctx.author.name}",
        topic=f"Ticket for {ctx.author.mention}"
    )
    # Add permissions, create embed, etc.
```

### 10. **Fun Mini-Games**
```python
@commands.command(name="connect4")
async def connect_four(self, ctx, opponent: discord.Member):
    """Play connect 4 with someone"""
    game = Connect4Game()
    # Implement game logic with reactions
```

---

## 📡 API Integration Ideas

### Already Integrated
- ✅ Meme API (meme-api.com)
- ✅ Joke API (v2.jokeapi.dev)
- ✅ Facts API (uselessfacts.jsoup.com)
- ✅ Quotes API (api.quotable.io)
- ✅ Trivia API (opentdb.com)
- ✅ Dog Images (dog.ceo)
- ✅ Cat Images (thecatapi.com)

### Easy to Add
- **Weather** - openweathermap.org
- **Crypto** - coingecko.com
- **News** - newsapi.org
- **Wikipedia** - wikipedia.org
- **Urban Dictionary** - urbandictionary.com
- **GIF Search** - giphy.com
- **YouTube Search** - yt-dlp

### Example: Add Weather
```python
import aiohttp

@commands.command(name="weather")
async def weather(self, ctx, *, city):
    api_key = "YOUR_OPENWEATHERMAP_KEY"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            
            embed = discord.Embed(
                title=f"Weather in {city}",
                description=f"{temp}K - {desc}",
                color=0x87CEEB
            )
            await ctx.send(embed=embed)
```

---

## 🗄️ Database Integration

### SQLite (Simple, Built-in)
```python
import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, discord_id INTEGER, coins INTEGER)''')

cursor.execute("INSERT INTO users (discord_id, coins) VALUES (?, ?)", (ctx.author.id, 100))
conn.commit()
```

### MongoDB (Cloud Database)
```python
from pymongo import MongoClient

client = MongoClient("mongodb+srv://user:pass@cluster.mongodb.net/")
db = client["discord_bot"]
users = db["users"]

users.insert_one({"discord_id": ctx.author.id, "coins": 100})
```

---

## 📊 Monitoring & Stats

Add to main.py:

```python
from datetime import datetime

bot.start_time = datetime.now()

@commands.command(name="uptime")
async def uptime(ctx):
    uptime = datetime.now() - bot.start_time
    embed = discord.Embed(
        title="Bot Uptime",
        description=f"{uptime.days}d {uptime.seconds//3600}h",
        color=0x00FF00
    )
    await ctx.send(embed=embed)
```

---

## 🔐 Security Best Practices

✅ **Do This:**
- Keep token in `.env` file
- Use `@commands.has_permissions()` for admin commands
- Validate user input before using in commands
- Check user roles before granting access

❌ **Don't Do This:**
- Hardcode token in code
- Allow anyone to use admin commands
- Trust user input without validation
- Share your `.env` file

```python
# Good security:
@commands.command()
@commands.has_permissions(administrator=True)
@commands.bot_has_permissions(manage_messages=True)
async def admin_command(ctx):
    # Check if user confirmed
    if not await confirm_action(ctx):
        return
    # Do admin stuff
```

---

## 🎨 Custom Embeds & Styling

```python
# Beautiful embed with all features:
embed = discord.Embed(
    title="Epic Title",
    description="Main description",
    color=0xFF6B9D,
    url="https://example.com"
)

embed.set_author(name="Author Name", icon_url="url")
embed.add_field(name="Field 1", value="Value 1", inline=True)
embed.add_field(name="Field 2", value="Value 2", inline=True)
embed.set_image(url="image_url")
embed.set_thumbnail(url="thumb_url")
embed.set_footer(text="Footer text", icon_url="url")

await ctx.send(embed=embed)
```

**Color Codes:**
- `0xFF6B9D` - Pink
- `0xFF0000` - Red
- `0x00FF00` - Green
- `0x0000FF` - Blue
- `0xFFD700` - Gold
- `0x9B59B6` - Purple
- `0xFF4500` - Orange Red
- `0x7289DA` - Discord Blue

---

## ⚡ Performance Tips

1. **Use async/await properly**
   ```python
   # Good - doesn't block
   await asyncio.sleep(1)
   
   # Bad - blocks entire bot
   import time
   time.sleep(1)
   ```

2. **Cache data** to avoid repeated API calls
3. **Use database** instead of JSON for large datasets
4. **Limit API calls** with cooldowns
5. **Use tasks** for recurring operations

---

## 📚 Resources

- **Discord.py Docs**: https://discordpy.readthedocs.io/
- **Discord Developer Portal**: https://discord.com/developers/
- **GitHub Examples**: github.com/Rapptz/discord.py
- **Python Docs**: https://docs.python.org/3/

---

## 🎯 Next Steps

1. Get your bot token and `.env` set up
2. Run the bot: `python main.py`
3. Test the existing commands
4. Try adding one new feature
5. Expand with ideas above
6. Share with friends and iterate!

**Have fun building! Your bot can be as simple or complex as you want it to be! 🚀**
