import discord
from discord.ext import commands, tasks
from discord import app_commands
import os
import sys
from pathlib import Path
from datetime import datetime
from config.config import *

# Set up bot intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.moderation = True

# Create bot instance with slash commands
bot = commands.Bot(command_prefix="!", intents=intents)

# Track startup time
bot.start_time = datetime.now()

# Bot event: On ready
@bot.event
async def on_ready():
    print(f"\n✅ {bot.user} is now running!")
    print(f"Bot ID: {bot.user.id}")
    print(f"Active in {len(bot.guilds)} guild(s)")
    print("─" * 40)
    
    try:
        synced = await bot.tree.sync()
        print(f"✨ Synced {len(synced)} slash command(s) globally")
        print(f"Use / to access commands!")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")
    
    # Set bot status
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name=BOT_STATUS
        ),
        status=discord.Status.online
    )

# Load all cogs
async def load_cogs():
    cogs_path = Path("cogs")
    for filename in os.listdir(cogs_path):
        if filename.endswith(".py") and not filename.startswith("_"):
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"✅ Loaded cog: {filename[:-3]}")
            except Exception as e:
                print(f"❌ Failed to load cog {filename[:-3]}: {e}")

# Error handler
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"❌ Command not found! Use `{COMMAND_PREFIX}help` for available commands.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"❌ Missing required argument. Check `{COMMAND_PREFIX}help {ctx.command}` for usage.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"❌ You don't have permission to use this command.")
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send(f"❌ I don't have the required permissions to execute this command.")
    else:
        print(f"❌ Unexpected error: {error}")
        await ctx.send(f"❌ An error occurred: {str(error)[:100]}")

# Main function
async def main():
    async with bot:
        await load_cogs()
        await bot.start(DISCORD_TOKEN)

if __name__ == "__main__":
    try:
        import asyncio
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Bot shutting down...")
    except Exception as e:
        print(f"\n❌ Critical error: {e}")
        sys.exit(1)
