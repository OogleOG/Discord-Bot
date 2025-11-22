import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime, timedelta

class Moderation(commands.Cog):
    """Moderation commands for server management"""
    
    def __init__(self, bot):
        self.bot = bot
        self.warnings = {}  # {user_id: {guild_id: count}}
    
    async def check_mod_role(self, member):
        """Check if user has mod permissions"""
        return member.guild_permissions.administrator or member.guild_permissions.moderate_members
    
    @app_commands.command(name="warn", description="Warn a user")
    @app_commands.describe(member="User to warn", reason="Reason for warning")
    @app_commands.default_permissions(moderate_members=True)
    async def warn_user(self, interaction: discord.Interaction, member: discord.User, reason: str = "No reason provided"):
        """Warn a user"""
        # Check if user has permissions
        if not interaction.user.guild_permissions.moderate_members:
            await interaction.response.send_message("❌ You don't have permission!", ephemeral=True)
            return
        
        if member == interaction.user:
            await interaction.response.send_message("❌ You can't warn yourself!", ephemeral=True)
            return
        
        if member.bot:
            await interaction.response.send_message("❌ You can't warn a bot!", ephemeral=True)
            return
        
        key = f"{member.id}_{interaction.guild.id}"
        if key not in self.warnings:
            self.warnings[key] = 0
        
        self.warnings[key] += 1
        
        embed = discord.Embed(
            title="⚠️ User Warned",
            color=0xFFFF00
        )
        embed.add_field(name="User", value=member.mention, inline=True)
        embed.add_field(name="Moderator", value=interaction.user.mention, inline=True)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.add_field(name="Warnings", value=f"{self.warnings[key]}/3", inline=True)
        
        await interaction.response.send_message(embed=embed)
        
        try:
            await member.send(f"You have been warned in **{interaction.guild.name}** for: {reason}\nWarnings: {self.warnings[key]}/3")
        except:
            pass
    
    @app_commands.command(name="clearwarnings", description="Clear warnings for a user")
    @app_commands.describe(member="User to clear warnings for")
    @app_commands.default_permissions(moderate_members=True)
    async def clear_warnings(self, interaction: discord.Interaction, member: discord.User):
        """Clear warnings for a user"""
        if not interaction.user.guild_permissions.moderate_members:
            await interaction.response.send_message("❌ You don't have permission!", ephemeral=True)
            return
        
        key = f"{member.id}_{interaction.guild.id}"
        if key in self.warnings:
            self.warnings[key] = 0
            await interaction.response.send_message(f"✅ Cleared warnings for {member.mention}")
        else:
            await interaction.response.send_message(f"❌ {member.mention} has no warnings")
    
    @app_commands.command(name="warnings", description="Check warnings for a user")
    @app_commands.describe(member="User to check (optional)")
    async def check_warnings(self, interaction: discord.Interaction, member: discord.User = None):
        """Check warnings for a user"""
        member = member or interaction.user
        key = f"{member.id}_{interaction.guild.id}"
        warnings_count = self.warnings.get(key, 0)
        
        embed = discord.Embed(
            title="⚠️ Warning Count",
            color=0xFFFF00
        )
        embed.add_field(name="User", value=member.mention, inline=True)
        embed.add_field(name="Warnings", value=f"{warnings_count}/3", inline=True)
        
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="kick", description="Kick a user from the server")
    @app_commands.describe(member="User to kick", reason="Reason for kick")
    @app_commands.default_permissions(kick_members=True)
    async def kick_user(self, interaction: discord.Interaction, member: discord.User, reason: str = "No reason provided"):
        """Kick a user from the server"""
        if not interaction.user.guild_permissions.kick_members:
            await interaction.response.send_message("❌ You don't have permission!", ephemeral=True)
            return
        
        if member == interaction.user:
            await interaction.response.send_message("❌ You can't kick yourself!", ephemeral=True)
            return
        
        if member.bot:
            await interaction.response.send_message("❌ You can't kick a bot!", ephemeral=True)
            return
        
        guild_member = interaction.guild.get_member(member.id)
        if not guild_member:
            await interaction.response.send_message("❌ User not in server!", ephemeral=True)
            return
        
        if guild_member.top_role >= interaction.user.top_role:
            await interaction.response.send_message("❌ You can't kick someone with equal or higher role!", ephemeral=True)
            return
        
        try:
            await member.send(f"You have been kicked from **{interaction.guild.name}** for: {reason}")
        except:
            pass
        
        await interaction.guild.kick(guild_member, reason=reason)
        
        embed = discord.Embed(
            title="🦶 User Kicked",
            color=0xFF6B6B
        )
        embed.add_field(name="User", value=member.mention, inline=True)
        embed.add_field(name="Moderator", value=interaction.user.mention, inline=True)
        embed.add_field(name="Reason", value=reason, inline=False)
        
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="ban", description="Ban a user from the server")
    @app_commands.describe(member="User to ban", reason="Reason for ban")
    @app_commands.default_permissions(ban_members=True)
    async def ban_user(self, interaction: discord.Interaction, member: discord.User, reason: str = "No reason provided"):
        """Ban a user from the server"""
        if not interaction.user.guild_permissions.ban_members:
            await interaction.response.send_message("❌ You don't have permission!", ephemeral=True)
            return
        
        if member == interaction.user:
            await interaction.response.send_message("❌ You can't ban yourself!", ephemeral=True)
            return
        
        if member.bot:
            await interaction.response.send_message("❌ You can't ban a bot!", ephemeral=True)
            return
        
        guild_member = interaction.guild.get_member(member.id)
        if guild_member and guild_member.top_role >= interaction.user.top_role:
            await interaction.response.send_message("❌ You can't ban someone with equal or higher role!", ephemeral=True)
            return
        
        try:
            await member.send(f"You have been banned from **{interaction.guild.name}** for: {reason}")
        except:
            pass
        
        await interaction.guild.ban(member, reason=reason)
        
        embed = discord.Embed(
            title="🔨 User Banned",
            color=0xFF0000
        )
        embed.add_field(name="User", value=member.mention, inline=True)
        embed.add_field(name="Moderator", value=interaction.user.mention, inline=True)
        embed.add_field(name="Reason", value=reason, inline=False)
        
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="unban", description="Unban a user")
    @app_commands.describe(user_id="User ID to unban")
    @app_commands.default_permissions(ban_members=True)
    async def unban_user(self, interaction: discord.Interaction, user_id: int):
        """Unban a user"""
        if not interaction.user.guild_permissions.ban_members:
            await interaction.response.send_message("❌ You don't have permission!", ephemeral=True)
            return
        
        try:
            user = await self.bot.fetch_user(user_id)
            await interaction.guild.unban(user)
            
            embed = discord.Embed(
                title="✅ User Unbanned",
                color=0x00FF00
            )
            embed.add_field(name="User", value=user.mention, inline=True)
            embed.add_field(name="Moderator", value=interaction.user.mention, inline=True)
            
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"❌ Error unbanning user: {str(e)[:100]}", ephemeral=True)
    
    @app_commands.command(name="timeout", description="Timeout a user (in minutes)")
    @app_commands.describe(member="User to timeout", duration="Duration in minutes", reason="Reason for timeout")
    @app_commands.default_permissions(moderate_members=True)
    async def timeout_user(self, interaction: discord.Interaction, member: discord.User, duration: int, reason: str = "No reason provided"):
        """Timeout a user (in minutes)"""
        if not interaction.user.guild_permissions.moderate_members:
            await interaction.response.send_message("❌ You don't have permission!", ephemeral=True)
            return
        
        if member == interaction.user:
            await interaction.response.send_message("❌ You can't timeout yourself!", ephemeral=True)
            return
        
        guild_member = interaction.guild.get_member(member.id)
        if not guild_member:
            await interaction.response.send_message("❌ User not in server!", ephemeral=True)
            return
        
        if guild_member.top_role >= interaction.user.top_role:
            await interaction.response.send_message("❌ You can't timeout someone with equal or higher role!", ephemeral=True)
            return
        
        timeout_duration = timedelta(minutes=duration)
        
        try:
            await guild_member.timeout(timeout_duration, reason=reason)
            
            embed = discord.Embed(
                title="🤐 User Timed Out",
                color=0xFF9F00
            )
            embed.add_field(name="User", value=member.mention, inline=True)
            embed.add_field(name="Duration", value=f"{duration} minutes", inline=True)
            embed.add_field(name="Reason", value=reason, inline=False)
            
            await interaction.response.send_message(embed=embed)
            
            try:
                await member.send(f"You have been timed out in **{interaction.guild.name}** for {duration} minutes. Reason: {reason}")
            except:
                pass
        except Exception as e:
            await interaction.response.send_message(f"❌ Error timing out user: {str(e)[:100]}", ephemeral=True)
    
    @app_commands.command(name="untimeout", description="Remove timeout from a user")
    @app_commands.describe(member="User to remove timeout from")
    @app_commands.default_permissions(moderate_members=True)
    async def untimeout_user(self, interaction: discord.Interaction, member: discord.User):
        """Remove timeout from a user"""
        if not interaction.user.guild_permissions.moderate_members:
            await interaction.response.send_message("❌ You don't have permission!", ephemeral=True)
            return
        
        guild_member = interaction.guild.get_member(member.id)
        if not guild_member:
            await interaction.response.send_message("❌ User not in server!", ephemeral=True)
            return
        
        try:
            await guild_member.timeout(None)
            
            embed = discord.Embed(
                title="✅ Timeout Removed",
                color=0x00FF00
            )
            embed.add_field(name="User", value=member.mention, inline=True)
            embed.add_field(name="Moderator", value=interaction.user.mention, inline=True)
            
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"❌ Error: {str(e)[:100]}", ephemeral=True)
    
    @app_commands.command(name="purge", description="Delete recent messages (max 100)")
    @app_commands.describe(amount="Number of messages to delete")
    @app_commands.default_permissions(manage_messages=True)
    async def purge_messages(self, interaction: discord.Interaction, amount: int):
        """Delete recent messages (max 100)"""
        if not interaction.user.guild_permissions.manage_messages:
            await interaction.response.send_message("❌ You don't have permission!", ephemeral=True)
            return
        
        if amount > 100:
            await interaction.response.send_message("❌ Can only delete up to 100 messages!", ephemeral=True)
            return
        
        if amount < 1:
            await interaction.response.send_message("❌ Must delete at least 1 message!", ephemeral=True)
            return
        
        deleted = await interaction.channel.purge(limit=amount + 1)
        
        embed = discord.Embed(
            title="🗑️ Messages Deleted",
            description=f"Deleted {len(deleted) - 1} messages",
            color=0xFF6B6B
        )
        
        await interaction.response.send_message(embed=embed, delete_after=5)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
