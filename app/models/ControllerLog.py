from app.core.db import Base
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy import Column, DateTime, Integer, String, UUID
import uuid


class ControllerLog(Base):
    __tablename__ = "controller_log"

    controller_log_id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    controller_name = Column(String(125), nullable=False)
    success = Column(Integer, nullable=False)
    message = Column(String(255), nullable=True)
    active = Column(Integer, nullable=False, server_default=str(1))
    created_at = Column(DateTime, default=current_timestamp())
    updated_at = Column(DateTime, default=current_timestamp(),
                        onupdate=current_timestamp())
