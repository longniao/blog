#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog
@file: fake_data.py
@author: zy7y
@time: 2021/2/16
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
虚拟数据生成
"""
import random

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import Admin, Category, Post, Comment, Link
from core.security import get_password_hash

engine = create_engine("sqlite:///blog.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()


class BlogFakeData:

    def __init__(self):
        self.fake = Faker("zh_CN")

    def fake_admin(self):
        """构造初始管理员数据"""
        username = self.fake.user_name()
        password = self.fake.password()
        admin_obj = Admin(
            username=username,
            password_hash=get_password_hash(password),
            blog_title=self.fake.pystr(max_chars=6),
            blog_sub_title=self.fake.pystr(max_chars=30),
            name=self.fake.name(),
            about=self.fake.sentence()
        )
        session.add(admin_obj)
        session.commit()
        session.refresh(admin_obj)
        print("管理员账号: " + username, "管理员密码: " + password)

    def fake_category(self, count: int = 10):
        """构造虚拟分类"""
        for i in range(count):
            category_obj = Category(name=self.fake.word())
            session.add(category_obj)
            try:
                session.commit()
                session.refresh(category_obj)
            except Exception as e:
                session.rollback()

    def fake_post(self, count: int = 50):
        """构造虚拟文章"""
        for i in range(count):
            post_obj = Post(
                title=self.fake.sentence(),
                body=self.fake.text(2000),
                category=session.query(Category).get(random.randint(1, session.query(Category).count()))
            )
            session.add(post_obj)
        session.commit()

    def fake_comment(self, count: int = 100):
        """构造虚拟评论"""
        for i in range(count):
            comment_obj = Comment(
                author=self.fake.name(),
                content=self.fake.sentence(),
                post=session.query(Post).get(random.randint(1, session.query(Post).count())),
            )
            session.add(comment_obj)
        session.commit()

    def fake_reply(self, count: int = 50):
        # 回复评论
        for i in range(count):
            reply_obj = Comment(
                author=self.fake.name(),
                content=self.fake.sentence(),
                post=session.query(Post).get(random.randint(1, session.query(Post).count())),
                replied=session.query(Comment).get(random.randint(1, session.query(Comment).count()))
            )
            session.add(reply_obj)
        session.commit()

    def fake_link(self):
        github = Link(name="Github", url="https://github.com/zy7y")
        gitee = Link(name="Gitee", url="https://gitee.com/zy7y")
        blog = Link(name="博客园", url="https://www.cnblogs.com/zy7y")
        testerhome = Link(name="TesterHome", url="https://testerhome.com/zy7y")
        session.add_all([github, gitee, blog, testerhome])
        session.commit()

    def init_fake_data(self):
        """初始化数据"""
        print("---------数据初始化----------")
        self.fake_admin()
        self.fake_category()
        self.fake_post()
        self.fake_comment()
        self.fake_reply()
        self.fake_link()
        session.close()
        print("---------数据初始化完成--------")


if __name__ == '__main__':
    BlogFakeData().init_fake_data()
