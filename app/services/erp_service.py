import random

from app.db.models.order import Order


def send_order_to_erp(order: Order) -> None:
    success = random.random() >= 0.2

    if not success:
        raise Exception("Fake ERP sync failed")

    print(f">>> Order {order.order_number} synced to ERP")