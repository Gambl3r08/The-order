from fastapi import FastAPI
from app.services.ProductService import router as product_router
from app.services.ControllerLogService import router as log_router
from app.core.db import engine, Base
from dotenv import load_dotenv

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    product_router, tags=["Products"], prefix="/api/v1")
app.include_router(
    log_router, tags=["Logs"], prefix="/api/v1"
)
