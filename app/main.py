from fastapi import FastAPI
from app.services.ProductService import router as product_router
from app.services.ControllerLogService import router as log_router
from app.services.OrderService import router as order_router
from app.core.db import engine, Base
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    product_router, tags=["Products"], prefix="/api/v1")
app.include_router(
    log_router, tags=["Logs"], prefix="/api/v1"
)
app.include_router(
    order_router, tags=["Orders"], prefix="/api/v1"
)
