from sqlalchemy.orm import Session

from app.products.models import Product
from app.revenue.models import Revenue
from app.sales.models import Sale
from app.sales.schemas import SaleListSchema
from app.sales.utils import format_sales
from sqlalchemy import func, Float


def get_all_sales(db: Session):
    sales = db.query(Sale).all()
    sales_data = format_sales(sales)
    sales_res = [SaleListSchema.model_validate(data) for data in sales_data]
    return sales_res


def get_sale_by_id(sale_id: int, db: Session):
    sale = db.query(Sale).filter_by(id=sale_id).first()
    data = {
            "id": sale.id,
            "sale_date": sale.created_at.strftime("%d-%m-%Y"),
            "products": [
                {
                    "id": sale_product.product.id,
                    "name": sale_product.product.name,
                    "quantity": sale_product.quantity,
                    "price": sale_product.product.price
                }
                for sale_product in sale.sales_products
            ],
            "revenues": [
                {
                    "id": revenue.id,
                    "amount": revenue.amount
                }
                for revenue in sale.revenues
            ]
        }
    sales_res = SaleListSchema(**data)
    return sales_res


def filter_sales_query(
    start_date, end_date, min_revenue, max_revenue, product_id, db: Session
):
    query = db.query(Sale)
    if start_date:
        query = query.filter(Sale.sale_date >= start_date)
    if end_date:
        query = query.filter(Sale.sale_date <= end_date)
    if min_revenue is not None:
        query = query.filter(Sale.revenues.any(func.cast(Revenue.amount, Float) >= min_revenue))
    if max_revenue is not None:
        query = query.filter(Sale.revenues.any(func.cast(Revenue.amount, Float) <= max_revenue))
    if product_id is not None:
        query = query.filter(Sale.products.any(Product.id == product_id))
    sales_data = format_sales(query)
    sales_res = [SaleListSchema.model_validate(data) for data in sales_data]
    return sales_res

