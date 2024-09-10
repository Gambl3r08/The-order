from fastapi import APIRouter, HTTPException
from app.schemas.ProductSchemma import Product, ProductCreate, ProductResponse
from app.controllers.ProductController import ProductController
from app.core.db import SessionLocal
from app.utils import StatusCodes
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


router = APIRouter()


@router.post("/products", response_model=Product)
async def create_product(product: ProductCreate):
    try:
        product_controller = ProductController(SessionLocal())
        data = product_controller.create_product(product)
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
