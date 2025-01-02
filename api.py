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
    config = Config(app, host=API_HOST, port=API_PORT)
    server = Server(config)
    await server.serve()

if __name__ == "__main__":
    import asyncio
    asyncio.run(start_api())