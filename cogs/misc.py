import discord
from discord import app_commands
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hello", description="Say hello to the bot")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello, {interaction.user.mention}!")

    @app_commands.command(name="help", description="Show all available commands")
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Bot Commands Help", color=discord.Color.blurple())
        embed.add_field(name="/join", value="Join your voice channel", inline=False)
        embed.add_field(name="/play [song]", value="Play a song from the song library", inline=False)
        embed.add_field(name="/skip", value="Skip the current song", inline=False)
        embed.add_field(name="/pause", value="Pause the current song", inline=False)
        embed.add_field(name="/resume", value="Resume the paused song", inline=False)
        embed.add_field(name="/stop", value="Stop playback and clear queue", inline=False)
        embed.add_field(name="/repeat", value="Toggle repeat for current song", inline=False)
        embed.add_field(name="/queue", value="Show current song queue", inline=False)
        embed.add_field(name="/leave", value="Disconnect the bot from voice channel", inline=False)
        embed.add_field(name="/ping", value="Show bot latency", inline=False)
        embed.add_field(name="/curtime", value="Show current time", inline=False)
        embed.add_field(name="/curdate", value="Show current date", inline=False)
        embed.add_field(name="/copy [text]", value="Bot repeats your text", inline=False)
        embed.add_field(name="/refresh", value="Refresh command placeholder", inline=False)
        embed.add_field(name="/speak [text]", value="Bot speaks your text in voice channel", inline=False)
        embed.add_field(name="/hello", value="Say hello to the bot", inline=False)

        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Misc(bot))
