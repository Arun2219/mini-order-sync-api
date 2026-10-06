from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.core.security import verify_api_key
from app.db.database import get_db
from app.db.models.order import Order
from app.schemas.order import OrderResponse

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)


@router.get(
    "",
    dependencies=[Depends(verify_api_key)],
)
def get_orders(
    status: str | None = None,
    page: int = 1,
    page_size: int = 10,
    db: Session = Depends(get_db),
):
    query = db.query(Order)

    if status:
        query = query.filter(Order.status == status)

    skip = (page - 1) * page_size

    orders = (
        query
        .order_by(Order.id)
        .offset(skip)
        .limit(page_size)
        .all()
    )

    return orders


@router.get(
    "/{order_number}",
    response_model=OrderResponse,
    dependencies=[Depends(verify_api_key)],
)
def get_order(
    order_number: str,
    db: Session = Depends(get_db),
):
    order = (
        db.query(Order)
        .filter(Order.order_number == order_number)
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found",
        )

    return order