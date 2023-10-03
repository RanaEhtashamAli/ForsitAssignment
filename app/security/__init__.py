import bcrypt
from datetime import timedelta
from fastapi_jwt import (
    JwtAccessBearerCookie,
    JwtRefreshBearer,
)

access_security = JwtAccessBearerCookie(
    secret_key="secret_key",
    auto_error=True,
    access_expires_delta=timedelta(hours=1)
)
refresh_security = JwtRefreshBearer(
    secret_key="secret_key",
    auto_error=True
)

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password.decode('utf-8')
