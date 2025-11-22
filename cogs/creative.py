import discord
from discord.ext import commands
from discord import app_commands
import random
import aiohttp

class Creative(commands.Cog):
    """Creative and fun commands"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="quote", description="Get an inspirational quote")
    async def daily_quote(self, interaction: discord.Interaction):
        """Get an inspirational quote"""
        await interaction.response.defer()
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get("https://api.quotable.io/random") as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        embed = discord.Embed(
                            title="💬 Quote",
                            description=f'"{data.get("content")}"',
                            color=0xFFD700
                        )
                        embed.set_footer(text=f"— {data.get('author')}")
                        await interaction.followup.send(embed=embed)
                    else:
                        await interaction.followup.send("❌ Failed to fetch quote")
            except Exception as e:
                await interaction.followup.send(f"❌ Error: {str(e)[:100]}")
    
    @app_commands.command(name="poem", description="Get a random poem")
    async def random_poem(self, interaction: discord.Interaction):
        """Get a random poem"""
        await interaction.response.defer()
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get("https://poetrydb.org/random/1/lines.json") as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        poem_data = data[0]
                        poem_text = "\n".join(poem_data.get("lines", []))
                        
                        embed = discord.Embed(
                            title="📝 Random Poem",
                            description=poem_text[:2000],
                            color=0x9B59B6
                        )
                        await interaction.followup.send(embed=embed)
                    else:
                        await interaction.followup.send("❌ Failed to fetch poem")
            except Exception as e:
                await interaction.followup.send(f"❌ Error: {str(e)[:100]}")
    
    @app_commands.command(name="dog", description="Get a random dog image")
    async def dog_image(self, interaction: discord.Interaction):
        """Get a random dog image"""
        await interaction.response.defer()
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get("https://dog.ceo/api/breeds/image/random") as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        embed = discord.Embed(
                            title="🐕 Random Dog",
                            color=0xA0522D
                        )
                        embed.set_image(url=data.get("message"))
                        await interaction.followup.send(embed=embed)
                    else:
                        await interaction.followup.send("❌ Failed to fetch dog image")
            except Exception as e:
                await interaction.followup.send(f"❌ Error: {str(e)[:100]}")
    
    @app_commands.command(name="cat", description="Get a random cat image")
    async def cat_image(self, interaction: discord.Interaction):
        """Get a random cat image"""
        await interaction.response.defer()
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get("https://api.thecatapi.com/v1/images/search") as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        embed = discord.Embed(
                            title="🐱 Random Cat",
                            color=0xFF69B4
                        )
                        embed.set_image(url=data[0].get("url"))
                        await interaction.followup.send(embed=embed)
                    else:
                        await interaction.followup.send("❌ Failed to fetch cat image")
            except Exception as e:
                await interaction.followup.send(f"❌ Error: {str(e)[:100]}")
    
    @app_commands.command(name="weather", description="Get weather for a city")
    @app_commands.describe(city="City name")
    async def weather(self, interaction: discord.Interaction, city: str):
        """Get weather for a city (requires OpenWeatherMap API key)"""
        embed = discord.Embed(
            title="🌤️ Weather",
            description=f"To use this command, add your OpenWeatherMap API key to config!",
            color=0x87CEEB
        )
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="rate", description="Rate something out of 10")
    @app_commands.describe(thing="What to rate")
    async def rate(self, interaction: discord.Interaction, thing: str):
        """Rate something out of 10"""
        rating = random.randint(1, 10)
        emoji = "⭐" * rating
        
        embed = discord.Embed(
            title="⭐ Rating",
            description=f"I rate **{thing}**: **{rating}/10**\n{emoji}",
            color=0xFFD700
        )
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="reverse", description="Reverse text")
    @app_commands.describe(text="Text to reverse")
    async def reverse_text(self, interaction: discord.Interaction, text: str):
        """Reverse text"""
        embed = discord.Embed(
            title="🔄 Reversed Text",
            description=f"**Original:** {text}\n**Reversed:** {text[::-1]}",
            color=0x7289DA
        )
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="emojify", description="Convert text to emoji representation")
    @app_commands.describe(text="Text to emojify")
    async def emojify(self, interaction: discord.Interaction, text: str):
        """Convert text to emoji representation"""
        emoji_dict = {
            'a': '🇦', 'b': '🇧', 'c': '🇨', 'd': '🇩', 'e': '🇪', 'f': '🇫', 'g': '🇬', 'h': '🇭',
            'i': '🇮', 'j': '🇯', 'k': '🇰', 'l': '🇱', 'm': '🇲', 'n': '🇳', 'o': '🇴', 'p': '🇵',
            'q': '🇶', 'r': '🇷', 's': '🇸', 't': '🇹', 'u': '🇺', 'v': '🇻', 'w': '🇼', 'x': '🇽',
            'y': '🇾', 'z': '🇿', ' ': '  ', '0': '0️⃣', '1': '1️⃣', '2': '2️⃣', '3': '3️⃣', '4': '4️⃣',
            '5': '5️⃣', '6': '6️⃣', '7': '7️⃣', '8': '8️⃣', '9': '9️⃣'
        }
        
        emojified = ''.join([emoji_dict.get(char.lower(), char) for char in text])
        
        if len(emojified) > 2000:
            await interaction.response.send_message("❌ Text too long!", ephemeral=True)
            return
        
        embed = discord.Embed(
            title="😀 Emojified",
            description=emojified,
            color=0xFF6B9D
        )
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="roast", description="Give someone a roast (good-natured)")
    @app_commands.describe(member="User to roast (optional)")
    async def roast(self, interaction: discord.Interaction, member: discord.User = None):
        """Give someone a roast (good-natured)"""
        member = member or interaction.user
        
        roasts = [
            f"{member.mention}, you're the human equivalent of a comment that should have been a DM.",
            f"{member.mention}, you're proof that even Discord admins make mistakes.",
            f"{member.mention}, I'd explain it to you but I don't have a crayons-to-English dictionary.",
            f"{member.mention}, you bring shame to your family name.",
            f"{member.mention}, if you were a vegetable, you'd be a turnip because you turn everything up.",
            f"{member.mention}, you're like a dictionary without definitions.",
            f"{member.mention}, your IQ is lower than a Discord bot's ping.",
            f"{member.mention}, you're the kind of person to make a typo in your own autobiography.",
        ]
        
        roast = random.choice(roasts)
        embed = discord.Embed(
            title="🔥 Roast",
            description=roast,
            color=0xFF4500
        )
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="truth", description="Get a truth or dare question")
    async def truth_or_dare_truth(self, interaction: discord.Interaction):
        """Get a truth or dare question"""
        truths = [
            "What's your biggest secret?",
            "Have you ever lied to your best friend?",
            "What's your most embarrassing moment?",
            "Who do you have a crush on?",
            "What's your biggest fear?",
            "Have you ever cried watching a movie?",
            "What's the weirdest thing you've done?",
            "Do you believe in ghosts?",
        ]
        
        dares = [
            "Send a message in a server with the first emoji you see!",
            "React with 👁️ to the last message in chat!",
            "Change your Discord status to something funny!",
            "Send a funny message in general chat!",
            "Use only emojis to communicate for 5 messages!",
            "Describe your day using only song lyrics!",
            "Speak in a funny accent for the next 3 messages!",
            "Reply to the next message with 'That's what she said!'!",
        ]
        
        question_type = random.choice(["truth", "dare"])
        
        if question_type == "truth":
            question = random.choice(truths)
            title = "💭 Truth"
            color = 0x00B8FF
        else:
            question = random.choice(dares)
            title = "🎯 Dare"
            color = 0xFF6B9D
        
        embed = discord.Embed(
            title=title,
            description=question,
            color=color
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Creative(bot))
