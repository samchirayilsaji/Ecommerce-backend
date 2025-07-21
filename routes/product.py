from fastapi import APIRouter
from models.product import Product
from db import product_collection
from bson import ObjectId

router = APIRouter()

@router.post("/products", status_code=201)
async def create_product(product: Product):
    result = await product_collection.insert_one(product.dict())
    return {"id": str(result.inserted_id), **product.dict()}

