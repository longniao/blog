#!/usr/bin/env/ python3
# -*- coding:utf-8 -*-
"""
@Project: blog
@File  :test_admin.py
@Author:zy7y
@Date  :2021/6/10 22:43
@Desc  : 测试管理员相关api
"""
import asyncio

from fastapi.testclient import TestClient
from jsonpath import jsonpath

from db import models


class TestAdmin:

    def test_login(self, client: TestClient, event_loop: asyncio.AbstractEventLoop):
        response = client.post("/login", json={
  "username": "tester",
  "password": "123456"
})
        assert response.status_code == 200, response.text
        # data = response.json()
        # assert data == "tester"

        async def get_user_by_db():
            user = await models.User.get(username="tester")
            return user

        assert event_loop.run_until_complete(get_user_by_db())