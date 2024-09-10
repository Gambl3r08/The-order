from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


class LogBase(BaseModel):
    log_name: str = Field(..., max_length=255)
    controller_name: str = Field(..., max_length=255)
    success: int
    message: str = Field(..., max_length=255)


class LogCreate(LogBase):
    pass


class LogUpdate(LogBase):
    pass


class Log(LogBase):
    controller_log_id: UUID
    controller_name: str

    class Config:
        from_attributes = True


class LogResponse(BaseModel):
    active: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
