from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session

from app.core.security import verify_api_key
from app.db.database import get_db
from app.schemas.order import OrderCreate
from app.services.order_service import create_order
from app.workers.sync_worker import sync_pending_orders

router = APIRouter(
    prefix="/webhooks",
    tags=["Webhooks"],
)


@router.post(
    "/orders",
    dependencies=[Depends(verify_api_key)],
)
def receive_order(
    order: OrderCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    saved_order = create_order(
        db=db,
        order_data=order,
    )
    background_tasks.add_task(sync_pending_orders)

    return {
        "message": "Order received",
        "order_number": saved_order.order_number,
    }
