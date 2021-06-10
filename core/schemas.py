#!/usr/bin/env/ python3
# -*- coding:utf-8 -*-
"""
@Project: blog
@File  :schemas.py
@Author:zy7y
@Date  :2021/6/10 21:30
@Desc  :
"""
from typing import Any

from pydantic import BaseModel


class Response(BaseModel):
    code: int
    data: Any = None
    msg: str = "请求成功."


class Success(Response):
    code = 200


class Fail(Response):
    code = 400
    msg = "请求失败."


class Token(BaseModel):
    username: str
    token: str
