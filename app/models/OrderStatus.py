from core.db import Base
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy import Column, DateTime, Integer, String


class OrderStatus(Base):
    __tablename__ = "orders_status"

    order_status_id = Column(
        Integer, primary_key=True, autoincrement=True)
    status_name = Column(String(100), nullable=False)
    active = Column(Integer, nullable=False, server_default=str(1))
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(DateTime, default=current_timestamp(),
                        onupdate=current_timestamp())
