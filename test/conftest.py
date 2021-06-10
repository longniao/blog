#!/usr/bin/env/ python3
# -*- coding:utf-8 -*-
"""
@Project: blog
@File  :conftest.py
@Author:zy7y
@Date  :2021/6/10 22:40
@Desc  :
"""
from typing import Generator
from fastapi.testclient import TestClient
import pytest as pytest
from main import app

from tortoise.contrib.test import finalizer, initializer


# 客户端对象
@pytest.fixture(scope="module")
def client() -> Generator:
    initializer(["db.models"])
    with TestClient(app) as c:
        yield c
    finalizer()


# 数据库对象
@pytest.fixture(scope="module")
def event_loop(client: TestClient) -> Generator:
    yield client.task.get_loop()