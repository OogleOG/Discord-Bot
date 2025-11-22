import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime

class Utility(commands.Cog):
    """Utility and info commands"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="userinfo", description="Get info about a user")
    @app_commands.describe(member="User to get info about (optional)")
    async def user_info(self, interaction: discord.Interaction, member: discord.User = None):
        """Get info about a user"""
        member = member or interaction.user
        
        embed = discord.Embed(
            title=f"👤 User Info - {member.name}",
            color=0x7289DA
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else None)
        
        embed.add_field(name="Username", value=f"{member.name}#{member.discriminator}", inline=True)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Bot", value="Yes ✅" if member.bot else "No ❌", inline=True)
        embed.add_field(name="Account Created", value=member.created_at.strftime("%Y-%m-%d %H:%M"), inline=True)
        
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="serverinfo", description="Get info about the server")
    async def server_info(self, interaction: discord.Interaction):
        """Get info about the server"""
        guild = interaction.guild
        
        embed = discord.Embed(
            title=f"🏠 Server Info - {guild.name}",
            color=0x7289DA
        )
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        
        embed.add_field(name="Server ID", value=guild.id, inline=True)
        embed.add_field(name="Owner", value=guild.owner.mention if guild.owner else "Unknown", inline=True)
        embed.add_field(name="Created", value=guild.created_at.strftime("%Y-%m-%d %H:%M"), inline=True)
        embed.add_field(name="Members", value=f"{guild.member_count} members", inline=True)
        embed.add_field(name="Channels", value=f"{len(guild.channels)} channels", inline=True)
        embed.add_field(name="Roles", value=f"{len(guild.roles)} roles", inline=True)
        
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="ping", description="Check bot latency")
    async def ping(self, interaction: discord.Interaction):
        """Check bot latency"""
        latency = round(self.bot.latency * 1000)
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"**Latency:** {latency}ms",
            color=0x00FF00 if latency < 100 else 0xFFFF00 if latency < 200 else 0xFF0000
        )
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="avatar", description="Get a user's avatar")
    @app_commands.describe(member="User to get avatar of (optional)")
    async def avatar(self, interaction: discord.Interaction, member: discord.User = None):
        """Get a user's avatar"""
        member = member or interaction.user
        
        embed = discord.Embed(
            title=f"👀 {member.name}'s Avatar",
            color=0x7289DA
        )
        embed.set_image(url=member.avatar.url if member.avatar else None)
        embed.add_field(name="Link", value=f"[Click here]({member.avatar.url if member.avatar else 'N/A'})", inline=False)
        
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="stats", description="Get bot statistics")
    async def bot_stats(self, interaction: discord.Interaction):
        """Get bot statistics"""
        embed = discord.Embed(
            title="📊 Bot Statistics",
            color=0x00B8FF
        )
        embed.add_field(name="Guilds", value=len(self.bot.guilds), inline=True)
        embed.add_field(name="Cogs", value=len(self.bot.cogs), inline=True)
        embed.add_field(name="Users Cached", value=len(self.bot.users), inline=True)
        
        if hasattr(self.bot, 'start_time'):
            uptime = datetime.now() - self.bot.start_time
            embed.add_field(name="Uptime", value=f"{uptime.days}d {uptime.seconds//3600}h", inline=True)
        
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))
