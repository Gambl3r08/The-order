from pydantic import BaseModel
from datetime import datetime


class OrderTypeBase(BaseModel):
    type_name: str

    class Config:
        from_attributes = True


class OrderTypeCreate(OrderTypeBase):
    pass


class OrderTypeResponse(BaseModel):
    order_type_id: int
    type_name: str
    active: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
