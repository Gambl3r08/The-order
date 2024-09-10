from pydantic import BaseModel, UUID4
from uuid import UUID
from typing import List
from datetime import datetime

class SubOrderBase(BaseModel):
    order_id: UUID
    product_id: UUID
    quantity: int

    class Config:
        from_attributes = True


class SubOrderCreate(BaseModel):
    order_id: UUID
    product_id: UUID
    quantity: int

    class Config:
        from_attributes = True


class SubOrderResponse(BaseModel):
    sub_order_id: UUID4
    order_id: UUID4
    product_id: UUID4
    quantity: int

    class Config:
        from_attributes = True
