from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.core.models import BaseModel
from app.sales.models import SalesProduct


class Product(BaseModel):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(length=255), unique=True, index=True)
    description = Column(String(length=1000))
    price = Column(Float)

    inventory = relationship("Inventory", back_populates="product", uselist=False)

    sales = relationship("Sale", secondary="sales_products", back_populates="products")


class Inventory(BaseModel):
    __tablename__ = "inventories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    quantity = Column(Integer)

    product_id = Column(Integer, ForeignKey("products.id"), unique=True)
    product = relationship("Product", back_populates="inventory")


class InventoryHistory(BaseModel):
    __tablename__ = "inventory_history"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product", backref="inventory_history")
    quantity_change = Column(Integer)
    new_quantity = Column(Integer)

