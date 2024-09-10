from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.schemas.OrderTypeSchema import OrderTypeResponse
from app.controllers.OrderTypeController import OrderTypeController
from app.core.db import SessionLocal
from app.utils import StatusCodes
from typing import List


router = APIRouter()


@router.post("/order-types", response_model=OrderTypeResponse)
async def create_order_type(order_type: OrderTypeResponse):
    try:
        order_type_controller = OrderTypeController(SessionLocal())
        data = order_type_controller.create_order_type(order_type)
        if data is None:
            response = {
                "status": StatusCodes.STATUS_CODE_BAD_REQUEST,
                "message": "Order type not created",
                "data": data
            }

        response = {
            "status": StatusCodes.STATUS_CODE_CREATED,
            "message": "Order type created successfully",
            "data": data
        }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/order-types", response_model=List[OrderTypeResponse])
async def get_order_types():
    try:
        order_type_controller = OrderTypeController(SessionLocal())
        data = order_type_controller.get_order_types()
        if data is None:
            response = {
                "status": StatusCodes.STATUS_CODE_NOT_FOUND,
                "message": "Order types not found",
                "data": data
            }

        response = {
            "status": StatusCodes.STATUS_CODE_OK,
            "message": "Order types found successfully",
            "data": data
        }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
