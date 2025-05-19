import discord
from discord.ext import commands
import json

with open("config.json") as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents,
            application_id=config["application_id"]
        )

    async def setup_hook(self):
        for cog in ["cogs.music", "cogs.utility", "cogs.voice", "cogs.misc"]:
            await self.load_extension(cog)
        await self.tree.sync()

bot = MyBot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

bot.run(config["token"])
