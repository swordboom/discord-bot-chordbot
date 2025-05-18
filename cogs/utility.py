import discord
from discord import app_commands
from discord.ext import commands
import datetime

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Check bot latency")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        await interaction.response.send_message(f"Pong! Latency: {latency}ms")

    @app_commands.command(name="curtime", description="Get current server time")
    async def curtime(self, interaction: discord.Interaction):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        await interaction.response.send_message(f"Current Time: {now}")

    @app_commands.command(name="curdate", description="Get today's date")
    async def curdate(self, interaction: discord.Interaction):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        await interaction.response.send_message(f"Today's Date: {today}")

    @app_commands.command(name="copy", description="Repeat your message")
    @app_commands.describe(text="Text to copy")
    async def copy(self, interaction: discord.Interaction, text: str):
        await interaction.response.send_message(text)

    @app_commands.command(name="refresh", description="Refresh command (placeholder)")
    async def refresh(self, interaction: discord.Interaction):
        await interaction.response.send_message("Refreshing... (Not implemented)")

async def setup(bot):
    await bot.add_cog(Utility(bot))
