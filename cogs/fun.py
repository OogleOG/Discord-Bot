import discord
from discord.ext import commands
from discord import app_commands
import aiohttp
import json
from config.config import MEME_APIS

class Fun(commands.Cog):
    """Fun and meme commands"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="darkmeme", description="Get a dark humor meme")
    async def dark_meme(self, interaction: discord.Interaction):
        """Sends a dark humor meme"""
        await interaction.response.defer()
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(MEME_APIS["dark_memes"]) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        embed = discord.Embed(
                            title="🖤 Dark Meme",
                            description=data.get("title", "No title"),
                            color=0x000000
                        )
                        embed.set_image(url=data.get("url"))
                        embed.set_footer(text=f"From: {data.get('subreddit')}")
                        await interaction.followup.send(embed=embed)
                    else:
                        await interaction.followup.send("❌ Failed to fetch meme")
            except Exception as e:
                await interaction.followup.send(f"❌ Error fetching dark meme: {str(e)[:100]}")
    
    @app_commands.command(name="meme", description="Get a random meme")
    async def random_meme(self, interaction: discord.Interaction):
        """Sends a random meme"""
        await interaction.response.defer()
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(MEME_APIS["random_memes"]) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        embed = discord.Embed(
                            title="😂 Random Meme",
                            description=data.get("title", "No title"),
                            color=0xFF6B9D
                        )
                        embed.set_image(url=data.get("url"))
                        embed.set_footer(text=f"From: {data.get('subreddit')}")
                        await interaction.followup.send(embed=embed)
                    else:
                        await interaction.followup.send("❌ Failed to fetch meme")
            except Exception as e:
                await interaction.followup.send(f"❌ Error fetching meme: {str(e)[:100]}")
    
    @app_commands.command(name="darkjoke", description="Get a dark humor joke")
    async def dark_joke(self, interaction: discord.Interaction):
        """Tells a dark humor joke"""
        await interaction.response.defer()
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(MEME_APIS["dark_jokes"]) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        if data.get("type") == "single":
                            joke = data.get("joke")
                            embed = discord.Embed(
                                title="🖤 Dark Joke",
                                description=joke,
                                color=0x000000
                            )
                        else:
                            setup = data.get("setup")
                            delivery = data.get("delivery")
                            embed = discord.Embed(
                                title="🖤 Dark Joke",
                                color=0x000000
                            )
                            embed.add_field(name="Setup", value=setup, inline=False)
                            embed.add_field(name="Punchline", value=delivery, inline=False)
                        await interaction.followup.send(embed=embed)
                    else:
                        await interaction.followup.send("❌ Failed to fetch joke")
            except Exception as e:
                await interaction.followup.send(f"❌ Error fetching joke: {str(e)[:100]}")
    
    @app_commands.command(name="fact", description="Get a random interesting fact")
    async def random_fact(self, interaction: discord.Interaction):
        """Sends a random interesting fact"""
        await interaction.response.defer()
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get("https://uselessfacts.jsoup.com/random.json") as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        embed = discord.Embed(
                            title="💡 Random Fact",
                            description=data.get("text"),
                            color=0xFFD700
                        )
                        await interaction.followup.send(embed=embed)
                    else:
                        await interaction.followup.send("❌ Failed to fetch fact")
            except Exception as e:
                await interaction.followup.send(f"❌ Error fetching fact: {str(e)[:100]}")
    
    @app_commands.command(name="compliment", description="Get a compliment")
    @app_commands.describe(member="Person to compliment (optional)")
    async def compliment(self, interaction: discord.Interaction, member: discord.User = None):
        """Gives a compliment to someone"""
        target = member or interaction.user
        compliments = [
            f"{target.mention}, you're awesome! 🌟",
            f"{target.mention}, you have great vibes! ✨",
            f"{target.mention}, you're a great friend! 💖",
            f"{target.mention}, your energy is contagious! 🔥",
            f"{target.mention}, you deserve good things! 🎉",
            f"{target.mention}, you're making a difference! 🌍",
            f"{target.mention}, you light up the room! 💡",
            f"{target.mention}, you're one of a kind! 🦄",
        ]
        import random
        await interaction.response.send_message(random.choice(compliments))
    
    @app_commands.command(name="8ball", description="Ask the magic 8 ball a question")
    @app_commands.describe(question="Your question")
    async def magic_8ball(self, interaction: discord.Interaction, question: str):
        """Ask the magic 8 ball a question"""
        responses = [
            "Yes, definitely ✅",
            "No, absolutely not ❌",
            "Maybe, ask again later 🤔",
            "Signs point to yes ✨",
            "Don't count on it 😬",
            "Outlook good 👍",
            "Ask again later ⏰",
            "It is certain 🔮",
            "My sources say no 📖",
            "Without a doubt ✔️",
        ]
        import random
        response = random.choice(responses)
        embed = discord.Embed(
            title="🔮 Magic 8 Ball",
            description=f"**Q:** {question}\n\n**A:** {response}",
            color=0x9B59B6
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Fun(bot))
