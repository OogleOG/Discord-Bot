# 📚 Complete Command Reference

## 🎮 Fun Commands (`fun.py`)
- `!darkmeme` - Send a dark humor meme
- `!meme` - Send a random meme
- `!darkjoke` - Tell a dark humor joke
- `!fact` - Send a random interesting fact
- `!compliment [@user]` - Give a compliment to yourself or someone else
- `!8ball <question>` - Ask the magic 8 ball a question

## 🕹️ Games & Entertainment (`games.py`)
- `!roll [NdN]` - Roll dice (e.g., `!roll 2d6` for two 6-sided dice)
- `!coinflip` - Flip a coin
- `!rps <rock|paper|scissors>` - Play rock paper scissors
- `!riddle` - Get a riddle to solve (30-second timer)
- `!trivia` - Get a trivia question with multiple choice

## 👥 Utility Commands (`utility.py`)
- `!userinfo [@user]` - Get user information
- `!serverinfo` - Get server information
- `!ping` - Check bot latency
- `!avatar [@user]` - Get a user's avatar
- `!stats` - Get bot statistics
- `!help [cog_name]` - Get help about commands

## 😂 Creative & Entertainment (`creative.py`)
- `!quote` - Get an inspirational quote
- `!poem` - Get a random poem
- `!dog` - Get a random dog image
- `!cat` - Get a random cat image
- `!rate <thing>` - Rate something out of 10
- `!reverse <text>` - Reverse text
- `!emojify <text>` - Convert text to emoji
- `!roast [@user]` - Give a good-natured roast
- `!truth` - Get a truth or dare question
- `!guess` - Play number guessing game (7 attempts)
- `!weather <city>` - Check weather (requires API key setup)

## 🎤 Interactive Commands (`interactive.py`)
- `!hug @user` - Give someone a hug
- `!highfive @user` - High five someone
- `!slap @user` - Playfully slap someone
- `!kiss @user` - Send a kiss to someone
- `!punch @user` - Punch someone (playfully)
- `!dance [@user]` - Dance alone or with someone
- `!ship @user1 [@user2]` - Ship two people together
- `!insult [@user]` - Playfully insult someone
- `!choose <option1> <option2> ...` - Bot chooses from options
- `!poll <question>` - Create a yes/no poll
- `!random` - Get a random feature suggestion
- `!flip <text>` - Flip text upside down

## 🎵 Music Commands (`music.py`)
- `!join` - Bot joins your voice channel
- `!leave` - Bot leaves voice channel
- `!play <song_name>` - Add song to queue
- `!queue` - Show current queue
- `!nowplaying` - Show currently playing song
- `!skip` - Skip to next song
- `!pause` - Pause music
- `!resume` - Resume music
- `!clear` - Clear entire queue
- `!shuffle` - Shuffle the queue

## 🛡️ Moderation Commands (`moderation.py`) - *Admin Only*
- `!warn @user [reason]` - Warn a user
- `!warnings [@user]` - Check warnings for a user
- `!clearwarnings @user` - Clear all warnings for a user
- `!kick @user [reason]` - Kick user from server
- `!ban @user [reason]` - Ban user from server
- `!unban <user_id>` - Unban a user
- `!timeout @user <minutes> [reason]` - Timeout a user
- `!untimeout @user` - Remove timeout from user
- `!purge <amount>` - Delete recent messages (max 100)

---

## 📖 How to Use Commands

### Basic Format
```
!command_name [optional_parameters] <required_parameters>
```

### Examples
```
!roll 2d6                    # Roll 2 six-sided dice
!userinfo @john             # Get info about john
!8ball Will I pass my test? # Ask magic 8 ball
!kick @spammer being rude   # Kick with reason
!ship @alice @bob           # Ship two people
```

---

## 🔑 Required Permissions

| Command | Permission Needed |
|---------|------------------|
| `!kick` | Kick Members |
| `!ban` | Ban Members |
| `!unban` | Ban Members |
| `!timeout` | Moderate Members |
| `!purge` | Manage Messages |
| `!warn` | Moderate Members |

---

## 🎨 Customization Tips

### Change Command Prefix
Edit `.env`:
```
COMMAND_PREFIX=?
```
Then use `?ping` instead of `!ping`

### Change Bot Status
Edit `config/config.py`:
```python
BOT_STATUS = "with your feelings ♡"  # Change this
```

### Add API Keys
Edit `config/config.py` and add:
```python
OPENWEATHER_API_KEY = "your_key_here"
```

### Disable Features
Edit `config/config.py`:
```python
FEATURES = {
    "fun": True,
    "memes": True,
    "games": False,  # Disable games
    "moderation": True,
    "music": True,
    "utility": True,
}
```

---

## ⚡ Pro Tips

1. **Mention users**: Use `@username` to mention (e.g., `!userinfo @john`)
2. **Type hints**: Commands show hints if you get the format wrong
3. **Embeds**: Responses are formatted as pretty embeds
4. **Reactions**: Some commands use emoji reactions (polls)
5. **Timeouts**: Some commands wait for your response (riddles, trivia)
6. **Server-specific**: Data like warnings resets per server

---

## 🐛 Command Troubleshooting

**Command says "not found"?**
- Check the command name spelling
- Make sure prefix is correct (`!` by default)

**Bot says "missing permissions"?**
- Give bot proper Discord permissions
- Make sure your role is high enough for mod commands

**API commands failing?**
- Check your internet connection
- API service might be down
- Try again in a few seconds

**Music not playing?**
- Bot needs to be in your voice channel first (`!join`)
- Queue system stores song names (no actual audio playback yet)

---

## 📝 Creating Custom Commands

Add to a cog file:
```python
@commands.command(name="mycommand")
async def my_command(self, ctx, member: discord.Member):
    """My custom command description"""
    embed = discord.Embed(
        title="My Command",
        description=f"Hello {member.mention}!",
        color=0xFF6B9D
    )
    await ctx.send(embed=embed)
```

Restart the bot and use `!mycommand @user`!

---

**Happy commanding! 🎉**
