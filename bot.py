import discord
import json
from discord.ext import commands

# Load configuration from config.json
with open("config.json") as f:
    config = json.load(f)

BOT_TOKEN = config.get("token")
APPLICATION_ID = config.get("application_id")

intents = discord.Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents,
            application_id=APPLICATION_ID  # Loaded from config.json
        )
        self.tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self):
        for cog in ["cogs.music", "cogs.utility", "cogs.voice", "cogs.misc"]:
            await self.load_extension(cog)
        await self.tree.sync()

bot = MyBot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

bot.run(BOT_TOKEN)
