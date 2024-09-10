from pydantic import BaseModel, UUID4
from datetime import datetime


class RestaurantBase(BaseModel):
    restaurant_name: str
    restaurant_email: str
    restaurant_passwd: str

    class Config:
        from_attributes = True


class RestaurantCreate(BaseModel):
    pass


class RestaurantResponse(BaseModel):
    restaurant_id: UUID4
    restaurant_name: str
    restaurant_email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
