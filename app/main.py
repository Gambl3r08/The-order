from fastapi import FastAPI
from app.services.ProductService import router as product_router
from app.core.db import engine, Base
from dotenv import load_dotenv

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    product_router, tags=["Products"], prefix="/api/v1")
