from bot import load_cogs, run_bot
from asyncio import create_task, gather, run
from api import start_api

async def main():
    load_cogs()
    api_task = create_task(start_api())
    bot_task = create_task(run_bot())
    await gather(api_task, bot_task)

if __name__ == '__main__':
    run(main())