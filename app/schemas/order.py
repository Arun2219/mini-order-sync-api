from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, EmailStr, Field


class OrderItemCreate(BaseModel):
    sku: str = Field(min_length=1)
    qty: int = Field(gt=0)
    price: Decimal = Field(ge=0)


class OrderCreate(BaseModel):
    order_number: str = Field(min_length=1)
    customer_name: str = Field(min_length=1)
    email: EmailStr
    items: list[OrderItemCreate] = Field(min_length=1)
    total: Decimal = Field(ge=0)
    currency: str = Field(min_length=3, max_length=3)


class OrderLineResponse(BaseModel):
    sku: str
    product_name: str
    quantity: int
    unit_price: Decimal
    total_price: Decimal


class OrderResponse(BaseModel):
    id: int
    order_number: str
    customer_name: str
    customer_email: EmailStr
    total_amount: Decimal
    status: str
    retry_count: int
    error_message: str | None
    created_at_utc: datetime
    updated_at_utc: datetime
    synced_at_utc: datetime | None
    lines: list[OrderLineResponse]

    model_config = {
        "from_attributes": True
    }