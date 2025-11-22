import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime

class Music(commands.Cog):
    """Music and audio commands"""
    
    def __init__(self, bot):
        self.bot = bot
        self.queue = {}  # {guild_id: [song1, song2, ...]}
        self.current = {}  # {guild_id: current_song}
        self.paused = {}  # {guild_id: True/False}
    
    def get_queue(self, guild_id):
        """Get or create queue for guild"""
        if guild_id not in self.queue:
            self.queue[guild_id] = []
        return self.queue[guild_id]
    
    @app_commands.command(name="join", description="Bot joins your voice channel")
    async def join_voice(self, interaction: discord.Interaction):
        """Bot joins your voice channel"""
        if not interaction.user.voice:
            await interaction.response.send_message("❌ You need to be in a voice channel!", ephemeral=True)
            return
        
        channel = interaction.user.voice.channel
        
        try:
            await channel.connect()
            embed = discord.Embed(
                title="🎵 Joined Voice Channel",
                description=f"Connected to {channel.name}",
                color=0x7289DA
            )
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"❌ Error joining channel: {str(e)[:100]}", ephemeral=True)
    
    @app_commands.command(name="leave", description="Bot leaves the voice channel")
    async def leave_voice(self, interaction: discord.Interaction):
        """Bot leaves the voice channel"""
        if not interaction.guild.voice_client:
            await interaction.response.send_message("❌ I'm not in a voice channel!", ephemeral=True)
            return
        
        await interaction.guild.voice_client.disconnect()
        embed = discord.Embed(
            title="👋 Left Voice Channel",
            color=0x7289DA
        )
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="queue", description="Show the current music queue")
    async def show_queue(self, interaction: discord.Interaction):
        """Show the current music queue"""
        queue = self.get_queue(interaction.guild.id)
        
        if not queue and interaction.guild.id not in self.current:
            await interaction.response.send_message("❌ Queue is empty!", ephemeral=True)
            return
        
        embed = discord.Embed(
            title="🎵 Music Queue",
            color=0x7289DA
        )
        
        if interaction.guild.id in self.current:
            embed.add_field(
                name="Currently Playing",
                value=self.current[interaction.guild.id],
                inline=False
            )
        
        if queue:
            queue_text = "\n".join([f"{i+1}. {song}" for i, song in enumerate(queue[:10])])
            embed.add_field(name="Next Songs", value=queue_text, inline=False)
            
            if len(queue) > 10:
                embed.add_field(name="Queue Length", value=f"... and {len(queue) - 10} more", inline=False)
        
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="skip", description="Skip to the next song")
    async def skip_song(self, interaction: discord.Interaction):
        """Skip to the next song"""
        queue = self.get_queue(interaction.guild.id)
        
        if not queue and interaction.guild.id not in self.current:
            await interaction.response.send_message("❌ Nothing to skip!", ephemeral=True)
            return
        
        if queue:
            skipped = self.current.get(interaction.guild.id, "Unknown")
            self.current[interaction.guild.id] = queue.pop(0)
            embed = discord.Embed(
                title="⏭️ Skipped Song",
                description=f"**Skipped:** {skipped}\n**Now Playing:** {self.current[interaction.guild.id]}",
                color=0x7289DA
            )
        else:
            self.current.pop(interaction.guild.id, None)
            embed = discord.Embed(
                title="⏭️ Queue Ended",
                description="No more songs in queue!",
                color=0x7289DA
            )
        
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="nowplaying", description="Show currently playing song")
    async def now_playing(self, interaction: discord.Interaction):
        """Show currently playing song"""
        if interaction.guild.id not in self.current:
            await interaction.response.send_message("❌ Nothing is playing!", ephemeral=True)
            return
        
        embed = discord.Embed(
            title="🎵 Now Playing",
            description=self.current[interaction.guild.id],
            color=0x7289DA
        )
        
        if self.paused.get(interaction.guild.id, False):
            embed.add_field(name="Status", value="⏸️ Paused", inline=False)
        else:
            embed.add_field(name="Status", value="▶️ Playing", inline=False)
        
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="play", description="Add a song to the queue")
    @app_commands.describe(song_name="Name of the song to play")
    async def play_song(self, interaction: discord.Interaction, song_name: str):
        """Add a song to the queue (demonstration - would need yt-dlp integration)"""
        queue = self.get_queue(interaction.guild.id)
        queue.append(song_name)
        
        if interaction.guild.id not in self.current:
            self.current[interaction.guild.id] = queue.pop(0)
            embed = discord.Embed(
                title="🎵 Now Playing",
                description=self.current[interaction.guild.id],
                color=0x7289DA
            )
            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(
                title="✅ Song Added to Queue",
                description=f"**Position:** #{len(queue) + 1}\n**Song:** {song_name}",
                color=0x7289DA
            )
            await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="pause", description="Pause current song")
    async def pause_music(self, interaction: discord.Interaction):
        """Pause current song"""
        if interaction.guild.id not in self.current:
            await interaction.response.send_message("❌ Nothing is playing!", ephemeral=True)
            return
        
        self.paused[interaction.guild.id] = True
        
        embed = discord.Embed(
            title="⏸️ Music Paused",
            description=self.current[interaction.guild.id],
            color=0x7289DA
        )
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="resume", description="Resume paused song")
    async def resume_music(self, interaction: discord.Interaction):
        """Resume paused song"""
        if interaction.guild.id not in self.current:
            await interaction.response.send_message("❌ Nothing is playing!", ephemeral=True)
            return
        
        if not self.paused.get(interaction.guild.id, False):
            await interaction.response.send_message("❌ Music is already playing!", ephemeral=True)
            return
        
        self.paused[interaction.guild.id] = False
        
        embed = discord.Embed(
            title="▶️ Music Resumed",
            description=self.current[interaction.guild.id],
            color=0x7289DA
        )
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="clear", description="Clear the entire queue")
    async def clear_queue(self, interaction: discord.Interaction):
        """Clear the entire queue"""
        self.queue[interaction.guild.id] = []
        embed = discord.Embed(
            title="🗑️ Queue Cleared",
            color=0x7289DA
        )
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="shuffle", description="Shuffle the queue")
    async def shuffle_queue(self, interaction: discord.Interaction):
        """Shuffle the queue"""
        queue = self.get_queue(interaction.guild.id)
        
        if not queue:
            await interaction.response.send_message("❌ Queue is empty!", ephemeral=True)
            return
        
        import random
        random.shuffle(queue)
        
        embed = discord.Embed(
            title="🎲 Queue Shuffled",
            color=0x7289DA
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Music(bot))
