from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import List
from app.schemas.SubOrderSchema import SubOrderBase


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
