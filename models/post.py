#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: post.py
@author: zy7y
@time: 2021/1/9
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
文章模型
"""
from sqlalchemy.orm import relationship

from models import Base, Column, Integer, Text, String, ForeignKey


class Post(Base):
    id = Column(Integer, index=True, primary_key=True)
    title = Column(String(100), comment="文章标题")
    body = Column(Text, comment="文章内容")
    # 文章状态
    status = Column(Integer, default=1, comment="文章状态,1 置顶显示 2正常显示 3 不显示")
    reading = Column(Integer, default=0, comment="阅读量")
    category_id = Column(Integer, ForeignKey('category.id'))
    # category = relationship('Category', back_populates='post')
    category = relationship('Category', back_populates='posts')
    # 级联操作
    comments = relationship('Comment', back_populates='post', cascade='all')
