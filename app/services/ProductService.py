from fastapi import APIRouter, HTTPException
from app.schemas.ProductSchema import Product, ProductCreate
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


@router.get("/products")
async def get_products():
    try:
        product_controller = ProductController(SessionLocal())
        data = product_controller.get_products()
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


@router.put("/products/{product_id}")
async def update_product(product_id: str, product: ProductCreate):
    try:
        product_controller = ProductController(SessionLocal())
        data = product_controller.update_product(product_id, product)
        if data is None:
            response = {
                "status": StatusCodes.STATUS_CODE_NOT_FOUND,
                "message": "Product not found",
                "data": data
            }
        response = {
            "status": StatusCodes.STATUS_CODE_OK,
            "message": "Product updated successfully",
            "data": data
        }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/products/{product_id}")
async def delete_product(product_id: str):
    try:
        product_controller = ProductController(SessionLocal())
        data = product_controller.delete_product(product_id)
        if data is None:
            response = {
                "status": StatusCodes.STATUS_CODE_NOT_FOUND,
                "message": "Product not found",
                "data": data
            }
        response = {
            "status": StatusCodes.STATUS_CODE_OK,
            "message": "Product deleted successfully",
            "data": data
        }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
