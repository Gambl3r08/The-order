from sqlalchemy.orm import Session
from app.models.Product import Product
from app.schemas.ProductSchemma import ProductResponse
from app.schemas.ProductSchemma import ProductCreate


class ProductController:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, product: ProductCreate):
        db_product = Product(**product.dict())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return ProductResponse.model_validate(db_product)
