from app.core.db import Base
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy import Column, DateTime, Integer, UUID
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
    quantity = Column(Integer, nullable=False)
    active = Column(Integer, nullable=False, server_default=str(1))
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(DateTime, default=current_timestamp(),
                        onupdate=current_timestamp())
