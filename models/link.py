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
友链表
"""
from models import Base, Column, Integer, String


class Link(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    url = Column(String(255))
