from app.core.db import Base
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy import (
    Column, DateTime, Integer, String, UUID, Text)
import uuid


class Restaurant(Base):
    __tablename__ = "restaurants"

    restaurant_id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    restaurant_name = Column(String(255), nullable=False)
    restaurant_email = Column(String(255), nullable=False)
    restaurant_passwd = Column(Text, nullable=False)
    active = Column(Integer, nullable=False, server_default=str(1))
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(DateTime, default=current_timestamp(),
                        onupdate=current_timestamp())
