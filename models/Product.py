from core.db import Base
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy import Column, DateTime, Integer, String, UUID, Numeric
import uuid


class Product(Base):
    __tablename__ = "products"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_name = Column(String(255), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    description = Column(String(255), nullable=False)
    stock = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    active = Column(Integer, nullable=False, server_default=str(1))
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(DateTime, default=current_timestamp(),
                        onupdate=current_timestamp())
