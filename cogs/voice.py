import discord
from discord import app_commands
from discord.ext import commands
from gtts import gTTS
import os

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="speak", description="Bot will speak the given text in voice channel")
    @app_commands.describe(text="Text to speak")
    async def speak(self, interaction: discord.Interaction, text: str):
        if not interaction.user.voice or not interaction.user.voice.channel:
            await interaction.response.send_message("You must be in a voice channel.", ephemeral=True)
            return

        tts = gTTS(text=text, lang="en")
        tts.save("tts.mp3")

        channel = interaction.user.voice.channel
        vc = interaction.guild.voice_client

        if not vc:
            await channel.connect()
            vc = interaction.guild.voice_client
        elif vc.channel != channel:
            await vc.move_to(channel)

        if vc.is_playing():
            vc.stop()

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("tts.mp3"))
        vc.play(source)

        await interaction.response.send_message("Speaking...")

async def setup(bot):
    await bot.add_cog(Voice(bot))
