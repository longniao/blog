from typing import Any, Dict, Generic, Optional, TypeVar

from pydantic import BaseModel, generics

DataT = TypeVar("DataT")


class LogModel(BaseModel):
    host: str
    method: str
    url: str
    headers: Optional[Dict[str, Any]]
    status_code: int = 502


class LogDBModel(LogModel):
    id: int

    class Config:
        orm_mode = True


class Response(generics.GenericModel, Generic[DataT]):
    code: int = 200
    msg: str = "ok"
    data: Optional[DataT]
    total: Optional[int] = None


class LoginForm(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "Bearer"
