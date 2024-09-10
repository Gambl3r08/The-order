from app.core.db import Base
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy import Column, DateTime, Integer, String, UUID
import uuid

CREATE = 0
IN_PREPARATION = 1
DELIVERED = 2


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_name = Column(String(255), nullable=False)
    order_status = Column(Integer, nullable=False, server_default=str(0))
    shipping = Column(Integer, nullable=False)
    active = Column(Integer, nullable=False, server_default=str(1))
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(DateTime, default=current_timestamp(),
                        onupdate=current_timestamp())

    def __repr__(self):
        return (f"Order(order_id={self.order_id!r}, "
                f"customer_name={self.customer_name!r}, "
                f"order_status={self.order_status!r}, "
                f"shipping={self.shipping!r}, "
                f"created_at={self.created_at!r}, "
                f"updated_at={self.updated_at!r})")

    def __str__(self):
        return (f"Order ID: {self.order_id}, "
                f"Customer Name: {self.customer_name}, "
                f"Order Status: {self.order_status}, "
                f"Shipping: {self.shipping}, "
                f"Created At: {self.created_at}, "
                f"Updated At: {self.updated_at}")
