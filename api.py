from fastapi import FastAPI
from routers import example
from uvicorn import Config, Server
from config import API_HOST, API_PORT

app = FastAPI()

# Include Routers
app.include_router(example.router)


@app.get('/')
async def root():
    return {'message': 'FastAPI Server is Running'}


async def start_api():
    config = Config(
        app=app,
        host=API_HOST,
        port=API_PORT,
    )
    server = Server(config)
    try:
        await server.serve()
    except KeyboardInterrupt:
        print("Shutting down FastAPI server gracefully.")
    except Exception as e:
        print(f"Failed to start FastAPI server: {e}")


if __name__ == "__main__":
    import asyncio
    try:
        asyncio.run(start_api())
    except KeyboardInterrupt:
        print("FastAPI server stopped manually.")
