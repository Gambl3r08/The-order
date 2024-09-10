from sqlalchemy.orm import Session
from app.models.Order import Order
from app.models.SubOrder import SubOrder
from app.schemas.OrderSchema import (
    OrderResponse, OrderCreate, OrderUpdate, OrderGetResponse)
from app.schemas.SubOrderSchema import SubOrderResponse
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
                quantity=item.quantity,
                observation=item.observation
            )
            self.db.add(sub_order)

        self.db.commit()
        self.db.refresh(db_order)

        return OrderResponse.model_validate(db_order)

    def get_orders(self):
        # import pdb
        # pdb.set_trace()
        orders = self.db.query(Order).filter(Order.active == 1).all()
        for order in orders:
            sub_orders = self.db.query(
                SubOrder).filter(SubOrder.order_id == order.order_id).all()
            order.sub_orders = [
                SubOrderResponse.model_validate(
                    sub_order) for sub_order in sub_orders]

        return [OrderGetResponse.model_validate(order) for order in orders]

    def update_order_status(self, order_id: uuid.UUID, order: OrderUpdate):
        db_order = self.db.query(
            Order).filter(Order.order_id == order_id).first()
        if not db_order:
            return None
        db_order.order_status = order.order_status
        self.db.commit()
        self.db.refresh(db_order)
        return OrderResponse.model_validate(db_order)
