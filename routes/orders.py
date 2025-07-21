from fastapi import APIRouter
from models.orders import Order  # ✅ Use the model from models/orders.py
from db import order_collection
from bson import ObjectId

router = APIRouter()

@router.post("/orders", status_code=201)
async def create_order(order: Order):
    result = await order_collection.insert_one(order.dict())
    return {"id": str(result.inserted_id), **order.dict()}

@router.get("/orders/{user_id}", status_code=200)
async def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    cursor = order_collection.find({"user_id": user_id}).skip(offset).limit(limit)
    orders = []
    async for order in cursor:
        order["_id"] = str(order["_id"])
        orders.append(order)
    return orders
