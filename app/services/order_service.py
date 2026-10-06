from fastapi import HTTPException
from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.db.models.order import Order, OrderLine
from app.schemas.order import OrderCreate


def create_order(
    db: Session,
    order_data: OrderCreate,
) -> Order:

    print(">>> create_order() CALLED")

    existing_order = (
        db.query(Order).filter(Order.order_number == order_data.order_number).first()
    )

    if existing_order:
        raise HTTPException(
            status_code=409,
            detail="Order number already exists",
        )

    now = datetime.now(timezone.utc).replace(tzinfo=None)

    order = Order(
        order_number=order_data.order_number,
        customer_name=order_data.customer_name,
        customer_email=str(order_data.email),
        total_amount=order_data.total,
        status="Pending",
        retry_count=0,
        created_at_utc=now,
        updated_at_utc=now,
    )

    for item in order_data.items:
        line = OrderLine(
            sku=item.sku,
            product_name=item.sku,
            quantity=item.qty,
            unit_price=item.price,
            total_price=item.price * item.qty,
        )

        order.lines.append(line)

    db.add(order)
    db.commit()
    db.refresh(order)

    return order
