# 🔄 Slash Commands Conversion Guide

Your bot has been partially converted to use slash commands (/) instead of prefix commands (!).

## ✅ Already Converted
- `cogs/fun.py` - ✅ Done
- `cogs/games.py` - ✅ Done
- `cogs/utility.py` - ✅ Done

## ⏳ Need to Convert (Use the pattern below)

### For Remaining Cogs:
- `cogs/moderation.py`
- `cogs/music.py`
- `cogs/creative.py`
- `cogs/interactive.py`

---

## 🔀 Conversion Pattern

### OLD (Prefix Command):
```python
@commands.command(name="mycommand")
async def my_command(self, ctx, arg: str):
    await ctx.send("Hello!")
```

### NEW (Slash Command):
```python
@app_commands.command(name="mycommand", description="What this does")
@app_commands.describe(arg="What this parameter is for")
async def my_command(self, interaction: discord.Interaction, arg: str):
    await interaction.response.send_message("Hello!")
```

---

## 📝 Key Changes

1. **Import statement:**
   ```python
   from discord import app_commands
   ```

2. **Decorator:**
   - OLD: `@commands.command(name="...")`
   - NEW: `@app_commands.command(name="...", description="...")`

3. **Describe parameters:**
   ```python
   @app_commands.describe(param1="Description", param2="Description")
   ```

4. **Function parameter:**
   - OLD: `ctx` (Context)
   - NEW: `interaction` (discord.Interaction)

5. **Send message:**
   - OLD: `await ctx.send(message)`
   - NEW: `await interaction.response.send_message(message)`

6. **For deferred responses (API calls):**
   ```python
   await interaction.response.defer()
   # ... do your work ...
   await interaction.followup.send(message)
   ```

---

## 🔍 Examples by Category

### Simple Command
```python
@app_commands.command(name="ping", description="Check bot latency")
async def ping(self, interaction: discord.Interaction):
    embed = discord.Embed(title="🏓 Pong!", description="Bot is working!")
    await interaction.response.send_message(embed=embed)
```

### Command with Parameter
```python
@app_commands.command(name="greet", description="Greet someone")
@app_commands.describe(name="Person's name")
async def greet(self, interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f"Hello, {name}!")
```

### Command with User Parameter
```python
@app_commands.command(name="userinfo", description="Get user info")
@app_commands.describe(user="User to get info about (optional)")
async def userinfo(self, interaction: discord.Interaction, user: discord.User = None):
    target = user or interaction.user
    await interaction.response.send_message(f"{target.mention}'s info here!")
```

### Command with API Call (needs defer)
```python
@app_commands.command(name="fact", description="Get a random fact")
async def fact(self, interaction: discord.Interaction):
    await interaction.response.defer()
    
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.example.com") as resp:
            data = await resp.json()
            await interaction.followup.send(data["fact"])
```

### Command with Permission Check
```python
@app_commands.command(name="kick", description="Kick a user")
@app_commands.default_permissions(kick_members=True)
@app_commands.describe(member="User to kick")
async def kick_user(self, interaction: discord.Interaction, member: discord.User):
    await interaction.response.send_message(f"Kicked {member.mention}!")
```

---

## 🎯 Quick Conversion Checklist

For each cog, go through:

- [ ] Add `from discord import app_commands` import
- [ ] Change `@commands.command()` to `@app_commands.command()`
- [ ] Add `description="..."` parameter to each command
- [ ] Add `@app_commands.describe(...)` for each parameter
- [ ] Change `ctx` to `interaction`
- [ ] Change `await ctx.send()` to `await interaction.response.send_message()`
- [ ] For API calls: add `await interaction.response.defer()` and use `await interaction.followup.send()`
- [ ] For permissions: use `@app_commands.default_permissions()` instead of `@commands.has_permissions()`

---

## 🔧 Converting Moderation Commands

OLD:
```python
@commands.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick_user(self, ctx, member: discord.Member):
    await ctx.guild.kick(member)
    await ctx.send(f"Kicked {member.mention}")
```

NEW:
```python
@app_commands.command(name="kick", description="Kick a user from server")
@app_commands.default_permissions(kick_members=True)
@app_commands.describe(member="User to kick", reason="Reason for kick")
async def kick_user(self, interaction: discord.Interaction, member: discord.User, reason: str = None):
    # Check if interaction.user has permissions
    if not interaction.user.guild_permissions.kick_members:
        await interaction.response.send_message("❌ You don't have permission!", ephemeral=True)
        return
    
    guild = interaction.guild
    # Get member from user
    member_obj = guild.get_member(member.id)
    if member_obj:
        await guild.kick(member_obj, reason=reason)
        await interaction.response.send_message(f"✅ Kicked {member.mention}")
    else:
        await interaction.response.send_message("❌ User not in server")
```

---

## 💡 Ephemeral Messages (Only user sees them)

```python
# Message only sender can see
await interaction.response.send_message("Secret message!", ephemeral=True)
```

---

## 📚 Full Updated Cogs

I've converted 3 cogs for you:
- ✅ fun.py
- ✅ games.py  
- ✅ utility.py

These use slash commands and are ready to go!

For the remaining cogs, follow the pattern above or let me know and I'll convert them!

---

## 🚀 To Use Your Bot Now

1. Start the bot: `python main.py`
2. Type `/` in Discord
3. See all your commands appear!
4. Much cleaner than prefix commands!

---

## ✨ Benefits of Slash Commands

- 🎯 Built-in parameter validation
- 📝 Autocomplete support
- 🔒 Better permission handling
- 👀 Parameters shown in Discord UI
- ✨ More professional
- 🌍 Works in DMs, servers, threads

---

**Start using slash commands today! 🎉**
