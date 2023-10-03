from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserSchema(BaseModel):
    id: int = Field(...)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: EmailStr = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "first_name": "Ehtasham",
                "last_name": "Ali",
                "email": "ranaehtashamali1@gmail.com",
            }
        }


class UserRegisterSchema(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "first_name": "Ehtasham",
                "last_name": "Ali",
                "email": "ranaehtashamali1@gmail.com",
                "password": "Password@1",
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "ranaehtashamali1@gmail.com",
                "password": "Password@1"
            }
        }
