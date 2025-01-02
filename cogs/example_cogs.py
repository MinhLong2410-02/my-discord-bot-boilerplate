from discord import app_commands
from discord.ext import commands
import discord
from utils.logger import setup_logger

# Logger
logger = setup_logger('example_cog')

class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello', help='Responds with a greeting message.')
    async def hello(self, ctx):
        logger.info(f"{ctx.author} used the 'hello' command.")
        await ctx.send(f'Hello, {ctx.author.mention}! 👋')

    @app_commands.command(name='ping', description='Check bot latency.')
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        logger.info(f"{interaction.user} used the 'ping' slash command. Latency: {latency}ms")
        await interaction.response.send_message(f'🏓 Pong! Latency: {latency}ms')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if 'bot' in message.content.lower():
            logger.info(f"Bot keyword detected in message by {message.author}.")
            await message.channel.send("Did someone mention me? 🤖")
    
    
async def setup(bot):
    await bot.add_cog(ExampleCog(bot))