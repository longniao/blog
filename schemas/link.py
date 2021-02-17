#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog
@file: link.py
@author: zy7y
@time: 2021/2/17
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:

"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# 创建/修改的基类, 回复的评论
class Link(BaseModel):
    name: str
    url: str


class LinkCreate(Link):
    pass


# 数据库查询出来的模型类
class LinkBase(Link):
    """数据库user表基础模型，并且与model中的user相关联"""
    id: Optional[int] = None

    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True
