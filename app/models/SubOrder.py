from app.core.db import Base
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy import Column, DateTime, Integer, UUID, String
import uuid

CREATE = 0
IN_PREPARATION = 1
DELIVERED = 2


class SubOrder(Base):
    __tablename__ = "sub_orders"

    sub_order_id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_id = Column(
        UUID(as_uuid=True), default=uuid.uuid4)
    product_id = Column(
        UUID(as_uuid=True), default=uuid.uuid4)
    observation = Column(String(255), nullable=True)
    quantity = Column(Integer, nullable=False)
    active = Column(Integer, nullable=False, server_default=str(1))
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(DateTime, default=current_timestamp(),
                        onupdate=current_timestamp())

    def __repr__(self):
        return (
            f"SubOrder(sub_order_id={self.sub_order_id!r}, "
            f"order_id={self.order_id!r}, "
            f"product_id={self.product_id!r}, "
            f"observation={self.observation!r}, "
            f"quantity={self.quantity!r}, "
            f"active={self.active!r}, "
            f"created_at={self.created_at!r}, "
            f"updated_at={self.updated_at!r})"
        )

    def __str__(self):
        return (
            f"SubOrder ID: {self.sub_order_id}, "
            f"Order ID: {self.order_id}, "
            f"Product ID: {self.product_id}, "
            f"Extras: {self.observation}, "
            f"Quantity: {self.quantity}, "
            f"Active: {self.active}, "
            f"Created At: {self.created_at}, "
            f"Updated At: {self.updated_at}"
        )
