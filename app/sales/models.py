from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.core.models import BaseModel
from app.revenue.models import Revenue


class SalesProduct(BaseModel):
    __tablename__ = "sales_products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sale_id = Column(Integer, ForeignKey("sales.id"))
    sale = relationship("Sale", backref="sales_products")
    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product", backref="sales_products")
    quantity = Column(Integer)


class Sale(BaseModel):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sale_date = Column(DateTime, default=datetime.utcnow)

    products = relationship("Product", secondary="sales_products", back_populates="sales")

    revenues = relationship("Revenue", back_populates="sale")
