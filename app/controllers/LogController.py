from sqlalchemy.orm import Session
from app.models.ControllerLog import ControllerLog
from app.schemas.ControllerLogSchema import LogResponse, LogCreate, Log
import uuid


class LogController:
    def __init__(self, db: Session):
        self.db = db

    def create_log(self, log: LogCreate):
        db_log = ControllerLog(**log.dict())
        self.db.add(db_log)
        self.db.commit()
        self.db.refresh(db_log)
        return LogResponse.model_validate(db_log)

    def get_logs(self):
        products = self.db.query(Log).filter(Log.active == 1).all()
        return products

    def get_log_by_id(self, product_id: uuid.UUID):
        product = self.db.query(
            ControllerLog).filter(
                ControllerLog.controller_log_id == product_id).first()
        return product
