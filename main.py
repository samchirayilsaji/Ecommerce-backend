from fastapi import FastAPI
from routes.product import router as product_router
from routes.orders import router as order_router


app = FastAPI()

app.include_router(product_router)
app.include_router(order_router)
