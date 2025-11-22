import discord
from discord.ext import commands
from discord import app_commands
import random

class Interactive(commands.Cog):
    """Interactive and social commands"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="hug", description="Give someone a hug")
    @app_commands.describe(member="Person to hug")
    async def hug(self, interaction: discord.Interaction, member: discord.User):
        """Give someone a hug"""
        if member == interaction.user:
            await interaction.response.send_message(f"{interaction.user.mention} hugged themselves 🤗")
        else:
            embed = discord.Embed(
                title="🤗 Hug",
                description=f"{interaction.user.mention} gives {member.mention} a warm hug!",
                color=0xFF69B4
            )
            await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="highfive", description="Give someone a high five")
    @app_commands.describe(member="Person to high five")
    async def highfive(self, interaction: discord.Interaction, member: discord.User):
        """Give someone a high five"""
        if member == interaction.user:
            await interaction.response.send_message(f"{interaction.user.mention} high-fived themselves ✋")
        else:
            embed = discord.Embed(
                title="✋ High Five",
                description=f"{interaction.user.mention} and {member.mention} high five!",
                color=0xFFD700
            )
            await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="slap", description="Playfully slap someone")
    @app_commands.describe(member="Person to slap")
    async def slap(self, interaction: discord.Interaction, member: discord.User):
        """Playfully slap someone"""
        if member == interaction.user:
            await interaction.response.send_message(f"{interaction.user.mention} slaps themselves 🤨")
        else:
            embed = discord.Embed(
                title="👋 Slap",
                description=f"{interaction.user.mention} playfully slaps {member.mention}!",
                color=0xFF6B6B
            )
            await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="kiss", description="Send a kiss to someone")
    @app_commands.describe(member="Person to kiss")
    async def kiss(self, interaction: discord.Interaction, member: discord.User):
        """Send a kiss to someone"""
        if member == interaction.user:
            await interaction.response.send_message(f"{interaction.user.mention} sends themselves a kiss 💋")
        else:
            embed = discord.Embed(
                title="💋 Kiss",
                description=f"{interaction.user.mention} sends {member.mention} a kiss!",
                color=0xFF69B4
            )
            await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="punch", description="Punch someone (in a fun way)")
    @app_commands.describe(member="Person to punch")
    async def punch(self, interaction: discord.Interaction, member: discord.User):
        """Punch someone (in a fun way)"""
        if member == interaction.user:
            await interaction.response.send_message(f"{interaction.user.mention} punches themselves 👊 ouch!")
        else:
            embed = discord.Embed(
                title="👊 Punch",
                description=f"{interaction.user.mention} playfully punches {member.mention}!",
                color=0xFF4500
            )
            await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="dance", description="Dance with someone")
    @app_commands.describe(member="Person to dance with (optional)")
    async def dance(self, interaction: discord.Interaction, member: discord.User = None):
        """Dance with someone"""
        if member is None:
            dances = ["🕺 does the disco!", "💃 does the macarena!", "🪩 does the moonwalk!"]
            embed = discord.Embed(
                title="💃 Dance",
                description=f"{interaction.user.mention} {random.choice(dances)}",
                color=0xFF6B9D
            )
            await interaction.response.send_message(embed=embed)
        elif member == interaction.user:
            dances = ["with themselves", "solo", "the moonwalk"]
            embed = discord.Embed(
                title="💃 Dance",
                description=f"{interaction.user.mention} dances {random.choice(dances)}!",
                color=0xFF6B9D
            )
            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(
                title="💃 Dance",
                description=f"{interaction.user.mention} and {member.mention} dance together! 🕺",
                color=0xFF6B9D
            )
            await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="ship", description="Ship two people together (for fun)")
    @app_commands.describe(member1="First person to ship", member2="Second person to ship (optional)")
    async def ship(self, interaction: discord.Interaction, member1: discord.User, member2: discord.User = None):
        """Ship two people together (for fun)"""
        if member2 is None:
            member2 = interaction.user
        
        if member1 == member2:
            await interaction.response.send_message("❌ Can't ship someone with themselves!", ephemeral=True)
            return
        
        ship_names = [
            f"{member1.name[:len(member1.name)//2]}{member2.name[len(member2.name)//2:]}",
            f"{member1.name[:3]}{member2.name[-3:]}",
            f"{member1.display_name.split()[0]} & {member2.display_name.split()[0]}",
        ]
        
        compatibility = random.randint(0, 100)
        
        embed = discord.Embed(
            title="💕 Shipping",
            description=f"{member1.mention} + {member2.mention}",
            color=0xFF69B4
        )
        embed.add_field(name="Ship Name", value=random.choice(ship_names), inline=False)
        embed.add_field(name="Compatibility", value=f"{'█' * (compatibility // 10)}{'░' * (10 - compatibility // 10)} {compatibility}%", inline=False)
        
        if compatibility >= 80:
            embed.add_field(name="Verdict", value="🔥 MATCH MADE IN HEAVEN! 🔥", inline=False)
        elif compatibility >= 60:
            embed.add_field(name="Verdict", value="💚 Pretty good match!", inline=False)
        elif compatibility >= 40:
            embed.add_field(name="Verdict", value="🤔 Could work...", inline=False)
        else:
            embed.add_field(name="Verdict", value="❌ Better as friends", inline=False)
        
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="insult", description="Playfully insult someone")
    @app_commands.describe(member="Person to insult (optional)")
    async def insult(self, interaction: discord.Interaction, member: discord.User = None):
        """Playfully insult someone"""
        member = member or interaction.user
        
        insults = [
            f"{member.mention}, you're as useful as a screen door on a submarine.",
            f"{member.mention}, if you were a vegetable, you'd be a turnip.",
            f"{member.mention}, you're the human version of a loading screen.",
            f"{member.mention}, you're not even the worst thing to happen today, but you're close.",
            f"{member.mention}, your brain is like a web browser with 47 tabs open.",
            f"{member.mention}, you're a human without the intelligence.",
            f"{member.mention}, you're what happens when biology goes wrong.",
            f"{member.mention}, you're not stupid, you just make stupid look genius.",
        ]
        
        embed = discord.Embed(
            title="😜 Playful Insult",
            description=random.choice(insults),
            color=0xFF6B9D
        )
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="choose", description="Bot chooses from your options")
    @app_commands.describe(option1="First option", option2="Second option", option3="Third option (optional)", option4="Fourth option (optional)")
    async def choose(self, interaction: discord.Interaction, option1: str, option2: str, option3: str = None, option4: str = None):
        """Bot chooses from your options"""
        options = [option1, option2]
        if option3:
            options.append(option3)
        if option4:
            options.append(option4)
        
        choice = random.choice(options)
        
        embed = discord.Embed(
            title="🤔 I Choose...",
            description=f"**{choice}**",
            color=0x9B59B6
        )
        embed.set_footer(text=f"From: {', '.join(options)}")
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="poll", description="Create a simple poll")
    @app_commands.describe(question="The poll question")
    async def poll(self, interaction: discord.Interaction, question: str):
        """Create a simple poll"""
        embed = discord.Embed(
            title="📊 Poll",
            description=question,
            color=0x00B8FF
        )
        embed.set_footer(text="React with 👍 or 👎 to vote!")
        
        msg = await interaction.response.send_message(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
    
    @app_commands.command(name="random", description="Get a random feature to use")
    async def random_command(self, interaction: discord.Interaction):
        """Get a random feature to use"""
        features = [
            "Try `/fact` for an interesting fact!",
            "Try `/8ball` for predictions!",
            "Try `/roll` to roll the dice!",
            "Try `/trivia` for a challenge!",
            "Try `/dog` or `/cat` for cute pictures!",
            "Try `/quote` for inspiration!",
            "Try `/riddle` to test your brain!",
            "Try `/rps` to play rock paper scissors!",
            "Try `/ship` to ship your friends!",
            "Try `/roast` for good-natured humor!",
        ]
        
        embed = discord.Embed(
            title="🎲 Random Feature",
            description=random.choice(features),
            color=0xFF6B9D
        )
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="flip", description="Flip text upside down")
    @app_commands.describe(text="Text to flip")
    async def flip_text(self, interaction: discord.Interaction, text: str):
        """Flip text upside down"""
        flip_map = {
            'a': 'ɐ', 'b': 'q', 'c': 'ɔ', 'd': 'p', 'e': 'ǝ', 'f': 'ɟ', 'g': 'ƃ', 'h': 'ɥ',
            'i': 'ᴉ', 'j': 'ɾ', 'k': 'ʞ', 'l': 'l', 'm': 'ɯ', 'n': 'u', 'o': 'o', 'p': 'd',
            'q': 'b', 'r': 'ɹ', 's': 's', 't': 'ʇ', 'u': 'n', 'v': 'ʌ', 'w': 'ʍ', 'x': 'x',
            'y': 'ʎ', 'z': 'z', '0': '0', '1': 'Ɩ', '2': 'ᄅ', '3': 'Ɛ', '4': 'ㄣ', '5': 'ϛ',
            '6': '9', '7': 'ㄥ', '8': '8', '9': '6', '.': '˙', ',': '\'', '!': '¡', '?': '¿',
            "'": ',', '"': '„', '(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{',
            '_': '‾', ';': '؛', ' ': ' '
        }
        
        flipped = ''.join([flip_map.get(char, char) for char in text.lower()])[::-1]
        
        embed = discord.Embed(
            title="🙃 Flipped Text",
            description=f"**Original:** {text}\n**Flipped:** {flipped}",
            color=0x7289DA
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Interactive(bot))
