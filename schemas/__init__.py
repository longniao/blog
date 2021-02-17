#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog
@file: response.py
@author: zy7y
@time: 2021/1/30
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
定义response响应模型
"""
from typing import Any

from pydantic import BaseModel


class Token(BaseModel):
    # token_type: str = "bearer"
    # access_token: str
    token: str


class Auth(BaseModel):
    username: str = "yan22"
    password: str = "S$V0CLeH_$"


class ResponseBase(BaseModel):
    data: Any = None


class Response200(ResponseBase):
    code = 200
    msg = "操作成功."


class Response404(ResponseBase):
    code = 404
    msg = "Not Found"
