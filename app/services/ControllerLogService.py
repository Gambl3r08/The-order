from fastapi import APIRouter, HTTPException
from app.schemas.ControllerLogSchema import LogCreate, LogResponse
from app.controllers.LogController import LogController
from app.core.db import SessionLocal
from app.utils import StatusCodes
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


router = APIRouter()


@router.post("/log", response_model=LogResponse)
async def create_controller_log(log: LogCreate):
    try:
        log_controller = LogController(SessionLocal())
        data = log_controller.create_log(log)
        if data is None:
            response = {
                "status": StatusCodes.STATUS_CODE_BAD_REQUEST,
                "message": "Product not created",
                "data": data
            }

        response = {
            "status": StatusCodes.STATUS_CODE_CREATED,
            "message": "Product created successfully",
            "data": data
        }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/log")
async def get_logs():
    try:
        log_controller = LogController(SessionLocal())
        data = log_controller.get_logs()
        if data is None:
            response = {
                "status": StatusCodes.STATUS_CODE_NOT_FOUND,
                "message": "Products not found",
                "data": data
            }
        response = {
            "status": StatusCodes.STATUS_CODE_OK,
            "message": "Products found successfully",
            "data": data
        }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/log/{log_id}")
async def get_log_by_id(log_id: str):
    try:
        log_controller = LogController(SessionLocal())
        data = log_controller.get_log_by_id(log_id)
        if data is None:
            response = {
                "status": StatusCodes.STATUS_CODE_NOT_FOUND,
                "message": "Product not found",
                "data": data
            }
        response = {
            "status": StatusCodes.STATUS_CODE_OK,
            "message": "Product found successfully",
            "data": data
        }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
