from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql.functions import now

from app.security import hash_password
from database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(length=255), unique=True, index=True)
    first_name = Column(String(length=50), nullable=True)
    last_name = Column(String(length=50), nullable=True)
    password = Column(String(length=255), nullable=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=now())

    def set_password(self, raw_password: str):
        self.password = hash_password(raw_password)

    class Config:
        orm_mode = True
