from sqlalchemy.orm import Session
from app.models.Order import Order
from app.models.SubOrder import SubOrder
from app.schemas.OrderSchema import OrderResponse, OrderCreate, OrderUpdate
from app.schemas.SubOrderSchema import SubOrderCreate
import uuid


class OrderController:
    def __init__(self, db: Session):
        self.db = db

    def create_order(self, order: OrderCreate):
        order_data = order.dict(exclude={'products'})
        db_order = Order(**order_data)
        self.db.add(db_order)
        self.db.commit()
        self.db.refresh(db_order)

        for item in order.products:
            sub_order = SubOrder(
                order_id=db_order.order_id,
                product_id=item.product_id,
                quantity=item.quantity
            )
            self.db.add(sub_order)

        self.db.commit()
        self.db.refresh(db_order)

        return OrderResponse.model_validate(db_order)
