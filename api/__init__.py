#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
@project: blog(FastAPI)
@file: __init__.py
@author: zy7y
@time: 2021/1/9
@site: https://cnblogs.com/zy7y
@github: https://github.com/zy7y
@gitee: https://gitee.com/zy7y
@desc:
蓝图模式，实际api管理
"""
from fastapi import FastAPI, Request
from tortoise.contrib.fastapi import register_tortoise

from api.admin import blog, admin
from api.auth import auth
from tools.logger import logger
from fastapi.middleware.cors import CORSMiddleware

from core.config import setting


def create_app():
    app = FastAPI(title="个人博客API",
              description="""
      Blog: https://www.cnblogs.com/zy7y
      账号: tester, 密码: 123456
              """)
    app.include_router(auth)
    app.include_router(blog)
    app.include_router(admin)

    # 挂载 数据库
    register_tortoise(
        app,
        db_url="sqlite://db.sqlite3",
        modules={"models": ["db.models"]},
        # # 生成表
        generate_schemas=True,
        # 使用异常，当无数据是自动返回
        add_exception_handlers=True,
    )

    # 设置跨域
    app.add_middleware(
        CORSMiddleware,
        allow_origins=setting.ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 自定义访问日志中间件
    @app.middleware("http")
    async def logger_request(request: Request, call_next):
        # https://stackoverflow.com/questions/60098005/fastapi-starlette-get-client-real-ip
        logger.info(f"访问记录:{request.method} url:{request.url}\nheaders:{request.headers.get('user-agent')}"
                    f"\nIP:{request.client.host}")
        response = await call_next(request)
        return response

    return app
