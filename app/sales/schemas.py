from typing import List

from pydantic import BaseModel, Field

from app.products.schemas import ProductListSchema
from app.revenue.schemas import RevenueListSchema


class SaleProductListSchema(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    quantity: int = Field(...)
    price: float = Field(...)


class SaleListSchema(BaseModel):
    id: int = Field(...)
    sale_date: str = Field(...)
    products: List[SaleProductListSchema]
    revenues: List[RevenueListSchema]

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "sale_date": "10-05-2023",
                "products": [
                    {
                        "id": "1",
                        "name": "Product Name",
                        "quantity": 10,
                        "price": 12.25
                    }
                ],
                "revenues": [
                    {
                        "id": 1,
                        "amount": "10.54"
                    }
                ]
            }
        }