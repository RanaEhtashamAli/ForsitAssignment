from contextlib import contextmanager
from sqlalchemy.orm import Session

from database import SessionLocal


# @contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
