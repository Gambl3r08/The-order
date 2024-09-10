from pydantic import BaseModel
from datetime import datetime


class OrderStatus(BaseModel):
    status_name: str

    class Config:
        from_attributes = True


class OrderTypeCreate(OrderStatus):
    pass


class OrderStatusResponse(BaseModel):
    order_status_id: int
    status_name: str
    active: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
