from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional
from decimal import Decimal
from datetime import datetime


class ProductBase(BaseModel):
    product_name: str = Field(..., max_length=255)
    price: Decimal
    description: str = Field(..., max_length=255)
    extras: Optional[str]


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    product_id: UUID
    product_name: str

    class Config:
        from_attributes = True


class ProductResponse(BaseModel):
    product_id: UUID
    product_name: str
    price: Decimal
    description: str
    extras: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
