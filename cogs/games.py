import discord
from discord.ext import commands
from discord import app_commands
import random
import aiohttp

class Games(commands.Cog):
    """Games and entertainment commands"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="roll", description="Roll dice! Format: 2d6 (rolls 2 six-sided dice)")
    @app_commands.describe(dice="Dice format (e.g., 2d6)")
    async def roll_dice(self, interaction: discord.Interaction, dice: str = "1d6"):
        """Roll dice!"""
        try:
            parts = dice.split("d")
            if len(parts) != 2:
                await interaction.response.send_message("❌ Invalid format! Use: 2d6")
                return
            
            num_dice = int(parts[0])
            num_sides = int(parts[1])
            
            if num_dice < 1 or num_dice > 100 or num_sides < 1 or num_sides > 1000:
                await interaction.response.send_message("❌ Too many dice or too many sides!")
                return
            
            rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
            total = sum(rolls)
            
            embed = discord.Embed(
                title="🎲 Dice Roll",
                description=f"**Dice:** {dice}",
                color=0xFF6B9D
            )
            embed.add_field(name="Results", value=" + ".join(map(str, rolls)), inline=False)
            embed.add_field(name="Total", value=f"**{total}**", inline=False)
            await interaction.response.send_message(embed=embed)
        except ValueError:
            await interaction.response.send_message("❌ Invalid format! Use: 2d6")
    
    @app_commands.command(name="coinflip", description="Flip a coin")
    async def coin_flip(self, interaction: discord.Interaction):
        """Flip a coin"""
        result = random.choice(["Heads 🪙", "Tails 🪙"])
        embed = discord.Embed(
            title="🪙 Coin Flip",
            description=result,
            color=0xFFD700
        )
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="rps", description="Play rock, paper, scissors!")
    @app_commands.describe(choice="Your choice: rock, paper, or scissors")
    async def rock_paper_scissors(self, interaction: discord.Interaction, choice: str):
        """Play rock paper scissors!"""
        choices = ["rock", "paper", "scissors"]
        user_choice = choice.lower()
        
        if user_choice not in choices:
            await interaction.response.send_message("❌ Choose: rock, paper, or scissors")
            return
        
        bot_choice = random.choice(choices)
        
        if user_choice == bot_choice:
            result = "It's a tie! 🤝"
            color = 0xFFFF00
        elif (user_choice == "rock" and bot_choice == "scissors") or \
             (user_choice == "paper" and bot_choice == "rock") or \
             (user_choice == "scissors" and bot_choice == "paper"):
            result = f"You win! 🎉\nYou: {user_choice.capitalize()}\nBot: {bot_choice.capitalize()}"
            color = 0x00FF00
        else:
            result = f"I win! 😎\nYou: {user_choice.capitalize()}\nBot: {bot_choice.capitalize()}"
            color = 0xFF0000
        
        embed = discord.Embed(
            title="✋ Rock Paper Scissors",
            description=result,
            color=color
        )
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="riddle", description="Get a random riddle to solve")
    async def riddle(self, interaction: discord.Interaction):
        """Get a riddle to solve"""
        riddles = [
            {
                "question": "I have cities but no houses, forests but no trees, and water but no fish. What am I?",
                "answer": "A map"
            },
            {
                "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
                "answer": "An echo"
            },
            {
                "question": "The more you take, the more you leave behind. What am I?",
                "answer": "Footsteps"
            },
            {
                "question": "I have a head and a tail but no body. What am I?",
                "answer": "A coin"
            },
            {
                "question": "What gets wetter as it dries?",
                "answer": "A towel"
            },
            {
                "question": "I'm tall when I'm young and short when I'm old. What am I?",
                "answer": "A candle"
            },
            {
                "question": "What question can you never answer 'yes' to?",
                "answer": "Are you asleep?"
            },
            {
                "question": "I have hands but cannot clap. What am I?",
                "answer": "A clock"
            },
        ]
        
        riddle = random.choice(riddles)
        embed = discord.Embed(
            title="🧩 Riddle",
            description=riddle["question"],
            color=0x9B59B6
        )
        embed.set_footer(text=f"Answer: ||{riddle['answer']}||")
        
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="trivia", description="Get a random trivia question")
    async def trivia(self, interaction: discord.Interaction):
        """Get a trivia question"""
        await interaction.response.defer()
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get("https://opentdb.com/api.php?amount=1&type=multiple") as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        question_data = data["results"][0]
                        
                        question = question_data["question"].replace("&quot;", '"').replace("&amp;", "&")
                        correct = question_data["correct_answer"].replace("&quot;", '"').replace("&amp;", "&")
                        wrong = [a.replace("&quot;", '"').replace("&amp;", "&") for a in question_data["incorrect_answers"]]
                        
                        all_answers = [correct] + wrong
                        random.shuffle(all_answers)
                        
                        embed = discord.Embed(
                            title="🧠 Trivia Question",
                            description=question,
                            color=0x00B8FF
                        )
                        for i, answer in enumerate(all_answers, 1):
                            embed.add_field(name=f"Option {i}", value=answer, inline=False)
                        embed.set_footer(text=f"Category: {question_data['category']}")
                        
                        await interaction.followup.send(embed=embed)
                        await interaction.followup.send(f"**Answer:** ||{correct}||")
                    else:
                        await interaction.followup.send("❌ Failed to fetch trivia")
            except Exception as e:
                await interaction.followup.send(f"❌ Error: {str(e)[:100]}")

async def setup(bot):
    await bot.add_cog(Games(bot))
