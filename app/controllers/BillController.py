from sqlalchemy.orm import Session
from app.models.SubOrder import SubOrder
from app.models.Product import Product
from decimal import Decimal
import uuid

IVA = 0.19


class BillController:
    def __init__(self, db: Session):
        self.db = db

    def get_total(self, order_id: uuid.UUID):
        subtotal = Decimal(0)

        query = (
            self.db.query(
                SubOrder.sub_order_id,
                SubOrder.order_id,
                SubOrder.quantity,
                SubOrder.observation,
                SubOrder.created_at,
                SubOrder.updated_at,
                Product.product_id,
                Product.product_name,
                Product.price,
                Product.description
            )
            .join(Product, SubOrder.product_id == Product.product_id)
            .filter(
                SubOrder.active == 1,
                Product.active == 1,
                SubOrder.order_id == order_id
            )
        )
        results = query.all()

        for result in results:
            subtotal += result.price * Decimal(result.quantity)

        total = subtotal + (subtotal * Decimal(IVA))

        response = {
            "subtotal": float(subtotal),
            "total": float(total)
        }
        return response

    def get_bill(self, order_id: uuid.UUID):
        data = {}
        products = []
        query = (
            self.db.query(
                SubOrder.sub_order_id,
                SubOrder.order_id,
                SubOrder.quantity,
                SubOrder.observation,
                SubOrder.created_at,
                SubOrder.updated_at,
                Product.product_id,
                Product.product_name,
                Product.price,
                Product.description
            )
            .join(Product, SubOrder.product_id == Product.product_id)
            .filter(
                SubOrder.active == 1,
                Product.active == 1,
                SubOrder.order_id == order_id
            )
        )
        results = query.all()

        for result in results:
            product_data = {
                "sub_order_id": str(result.sub_order_id),
                "order_id": str(result.order_id),
                "quantity": result.quantity,
                "observation": result.observation,
                "created_at": result.created_at.isoformat(),
                "updated_at": result.updated_at.isoformat(),
                "product_id": str(result.product_id),
                "product_name": result.product_name,
                "price": float(result.price),
                "description": result.description
            }
            products.append(product_data)

        data["products"] = products
        total_data = self.get_total(order_id)
        data["sub_total"] = total_data["subtotal"]
        data["total"] = total_data["total"]
        data["IVA"] = IVA

        return data
