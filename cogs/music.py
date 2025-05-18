import discord
from discord import app_commands
from discord.ext import commands
import os

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Per guild queues
        self.queues = {}
        self.repeat = {}

    def get_queue(self, guild_id):
        return self.queues.setdefault(guild_id, [])

    def get_repeat(self, guild_id):
        return self.repeat.setdefault(guild_id, False)

    def set_repeat(self, guild_id, value):
        self.repeat[guild_id] = value

    def play_next(self, interaction: discord.Interaction):
        guild_id = interaction.guild.id
        vc = interaction.guild.voice_client
        if not vc:
            return
        queue = self.get_queue(guild_id)
        if self.get_repeat(guild_id) and hasattr(self, "current_song"):
            # Replay the same song
            song = self.current_song[guild_id]
        elif queue:
            song = queue.pop(0)
            self.current_song[guild_id] = song
        else:
            self.current_song[guild_id] = None
            return
        path = os.path.join("song-lib", f"{song}.mp3")
        if not os.path.isfile(path):
            return
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(path), volume=0.5)
        def after_playing(error):
            if error:
                print(f"Player error: {error}")
            coro = self.play_next(interaction)
            fut = discord.utils.ensure_future(coro)
        vc.play(source, after=after_playing)

    @app_commands.command(name="join", description="Join your voice channel")
    async def join(self, interaction: discord.Interaction):
        if not interaction.user.voice or not interaction.user.voice.channel:
            await interaction.response.send_message("You need to be in a voice channel.", ephemeral=True)
            return
        channel = interaction.user.voice.channel
        vc = interaction.guild.voice_client
        if vc and vc.channel.id == channel.id:
            await interaction.response.send_message("I'm already in your voice channel.", ephemeral=True)
            return
        elif vc:
            await vc.move_to(channel)
        else:
            await channel.connect()
        await interaction.response.send_message(f"Joined {channel.name}")

    @app_commands.command(name="play", description="Play a song from song library")
    @app_commands.describe(song="Name of the song file (without .mp3)")
    async def play(self, interaction: discord.Interaction, song: str):
        guild_id = interaction.guild.id
        vc = interaction.guild.voice_client
        if not interaction.user.voice or not interaction.user.voice.channel:
            await interaction.response.send_message("You must be in a voice channel to play music.", ephemeral=True)
            return
        if not vc:
            await interaction.user.voice.channel.connect()
            vc = interaction.guild.voice_client
        song_path = os.path.join("song-lib", f"{song}.mp3")
        if not os.path.isfile(song_path):
            await interaction.response.send_message(f"Song '{song}' not found in library.", ephemeral=True)
            return
        queue = self.get_queue(guild_id)
        if vc.is_playing() or vc.is_paused():
            queue.append(song)
            await interaction.response.send_message(f"Added **{song}** to the queue.")
        else:
            self.current_song = {}
            self.current_song[guild_id] = song
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song_path), volume=0.5)
            vc.play(source, after=lambda e: self.bot.loop.create_task(self.play_next(interaction)))
            await interaction.response.send_message(f"Now playing **{song}**.")

    @app_commands.command(name="skip", description="Skip the current song")
    async def skip(self, interaction: discord.Interaction):
        vc = interaction.guild.voice_client
        if not vc or (not vc.is_playing() and not vc.is_paused()):
            await interaction.response.send_message("Nothing is playing to skip.", ephemeral=True)
            return
        vc.stop()
        await interaction.response.send_message("Skipped current song.")

    @app_commands.command(name="pause", description="Pause the current song")
    async def pause(self, interaction: discord.Interaction):
        vc = interaction.guild.voice_client
        if not vc or not vc.is_playing():
            await interaction.response.send_message("Nothing is playing.", ephemeral=True)
            return
        vc.pause()
        await interaction.response.send_message("Paused playback.")

    @app_commands.command(name="resume", description="Resume paused song")
    async def resume(self, interaction: discord.Interaction):
        vc = interaction.guild.voice_client
        if not vc or not vc.is_paused():
            await interaction.response.send_message("Nothing is paused.", ephemeral=True)
            return
        vc.resume()
        await interaction.response.send_message("Resumed playback.")

    @app_commands.command(name="stop", description="Stop playback and clear the queue")
    async def stop(self, interaction: discord.Interaction):
        vc = interaction.guild.voice_client
        guild_id = interaction.guild.id
        if not vc or (not vc.is_playing() and not vc.is_paused()):
            await interaction.response.send_message("Nothing is playing.", ephemeral=True)
            return
        vc.stop()
        self.queues[guild_id] = []
        await interaction.response.send_message("Stopped playback and cleared queue.")

    @app_commands.command(name="repeat", description="Toggle repeat for current song")
    async def repeat(self, interaction: discord.Interaction):
        guild_id = interaction.guild.id
        current = self.get_repeat(guild_id)
        self.set_repeat(guild_id, not current)
        await interaction.response.send_message(f"Repeat {'enabled' if not current else 'disabled'}.")

    @app_commands.command(name="queue", description="Show current song queue")
    async def queue(self, interaction: discord.Interaction):
        guild_id = interaction.guild.id
        queue = self.get_queue(guild_id)
        if not queue:
            await interaction.response.send_message("Queue is empty.")
            return
        qlist = "\n".join(f"{i+1}. {song}" for i, song in enumerate(queue))
        await interaction.response.send_message(f"**Queue:**\n{qlist}")

    @app_commands.command(name="leave", description="Make the bot leave the voice channel")
    async def leave(self, interaction: discord.Interaction):
        vc = interaction.guild.voice_client
        if not vc:
            await interaction.response.send_message("I'm not connected to any voice channel.", ephemeral=True)
            return
        await vc.disconnect()
        await interaction.response.send_message("Disconnected from the voice channel.")

async def setup(bot):
    await bot.add_cog(Music(bot))
