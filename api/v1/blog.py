#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog
@file: blog.py
@author: zy7y
@time: 2021/1/31
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
博客前端，游客可见
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import db as models
from core import deps
from schemas import Response200, Response404
from schemas.review import ReviewCreate, ReviewReply

blog_router = APIRouter(tags=["前台"])


# 文章相关API
@blog_router.get("/post", name="分页文章列表")
async def get_posts(limit: int = 10, page: int = 1, db: Session = Depends(deps.get_db)):
    posts = db.query(models.Post).order_by(models.Post.create_at.desc()).offset((page - 1) * 2).limit(limit).all()
    return Response200(data={"post": posts})


@blog_router.get("/post/{post_id}", name="文章详情")
async def get_post(post_id: int, db: Session = Depends(deps.get_db)):
    # 连接查询返回分类名称
    post_obj = db.query(models.Post).get(post_id)
    if post_obj is None:
        return Response404
    post_obj.reading += 1
    db.commit()
    # # 三表查询
    # post = db.query(models.Post, models.Category, models.Comment).join(models.Category, models.Post.category_id==models.Category.id).join(
    #     models.Comment, models.Post.id == models.Comment.post_id
    # ).filter(models.Post.id==post_id).first()
    # return Response200(data={"post": post})
    category = db.query(models.Category).filter_by(id=post_obj.category_id).first()
    comment = db.query(models.Comment).filter_by(post_id=post_id).all()
    return Response200(data={"post": post_obj, "category": category, "comment": comment})


# 分类相关API
@blog_router.get("/category", name="分类列表")
async def get_sorts(limit: int = 10, page: int = 1, db: Session = Depends(deps.get_db)):
    category = db.query(models.Category).order_by(models.Category.create_at.desc()).offset((page - 1) * 2).limit(
        limit).all()
    return Response200(data={"category": category})


@blog_router.get("/category/{category_id}/post", name="分类文章列表")
async def get_sort_posts(category_id: int, limit: int = 10, page: int = 1, db: Session = Depends(deps.get_db)):
    category = db.query(models.Category).get(category_id)
    if category is not None:
        posts = db.query(models.Post). \
            filter(models.Post.category_id == category_id).order_by(models.Post.create_at.desc()).offset(
            (page - 1) * 2).limit(limit).all()
        return Response200(data={"category": category, "posts": posts})
    return Response404


# 评论相关API
@blog_router.get("/comment", name="评论列表")
async def get_reviews(post_id: int, limit: int = 10, page: int = 1, db: Session = Depends(deps.get_db)):
    data = db.query(models.Comment).filter_by(post_id=post_id).order_by(models.Comment.create_at.desc()).offset(
        (page - 1) * 2).limit(limit).all()
    return Response200(data={"comment": data})


@blog_router.post("/comment", name="发表评论")
async def create_review(review: ReviewCreate, db: Session = Depends(deps.get_db)):
    if db.query(models.Post).get(review.post_id):
        review_obj = models.Comment(**review.dict())
        db.add(review_obj)
        db.commit()
        db.refresh(review_obj)
        return Response200(data={"review": review_obj})
    return Response404(msg="评论失败，文章不存在")


@blog_router.post("/comment/{comment_id}", name="回复评论")
async def create_review(comment_id: int, review: ReviewReply, db: Session = Depends(deps.get_db)):
    if db.query(models.Post).get(review.post_id):
        review_obj = models.Comment(**review.dict())
        review_obj.replied_id = comment_id
        db.add(review_obj)
        db.commit()
        db.refresh(review_obj)
        return Response200(data={"review": review_obj})
    return Response404(msg="评论失败，文章不存在")


@blog_router.get("/link", name="友链列表")
async def get_link(db: Session = Depends(deps.get_db)):
    data = db.query(models.Link).all()
    return Response200(data={"link": data})
