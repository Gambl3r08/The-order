from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional
from decimal import Decimal
from datetime import datetime


class ProductBase(BaseModel):
    product_name: str = Field(..., max_length=255)
    price: Decimal
    description: str = Field(..., max_length=255)
    stock: Optional[int] = None
    quantity: int
    active: int = Field(..., ge=0)  # Asegura que el valor sea 0 o mayor


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    product_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
