import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents,
            application_id=YOUR_APPLICATION_ID  # Replace with your app ID (int)
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

bot.run("YOUR_BOT_TOKEN")
