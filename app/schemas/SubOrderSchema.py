from pydantic import BaseModel, UUID4
from uuid import UUID
from typing import Optional


class SubOrderBase(BaseModel):
    product_id: UUID
    quantity: int
    extra: Optional[str]

    class Config:
        from_attributes = True


class SubOrderCreate(BaseModel):
    order_id: UUID
    product_id: UUID
    quantity: int
    extra: Optional[str]

    class Config:
        from_attributes = True


class SubOrderResponse(BaseModel):
    sub_order_id: UUID4
    order_id: UUID4
    product_id: UUID4
    quantity: int
    extra: Optional[str]

    class Config:
        from_attributes = True
