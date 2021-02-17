#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog
@file: admin.py
@author: zy7y
@time: 2021/1/31
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
admin schemas模型， 用于 请求和响应
"""
from datetime import datetime

from pydantic import BaseModel


class Admin(BaseModel):
    username: str
    blog_title: str
    blog_sub_title: str
    name: str
    about: str


class AdminUpdate(Admin):
    password: str


# 与数据库对应的响应模型
class AdminBase(Admin):
    id: int
    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True
