from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.controllers.OrderStatusController import OrderStatusController
from app.schemas.OrderStatusSchema import OrderStatusResponse
from app.core.db import SessionLocal
from app.utils import StatusCodes
from typing import List


router = APIRouter()


@router.post("/order-statuses", response_model=OrderStatusResponse)
async def create_order_status(order_status: OrderStatusResponse):
    try:
        order_status_controller = OrderStatusController(SessionLocal())
        data = order_status_controller.create_order_status(order_status)
        if data is None:
            response = {
                "status": StatusCodes.STATUS_CODE_BAD_REQUEST,
                "message": "Order status not created",
                "data": data
            }

        response = {
            "status": StatusCodes.STATUS_CODE_CREATED,
            "message": "Order status created successfully",
            "data": data
        }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/order-statuses", response_model=List[OrderStatusResponse])
async def get_order_statuses():
    try:
        order_status_controller = OrderStatusController(SessionLocal())
        data = order_status_controller.get_order_statuses()
        if data is None:
            response = {
                "status": StatusCodes.STATUS_CODE_NOT_FOUND,
                "message": "Order statuses not found",
                "data": data
            }

        response = {
            "status": StatusCodes.STATUS_CODE_OK,
            "message": "Order statuses found successfully",
            "data": data
        }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
