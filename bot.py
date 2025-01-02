import discord
from discord.ext import commands
import os, aiohttp, asyncio
from config import BOT_TOKEN
from utils.logger import setup_logger
# Logger
logger = setup_logger('discord_bot')

# Intents
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.guilds = True  
intents.members = True

# Bot Setup
bot = commands.Bot(command_prefix='!', intents=intents)

# Load Cogs
async def load_cogs():
    cogs_dir = os.path.join(os.path.dirname(__file__), 'cogs')
    for filename in os.listdir(cogs_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                logger.info(f"Successfully loaded cog: {filename}")
            except Exception as e:
                logger.error(f"Failed to load cog: {filename}. Error: {e}")



@bot.event
async def on_ready():
    logger.info(f'Bot connected as {bot.user}')
    try:
        await bot.tree.sync()
        command_count = len(bot.tree.get_commands())
        logger.info(f"Slash commands synced successfully. Total commands: {command_count}")
    except Exception as e:
        logger.error(f"Failed to sync slash commands: {e}")



async def run_bot():
    await load_cogs()
    max_retries = 5
    retry_delay = 1

    for attempt in range(max_retries):
        try:
            await bot.start(BOT_TOKEN)
            break
        except (discord.ConnectionClosed, aiohttp.ClientConnectorError) as e:
            logger.error(f"Connection error: {str(e)}. Attempt {attempt + 1}/{max_retries}")

            await asyncio.sleep(retry_delay)
            retry_delay = min(retry_delay * 2, 60)
    else:
        logger.critical("Max retries exceeded. Bot could not connect to Discord.")

async def main():
    bot_task = asyncio.create_task(run_bot())
    await asyncio.gather(bot_task)

if __name__ == '__main__':
    asyncio.run(main())