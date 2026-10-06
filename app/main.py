from fastapi import FastAPI

from app.api.routes.webhooks import router as webhook_router
from app.api.routes.orders import router as orders_router


app = FastAPI(
    title="Mini Order Sync API",
    version="1.0.0",
)


app.include_router(webhook_router)
app.include_router(orders_router)


@app.get("/")
def root():
    return {
        "message": "Mini Order Sync API is running"
    }