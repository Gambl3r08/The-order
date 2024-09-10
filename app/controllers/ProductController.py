from sqlalchemy.orm import Session
from app.models.Product import Product
from app.schemas.ProductSchema import ProductResponse
from app.schemas.ProductSchema import ProductCreate
import uuid


class ProductController:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, product: ProductCreate):
        db_product = Product(**product.dict())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return ProductResponse.model_validate(db_product)

    def get_products(self):
        products = self.db.query(Product).filter(Product.active == 1).all()
        return products

    def get_product_by_id(self, product_id: uuid.UUID):
        product = self.db.query(
            Product).filter(Product.product_id == product_id).first()
        return product

    def update_product(self, product_id: uuid.UUID, product: ProductCreate):
        db_product = self.db.query(
            Product).filter(Product.product_id == product_id).first()
        if not db_product:
            return None
        db_product.product_name = product.product_name
        db_product.price = product.price
        db_product.description = product.description
        db_product.stock = product.stock
        db_product.quantity = product.quantity
        self.db.commit()
        self.db.refresh(db_product)
        return ProductResponse.model_validate(db_product)

    def delete_product(self, product_id: uuid.UUID):
        db_product = self.db.query(
            Product).filter(Product.product_id == product_id).first()
        if not db_product:
            return None
        self.db.delete(db_product)
        self.db.commit()
        return db_product
