from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.schemas.RestaurantSchema import Restaurant, RestaurantCreate
from app.controllers.RestaurantController import RestaurantController
from app.core.db import SessionLocal
from app.utils import StatusCodes


router = APIRouter()


@router.post("/restaurants", response_model=Restaurant)
async def create_restaurant(restaurant: RestaurantCreate):
    try:
        restaurant_controller = RestaurantController(SessionLocal())
        data = restaurant_controller.create_restaurant(restaurant)
        if data is None:
            response = {
                "status": StatusCodes.STATUS_CODE_BAD_REQUEST,
                "message": "Restaurant not created",
                "data": data
            }

        response = {
            "status": StatusCodes.STATUS_CODE_CREATED,
            "message": "Restaurant created successfully",
            "data": data
        }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/restaurants")
async def get_tokens():
    pass
