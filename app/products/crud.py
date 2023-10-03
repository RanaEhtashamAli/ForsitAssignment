from sqlalchemy.orm import Session

from app.products.models import Product, InventoryHistory
from app.products.schemas import ProductListSchema


def get_all_products(db: Session):
    products = db.query(Product).all()
    product_schemas = [ProductListSchema(id=product.id, name=product.name, description=product.description,
                                         price=product.price, available_quantity=product.inventory.quantity,
                                         has_low_stock=product.inventory.quantity <= 10) for product in products]
    return product_schemas


def create_inventory_history(prod_id: int, previous_quantity, quantity_to_add, db: Session) -> None:
    inventory_history = InventoryHistory(product_id=prod_id, quantity_change=quantity_to_add,
                                         new_quantity=previous_quantity+quantity_to_add)
    db.add(inventory_history)
    db.commit()


def get_product_by_id(prod_id: int, db: Session):
    return db.query(Product).filter_by(id=prod_id).first()
