#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog
@file: auth.py
@author: zy7y
@time: 2021/1/31
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
登录认证
"""
from typing import Union

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from db import Admin
from core import deps, security
from core.security import create_access_token
from schemas import Token, Response200, Response404

auth_router = APIRouter(tags=["登录"])


@auth_router.post("/auth", name="管理员登录", response_model=Union[Response200, Response404])
async def admin_login(
        db: Session = Depends(deps.get_db),
        form_data: OAuth2PasswordRequestForm = Depends()
):
    user = db.query(Admin).filter(Admin.username == form_data.username).first()
    if not user or not security.verify_password(form_data.password, user.password_hash):
        return Response404(msg="用户名或密码错误")
    token = Token(access_token=create_access_token(user.id))
    return Response200(data={"token": token})
