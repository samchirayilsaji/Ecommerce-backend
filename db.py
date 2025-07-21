from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DETAILS = os.getenv("mongodb+srv")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client["ecommerce"]  # or whatever name you want
product_collection = database["products"]
order_collection = database["orders"]
