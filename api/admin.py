#!/usr/bin/env/ python3
# -*- coding:utf-8 -*-
"""
@Project: serve-blog
@File  :admin.py
@Author:zy7y
@Date  :2021/6/10 19:49
@Desc  :
"""
from fastapi import APIRouter, Depends

from core.schemas import Success, Fail
from core.security import get_current_user
from db import models

admin = APIRouter(tags=["管理员"], dependencies=[Depends(get_current_user)])
# admin = APIRouter(tags=["管理员"])


@admin.post("/posts", name="新增文章")
async def create_post(post: models.PostIn_Pydantic):
    post_obj = await models.Post.create(**post.dict(exclude_unset=True))
    return Success(data=await models.Post_Pydantic.from_tortoise_orm(post_obj))


@admin.delete("/posts/{post_id}", name="删除文章")
async def delete_post(post_id: int):
    if await models.Post.filter(id=post_id).delete():
        return Success()
    return Fail(msg="文章不存在")


@admin.put("/posts/{post_id}", name="更新文章")
async def update_post(post_id: int, post: models.PostIn_Pydantic):
    await models.Post.filter(id=post_id).update(**post.dict(exclude_unset=True))
    return Success(data=await models.Post_Pydantic.from_queryset_single(models.Post.get(id=post_id)))


@admin.post("/categorys", name="新增分类")
async def create_post(category: models.CategoryIn_Pydantic):
    category_obj = await models.Category.create(**category.dict(exclude_unset=True))
    return Success(data=await models.Category_Pydantic.from_tortoise_orm(category_obj))


@admin.delete("/categorys/{category_id}", name="删除分类")
async def delete_post(category_id: int):
    if await models.Category.filter(id=category_id).delete():
        return Success()
    return Fail(msg="分类不存在")


@admin.put("/categorys/{category_id}", name="更新分类")
async def update_post(category_id: int, category: models.CategoryIn_Pydantic):
    await models.Category.filter(id=category_id).update(**category.dict(exclude_unset=True))
    return Success(data=await models.Category_Pydantic.from_queryset_single(models.Category.get(id=category_id)))


@admin.delete("/comments/{comment_id}", name="删除评论")
async def delete_comment(comment_id: int):
    if await models.Comment.filter(id=comment_id).delete():
        return Success()
    return Fail(msg="分类不存在")


@admin.post("/links", name="新增友链")
async def create_link(link: models.LinkIn_Pydantic):
    link_obj = await models.Link.create(**link.dict(exclude_unset=True))
    return Success(data=await models.Link_Pydantic.from_tortoise_orm(link_obj))


@admin.put("/links/{link_id}", name="更新友链")
async def update_link(link_id: int, link: models.LinkIn_Pydantic):
    await models.Link.filter(id=link_id).update(**link.dict(exclude_unset=True))
    return Success(data=await models.Link_Pydantic.from_queryset_single(models.Link.get(id=link_id)))


@admin.delete("/links/{link_id}", name="删除友链")
async def update_link(link_id: int):
    if await models.Link.filter(id=link_id).delete():
        return Success()
    return Fail(msg="分类不存在")

blog = APIRouter(tags=["游客"])


@blog.get("/posts", name="获取文章列表")
async def select_all_post(limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    items = await models.Post_Pydantic.from_queryset(models.Post.all().offset(skip).limit(limit))
    total = await models.Post.all().count()
    return Success(data={"total": total, "items": items})


@blog.get("/posts/{post_id}", name="获取文章详情")
async def select_post(post_id: int):
    return Success(data=await models.Post_Pydantic.from_queryset_single(models.Post.get(id=post_id)))


@blog.get("/categorys", name="获取分类列表")
async def select_all_category(limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    items = await models.Category_Pydantic.from_queryset(models.Category.all().offset(skip).limit(limit))
    total = await models.Category.all().count()
    return Success(data={"total": total, "items": items})


@blog.get("/categorys/{category_id}", name="获取分类详情")
async def select_post(post_id: int):
    return Success(data=await models.Category_Pydantic.from_queryset_single(models.Category.get(id=post_id)))


@blog.get("/comments", summary="获取评论列表")
async def select_all_comment(limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    items = await models.Comment_Pydantic.from_queryset(models.Comment.all().offset(skip).limit(limit))
    total = await models.Comment.all().count()
    return Success(data={"total": total, "items": items})


@blog.post("/comments", name="新增评论")
async def create_comment(comment: models.CommentIn_Pydantic):
    comment_obj = await models.Comment.create(**comment.dict(exclude_unset=True))
    return Success(data=await models.Post_Pydantic.from_tortoise_orm(comment_obj))


@blog.get("/links", name="友链列表")
async def select_all_link(limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    items = await models.Link_Pydantic.from_queryset(models.Link.all().offset(skip).limit(limit))
    total = await models.Link.all().count()
    return Success(data={"total": total, "items": items})


@blog.get("/links/{link_id}", name="友链详细")
async def select_link(link_id: int):
    return Success(data=await models.Link_Pydantic.from_queryset_single(models.Link.get(id=link_id)))
