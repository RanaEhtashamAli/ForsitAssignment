from datetime import timedelta
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi_jwt import JwtAuthorizationCredentials
from sqlalchemy.orm import Session

from app.security import access_security, refresh_security
from app.user.crud import get_users, get_user_from_email, create_user as register_user
from app.user.schemas import UserSchema, UserRegisterSchema, UserLoginSchema
from app.user.utils import validate_user_password
from database.session import get_db

router = APIRouter()


@router.get("/", response_model=List[UserSchema])
def read_user(db: Session = Depends(get_db),
              credentials: JwtAuthorizationCredentials = Security(access_security)) -> List[UserSchema]:
    users = get_users(db)
    return users


@router.post("/register/", response_model=UserSchema)
def create_user(data: UserRegisterSchema, db: Session = Depends(get_db)):
    if get_user_from_email(data.email, db):
        raise HTTPException(status_code=400, detail="User with this email already exists")
    user = register_user(data, db=db)
    return user


@router.post("/login/")
def create_user(data: UserLoginSchema, db: Session = Depends(get_db)):
    user = get_user_from_email(data.email, db)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password provided.")
    valid_password = validate_user_password(data.password, user.password)
    if not valid_password:
        raise HTTPException(status_code=400, detail="Invalid email or password provided.")
    subject = {"id": user.id}
    access_token = access_security.create_access_token(subject=subject, expires_delta=timedelta(hours=1))
    refresh_token = refresh_security.create_refresh_token(subject=subject, expires_delta=timedelta(days=2))

    return {"access_token": access_token, "refresh_token": refresh_token}


@router.post("/refresh/")
def refresh(
        credentials: JwtAuthorizationCredentials = Security(refresh_security)
):
    access_token = access_security.create_access_token(subject=credentials.subject, expires_delta=timedelta(hours=1))
    refresh_token = refresh_security.create_refresh_token(subject=credentials.subject, expires_delta=timedelta(days=2))

    return {"access_token": access_token, "refresh_token": refresh_token}
