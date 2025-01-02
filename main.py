from bot import run_bot
from asyncio import create_task, gather, run
from api import start_api
import asyncio

async def main():
    api_task = create_task(start_api())
    bot_task = create_task(run_bot())
    await gather(api_task, bot_task)

if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    run(main())