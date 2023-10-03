from pydantic import BaseModel, Field, computed_field


class ProductListSchema(BaseModel):
    id: int = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    price: float = Field(...)
    available_quantity: int = Field(...)
    has_low_stock: bool = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Product 1",
                "last_name": "Description 1",
                "price": 5.012,
                "available_quantity": 10,
                "has_low_stock": True,
            }
        }


class ProductQuantityUpdateIn(BaseModel):
    quantity_to_add: int = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "quantity_to_add": 1,
            }
        }


class ProductInventoryHistoryListSchema(BaseModel):
    product_name: str = Field(...)
    quantity_change: int = Field(...)
    new_quantity: int = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "product_name": "Product name",
                "quantity_change": 1,
                "new_quantity": 2
            }
        }
