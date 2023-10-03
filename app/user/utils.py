import bcrypt


def validate_user_password(raw_password: str, encrypted_password: str) -> bool:
    if bcrypt.checkpw(raw_password.encode('utf-8'), encrypted_password.encode('utf-8')):
        return True
    return False
