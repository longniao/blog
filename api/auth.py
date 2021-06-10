#!/usr/bin/env/ python3
# -*- coding:utf-8 -*-
"""
@Project: serve-blog
@File  :auth.py
@Author:zy7y
@Date  :2021/6/10 19:49
@Desc  :
"""

from fastapi import APIRouter, Depends

from core import security
from core.schemas import Token, Success, Fail
from db import models

auth = APIRouter(tags=["登录相关"])


@auth.post("/login", name="登录")
async def login(user: models.UserIn_Pydantic):
    try:
        user_obj = await models.User.get(username=user.username)
        if user_obj and security.verify_password(user.password, user_obj.password):
            user_token = Token(username=user_obj.username, token=security.create_access_token({"sub": user_obj.username}))
            return Success(data=user_token)
    except Exception as e:
        pass
    return Fail(msg="用户名或密码错误")


@auth.post("/logout", name="退出")
async def logout(token: str = Depends(security.get_current_user)):
    return Success(data=token)


@auth.post("/user", name="新增用户", include_in_schema=False)
async def create(user: models.UserIn_Pydantic):
    """
    - name：str
    - username： str
    - password： str
    :return: 用户除密码外的信息
    """
    user.password = security.get_password_hash(user.password)
    user_obj = await models.User.create(**user.dict(exclude_unset=True))
    # from_tortoise_orm 从 数据表中序列化
    return Success(data=await models.User_Pydantic.from_tortoise_orm(user_obj))