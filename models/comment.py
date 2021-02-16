#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: comment.py
@author: zy7y
@time: 2021/1/31
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
评论模型
"""
from sqlalchemy.orm import relationship

from models import Base, Column, Integer, Text, String, ForeignKey


class Comment(Base):
    id = Column(Integer, index=True, primary_key=True)
    author = Column(String(30), comment="昵称")
    content = Column(Text, comment="评论内容")

    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post', back_populates='comments')

    replied_id = Column(Integer, ForeignKey('comment.id'))
    replied = relationship('Comment', back_populates='replies', remote_side=[id])
    replies = relationship('Comment', back_populates='replied', cascade='all, delete-orphan')
