from sqlalchemy.orm import Session
from app.models.OrderStatus import OrderStatus
from app.schemas.OrderStatusSchema import OrderStatusResponse


class OrderStatusController:
    def __init__(self, db: Session):
        self.db = db

    def create_order_status(self, order_status: OrderStatus):
        db_order_status = OrderStatus(**order_status.dict())
        self.db.add(db_order_status)
        self.db.commit()
        self.db.refresh(db_order_status)
        return OrderStatusResponse.model_validate(db_order_status)

    def get_order_statuses(self):
        order_statuses = self.db.query(OrderStatus).filter(
            OrderStatus.active == 1
        ).all()
        return [OrderStatusResponse.model_validate(
            order_status) for order_status in order_statuses]
