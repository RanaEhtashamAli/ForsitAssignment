from pydantic import BaseModel, Field


class RevenueListSchema(BaseModel):
    id: int = Field(...)
    amount: float = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "amount": "10.54"
            }
        }
