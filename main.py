from fastapi import FastAPI
from routes.product import router as product_router
from routes.orders import router as order_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend running"}

app.include_router(product_router)
app.include_router(order_router)
