#!/usr/bin/env/ python3
# -*- coding:utf-8 -*-
"""
@Project: serve-blog
@File  :models.py
@Author:zy7y
@Date  :2021/6/10 18:55
@Desc  : 模型类
"""
from typing import List

from tortoise import fields, Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


# 抽象模型类
class AbstractModel(Model):
    id = fields.IntField(pk=True, index=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractModel):
    username = fields.CharField(max_length=255, unique=True, description="用户名")
    password = fields.CharField(max_length=255, description="用户密码")


class Post(AbstractModel):
    title = fields.CharField(max_length=200, null=False, description="文章标题")
    content = fields.TextField(description="文章内容")
    status = fields.BooleanField(default=True, description="是否显示")
    reading = fields.IntField(default=0, description="阅读量", allow_none=True)
    category = fields.ForeignKeyField(
        'models.Category',
        related_name='posts',
        description="所属分类")


class Category(AbstractModel):
    name = fields.CharField(max_length=100, null=False, description="分类名称")


class Comment(AbstractModel):
    user = fields.CharField(max_length=60, null=False, description="昵称")
    email = fields.CharField(max_length=120, description="邮箱", null=True)
    parent = fields.ForeignKeyField(
        'models.Comment',
        null=True,
        allow_none=True,
        default=None,
        description="父级评论")
    post = fields.OneToOneField(
        'models.Post',
        related_name='comments',
        description="文章")
    content = fields.TextField(description="评论内容", null=False)


class Link(AbstractModel):
    name = fields.CharField(max_length=30, null=False, description="名称")
    path = fields.CharField(max_length=255, null=False, description="链接")
    desc = fields.TextField(verbose_name="描述")


# 解决pydantic_model_creator 生成的模型中 缺少外键关联字段
Tortoise.init_models(["db.models"], "models")

# 返回模型
User_Pydantic = pydantic_model_creator(User, name="User", exclude=["password"])

# 输入模型 exclude_readonly 只读字段 非必填
UserIn_Pydantic = pydantic_model_creator(
    User, name="UserIn", exclude_readonly=True)

Post_Pydantic = pydantic_model_creator(Post, name="Post")
PostIn_Pydantic = pydantic_model_creator(
    Post, name="PostIn", exclude_readonly=True, exclude=['reading'])

Category_Pydantic = pydantic_model_creator(Category, name="Category")
CategoryIn_Pydantic = pydantic_model_creator(
    Category, name="CategoryIn", exclude_readonly=True)

Comment_Pydantic = pydantic_model_creator(Comment, name="Comment")
CommentIn_Pydantic = pydantic_model_creator(
    Comment, name="CommentIn", exclude_readonly=True)

Link_Pydantic = pydantic_model_creator(Link, name="Link")
LinkIn_Pydantic = pydantic_model_creator(
    Link, name="LinkIn", exclude_readonly=True)
