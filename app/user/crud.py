from pydantic import EmailStr
from sqlalchemy.orm import Session

from app.user.models import User
from app.user.schemas import UserSchema, UserRegisterSchema


def get_users(db: Session):
    users = db.query(User).all()
    user_schemas = [UserSchema(id=user.id, email=user.email, first_name=user.first_name, last_name=user.last_name)
                    for user in users]
    return user_schemas


def get_user_from_email(email: EmailStr, db: Session):
    user = db.query(User).filter_by(email=email).first()
    return user


def create_user(user: UserRegisterSchema, db: Session):
    user_obj = User(email=user.email, first_name=user.first_name, last_name=user.last_name)
    user_obj.set_password(user.password)
    db.add(user_obj)
    db.commit()
    user_schema = UserSchema(id=user_obj.id, email=user.email, first_name=user.first_name, last_name=user.last_name)
    return user_schema



