from datetime import datetime, timedelta
from typing import Optional

from jose import jwt
# hash 密码库
from passlib.context import CryptContext
from starlette.exceptions import HTTPException
from starlette.requests import Request

from config import setting

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """使用哈希算法加密密码"""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """验证密码与hash密码"""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(username: str, expires_delta: Optional[timedelta] = None):
    to_encode = {"sub": username}.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, setting.SECRET_KEY, algorithm=setting.ALGORITHM)
    return encoded_jwt


async def check_token(request: Request):
    credentials_exception = HTTPException(
        status_code=401,
        detail="认证失败",
    )
    try:
        token = request.headers.get("Authorization")
        payload = jwt.decode(token, setting.SECRET_KEY, algorithms=[setting.ALGORITHM])
        username: str = payload.get("sub")
        if username == setting.username:
            pass
        else:
            raise credentials_exception
    except jwt.JWTError:
        raise credentials_exception


if __name__ == '__main__':
    print(get_password_hash("123456"))