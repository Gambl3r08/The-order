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
    order_status = Column(Integer, nullable=False, default=0)
    observations = Column(String(255), nullable=True)
    shipping = Column(Integer, nullable=False)
    active = Column(Integer, nullable=False, server_default=str(1))
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(DateTime, default=current_timestamp(),
                        onupdate=current_timestamp())
