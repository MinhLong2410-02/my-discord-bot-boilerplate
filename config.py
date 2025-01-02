import os
try:
    from dotenv import load_dotenv
except ImportError:
    print('Production Environment')
load_dotenv()

# Discord Bot Token
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Database Credentials
POSTGRES_URL = os.getenv('POSTGRES_URL')
MONGO_URL = os.getenv('MONGO_URL')

API_HOST = os.getenv('API_HOST')
API_PORT = int(os.getenv('API_PORT', 8000))