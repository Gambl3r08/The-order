from sqlalchemy.orm import Session
from app.models.Restaurant import Restaurant
from app.schemas.RestaurantSchema import RestaurantResponse, RestaurantCreate
import uuid


class RestaurantController:
    def __init__(self, db: Session):
        self.db = db

    def create_restaurant(self, restaurant: RestaurantCreate):
        db_restaurant = Restaurant(**restaurant.dict())
        self.db.add(db_restaurant)
        self.db.commit()
        self.db.refresh(db_restaurant)
        return RestaurantResponse.model_validate(db_restaurant)

    def get_restaurants(self):
        restaurants = self.db.query(
            Restaurant).filter(Restaurant.active == 1).all()
        return restaurants

    def get_restaurant_by_id(self, restaurant_id: uuid.UUID):
        restaurant = self.db.query(
            Restaurant).filter(
                Restaurant.restaurant_id == restaurant_id).filter(
                    Restaurant.active == 1).first()
        return restaurant

    def update_restaurant(self, restaurant_id: uuid.UUID,
                          restaurant: RestaurantCreate):
        db_restaurant = self.db.query(
            Restaurant).filter(
                Restaurant.restaurant_id == restaurant_id).first()
        if not db_restaurant:
            return None
        db_restaurant.restaurant_name = restaurant.restaurant_name
        db_restaurant.restaurant_email = restaurant.restaurant_email
        db_restaurant.restaurant_passwd = restaurant.restaurant_passwd
        self.db.commit()
        self.db.refresh(db_restaurant)
        return RestaurantResponse.model_validate(db_restaurant)

    def delete_restaurant(self, restaurant_id: uuid.UUID):
        db_restaurant = self.db.query(
            Restaurant).filter(
                Restaurant.restaurant_id == restaurant_id).first()
        if not db_restaurant:
            return None
        self.db.delete(db_restaurant)
        self.db.commit()
        return db_restaurant
