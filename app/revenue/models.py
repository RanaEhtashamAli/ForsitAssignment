from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship

from app.core.models import BaseModel


class Revenue(BaseModel):
    __tablename__ = "revenues"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    sale_id = Column(Integer, ForeignKey("sales.id"))
    sale = relationship("Sale", back_populates="revenues")

    @property
    def amount(self):
        return sum(
            product.price * sales_product.quantity
            for sales_product in self.sale.sales_products
            if self.sale.products
            for product in self.sale.products
        ) if self.sale else 0.0
