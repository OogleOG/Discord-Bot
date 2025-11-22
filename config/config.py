import os
from dotenv import load_dotenv

load_dotenv()

# Bot Configuration
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
COMMAND_PREFIX = os.getenv("COMMAND_PREFIX", "!")

# Bot settings
BOT_NAME = "WeenieHut Bot"
BOT_STATUS = "with your feelings ♡"
BOT_COLOR = 0xFF1493  # Deep Pink

# Feature toggles
FEATURES = {
    "fun": True,
    "memes": True,
    "games": True,
    "moderation": True,
    "music": True,
    "utility": True,
}

# API endpoints for memes and jokes
MEME_APIS = {
    "dark_memes": "https://meme-api.com/gimme/darkjokes",
    "random_memes": "https://meme-api.com/gimme",
    "dark_jokes": "https://v2.jokeapi.dev/joke/Dark",
}

# Moderation settings
MOD_LOG_ENABLED = True
WARNING_THRESHOLD = 3
