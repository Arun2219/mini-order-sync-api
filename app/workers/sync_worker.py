from datetime import datetime, timezone

from app.db.database import SessionLocal
from app.db.models.order import Order
from app.services.erp_service import send_order_to_erp


def sync_pending_orders():
    db = SessionLocal()

    try:
        orders = (
            db.query(Order)
            .filter(Order.status == "Pending")
            .all()
        )

        for order in orders:
            for attempt in range(1, 4):
                try:
                    send_order_to_erp(order)

                    now = datetime.now(timezone.utc).replace(tzinfo=None)

                    order.status = "Synced"
                    order.synced_at_utc = now
                    order.updated_at_utc = now
                    order.error_message = None

                    db.commit()

                    break

                except Exception as e:
                    order.retry_count += 1
                    order.error_message = str(e)
                    order.updated_at_utc = (
                        datetime.now(timezone.utc).replace(tzinfo=None)
                    )

                    if order.retry_count >= 3:
                        order.status = "Failed"

                    db.commit()

                    if order.retry_count >= 3:
                        break

    finally:
        db.close()


if __name__ == "__main__":
    sync_pending_orders()