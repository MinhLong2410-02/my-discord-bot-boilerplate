import discord
from discord.ext import commands
import os, aiohttp, asyncio
from config import BOT_TOKEN
from utils.logger import setup_logger
from routers import start_api
# Logger
logger = setup_logger('discord_bot')

# Intents
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# Bot Setup
bot = commands.Bot(command_prefix='!', intents=intents)

# Load Cogs
def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and filename != '__init__.py':
            bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    logger.info(f'Bot connected as {bot.user}')
    print(f'Bot connected as {bot.user}')


async def run_bot():
    max_retries = 5
    retry_delay = 1

    for attempt in range(max_retries):
        try:
            await bot.start(BOT_TOKEN)
            break
        except (discord.ConnectionClosed, aiohttp.ClientConnectorError) as e:
            logger.error(f"Connection error: {e}. Attempt {attempt + 1}/{max_retries}")
            await asyncio.sleep(retry_delay)
            retry_delay = min(retry_delay * 2, 60)
    else:
        logger.critical("Max retries exceeded. Bot could not connect to Discord.")

async def main():
    load_cogs()
    bot_task = asyncio.create_task(run_bot())
    await asyncio.gather(bot_task)

if __name__ == '__main__':
    asyncio.run(main())