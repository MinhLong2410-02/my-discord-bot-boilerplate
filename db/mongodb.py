from pymongo import MongoClient
from config import MONGO_URL

mongo_client = MongoClient(MONGO_URL)
db = mongo_client['discord_bot']