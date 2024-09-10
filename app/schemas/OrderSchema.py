from pydantic import BaseModel, Field, UUID4
from uuid import UUID
from datetime import datetime
from typing import List, Optional
from app.schemas.SubOrderSchema import SubOrderBase, SubOrderResponse


class OrderBase(BaseModel):
    customer_name: str = Field(..., max_length=255)
    order_status: int
    observations: str = Field(..., max_length=255)
    shipping: int


class OrderCreate(OrderBase):
    products: List[SubOrderBase]


class OrderUpdate(OrderBase):
    pass


class OrderResponse(BaseModel):
    order_id: UUID
    customer_name: str
    order_status: int
    observations: str
    shipping: int
    active: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class OrderGetResponse(BaseModel):
    order_id: UUID4
    customer_name: str
    order_status: int
    observations: Optional[str]
    shipping: int
    created_at: datetime
    updated_at: datetime
    sub_orders: List[SubOrderResponse] = []

    class Config:
        from_attributes = True
