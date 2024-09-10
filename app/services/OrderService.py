from fastapi import APIRouter, HTTPException
from app.schemas.OrderSchema import OrderResponse, OrderCreate
from app.controllers.OrderController import OrderController
from app.core.db import SessionLocal
from app.utils import StatusCodes
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


router = APIRouter()


@router.post("/orders", response_model=OrderCreate)
async def create_order(order: OrderCreate):
    try:
        order_controller = OrderController(SessionLocal())
        data = order_controller.create_order(order)
        if data is None:
            response = {
                "status": StatusCodes.STATUS_CODE_BAD_REQUEST,
                "message": "Order not created",
                "data": data
            }

        response = {
            "status": StatusCodes.STATUS_CODE_CREATED,
            "message": "Order created successfully",
            "data": data
        }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
