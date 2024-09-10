from pydantic import BaseModel
from uuid import UUID
from typing import List


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
