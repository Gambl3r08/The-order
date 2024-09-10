from app.models.OrderType import OrderType
from app.schemas.OrderTypeSchema import OrderTypeResponse
from sqlalchemy.orm import Session


class OrderTypeController:
    def __init__(self, db: Session):
        self.db = db

    def create_order_type(self, order_type: OrderType):
        db_order_type = OrderType(**order_type.dict())
        self.db.add(db_order_type)
        self.db.commit()
        self.db.refresh(db_order_type)
        return OrderTypeResponse.model_validate(db_order_type)

    def get_order_types(self):
        order_types = self.db.query(OrderType).all()
        return [OrderTypeResponse.model_validate(
            order_type) for order_type in order_types]
