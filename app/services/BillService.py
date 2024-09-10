from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.controllers.BillController import BillController
from app.core.db import SessionLocal
from app.utils import StatusCodes
import uuid

router = APIRouter()


@router.get("/bills/{order_id}")
async def get_bill_by_order_id(order_id: uuid.UUID):
    try:
        bill_controller = BillController(SessionLocal())
        data = bill_controller.get_bill(order_id)
        if data is None:
            response = {
                "status": StatusCodes.STATUS_CODE_NOT_FOUND,
                "message": "Bill not found",
                "data": data
            }
        response = {
            "status": StatusCodes.STATUS_CODE_OK,
            "message": "Bill found successfully",
            "data": data
        }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
