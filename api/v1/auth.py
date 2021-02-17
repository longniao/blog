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
from sqlalchemy.orm import Session

from db import Admin
from core import deps, security
from core.security import create_access_token
from schemas import Token, Response200, Response404, Auth

auth_router = APIRouter(tags=["登录"])


@auth_router.post("/auth", name="管理员登录", response_model=Union[Response200, Response404])
async def admin_login(
        auth: Auth,
        db: Session = Depends(deps.get_db)
):
    user = db.query(Admin).filter(Admin.username == auth.username).first()
    if not user or not security.verify_password(auth.password, user.password_hash):
        return Response404(msg="用户名或密码错误")
    token = Token(token=f"Bearer {create_access_token(user.id)}")
    return Response200(data=token)
