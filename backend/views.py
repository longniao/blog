from abc import ABC, abstractmethod

from fastapi import Depends
from tortoise.contrib.pydantic import pydantic_model_creator

from config import setting
from deps import check_token, create_access_token, verify_password
from models import Article, Category, Comment, Project, VisitLog
from schemas import LoginForm, Response, Token


class RESTFulViews(ABC):
    @classmethod
    @abstractmethod
    async def all(cls, limit: int = 10, page: int = 1):
        """分页查所有"""

    @classmethod
    @abstractmethod
    async def get(cls, pk: int):
        """查详情"""

    @classmethod
    @abstractmethod
    async def post(cls, *args, **kwargs):
        """新增"""

    @classmethod
    @abstractmethod
    async def put(cls, *args, **kwargs):
        """修改"""

    @classmethod
    @abstractmethod
    async def delete(cls, pk: int):
        """删除"""


def login_view(login_form: LoginForm):
    """登录视图"""
    if login_form.username == setting.SUPER_USER:
        if verify_password(login_form.password, setting.SUPER_PASSWD):
            return Response(data=Token(access_token=create_access_token(login_form.username)))
    return Response(code=400, msg="账号或密码错误.")


class ArticleViews(RESTFulViews):
    """文章列表"""

    OutPut = pydantic_model_creator(Article, name="Article")
    Input = pydantic_model_creator(
        Article, name="ArticleIn", exclude_readonly=True, exclude=("visit",)
    )

    not_404 = Response(code=400, msg="文章不存在.")

    @classmethod
    async def all(cls, limit: int = 10, page: int = 1):
        """返回所有文章"""
        items = await cls.OutPut.from_queryset(
            Article.all().offset((page - 1) * limit).limit(limit)
        )
        total = await Article.all().count()
        return Response(total=total, data=items)

    @classmethod
    async def get(cls, pk: int):
        """返回文章详情"""
        if obj := await Article.filter(id=pk).first():
            await Article.filter(id=pk).update(visit=obj.visit + 1)
            return Response(
                data=await cls.OutPut.from_queryset_single(Article.get(id=pk))
            )
        return cls.not_404

    @classmethod
    async def delete(cls, pk: int, token: str = Depends(check_token)):
        """删除文章"""
        if await Article.filter(id=pk).delete():
            return Response(msg="删除成功.")
        return cls.not_404

    @classmethod
    async def put(cls, pk: int, article: Input, token: str = Depends(check_token)):
        """更新文章"""
        await Article.filter(id=pk).update(**article.dict(exclude_unset=True))
        return Response(data=await cls.OutPut.from_queryset_single(Article.get(id=pk)))

    @classmethod
    async def post(cls, article: Input, token: str = Depends(check_token)):
        """添加文章"""
        article_obj = await Article.create(**article.dict(exclude_unset=True))
        return Response(data=await cls.OutPut.from_tortoise_orm(article_obj))


class CategoryViews(RESTFulViews):
    """分类列表"""

    OutPut = pydantic_model_creator(Category, name="Category")
    Input = pydantic_model_creator(Category, name="CategoryIn", exclude_readonly=True)

    not_404 = Response(code=400, msg="标签不存在.")

    @classmethod
    async def all(cls, limit: int = 10, page: int = 1):
        """返回所有"""
        items = await cls.OutPut.from_queryset(
            Category.all().offset((page - 1) * limit).limit(limit)
        )
        total = await Category.all().count()
        return Response(total=total, data=items)

    @classmethod
    async def get(cls, pk: int):
        """返回详情"""

    @classmethod
    async def delete(cls, pk: int, token: str = Depends(check_token)):
        """删除"""
        if await Category.filter(id=pk).delete():
            return Response(msg="删除成功.")
        return cls.not_404

    @classmethod
    async def put(cls, pk: int, category: Input, token: str = Depends(check_token)):
        """更新文章"""
        await Category.filter(id=pk).update(**category.dict(exclude_unset=True))
        return Response(data=await cls.OutPut.from_queryset_single(Category.get(id=pk)))

    @classmethod
    async def post(cls, category: Input, token: str = Depends(check_token)):
        """添加文章"""
        category_obj = await Category.create(**category.dict(exclude_unset=True))
        return Response(data=await cls.OutPut.from_tortoise_orm(category_obj))


class CommentViews(RESTFulViews):
    """分类列表"""

    OutPut = pydantic_model_creator(Comment, name="Comment")
    Input = pydantic_model_creator(Comment, name="CommentIn", exclude_readonly=True)

    not_404 = Response(code=400, msg="评论不存在.")

    @classmethod
    async def all(cls, limit: int = 10, page: int = 1):
        """返回所有"""
        items = await cls.OutPut.from_queryset(
            Comment.all().offset((page - 1) * limit).limit(limit)
        )
        total = await Comment.all().count()
        return Response(total=total, data=items)

    @classmethod
    async def get(cls, pk: int):
        """返回详情"""

    @classmethod
    async def delete(cls, pk: int, token: str = Depends(check_token)):
        """删除"""
        if await Comment.filter(id=pk).delete():
            return Response(msg="删除成功.")
        return cls.not_404

    @classmethod
    async def put(cls):
        """更新"""

    @classmethod
    async def post(cls, comment: Input):
        """添加"""
        comment_obj = await Comment.create(**comment.dict(exclude_unset=True))
        return Response(data=await cls.OutPut.from_tortoise_orm(comment_obj))


class ProjectViews(RESTFulViews):
    """分类列表"""

    OutPut = pydantic_model_creator(Project, name="Project")
    Input = pydantic_model_creator(Project, name="ProjectIn", exclude_readonly=True)

    not_404 = Response(code=400, msg="项目不存在.")

    @classmethod
    async def all(cls, limit: int = 10, page: int = 1):
        """返回所有"""
        items = await cls.OutPut.from_queryset(
            Project.all().offset((page - 1) * limit).limit(limit)
        )
        total = await Project.all().count()
        return Response(total=total, data=items)

    @classmethod
    async def get(cls, pk: int):
        """返回详情"""
        data = await cls.OutPut.from_queryset_single(Project.get(id=pk))
        return Response(data=data)

    @classmethod
    async def delete(cls, pk: int, token: str = Depends(check_token)):
        """删除"""
        if await Project.filter(id=pk).delete():
            return Response(msg="删除成功.")
        return cls.not_404

    @classmethod
    async def put(cls, pk: int, project: Input, token: str = Depends(check_token)):
        """更新"""
        await Project.filter(id=pk).update(**project.dict(exclude_unset=True))
        return Response(data=await cls.OutPut.from_queryset_single(Project.get(id=pk)))

    @classmethod
    async def post(cls, project: Input, token: str = Depends(check_token)):
        """添加"""
        project_obj = await Project.create(**project.dict(exclude_unset=True))
        return Response(data=await cls.OutPut.from_tortoise_orm(project_obj))


class VisitLogViews(RESTFulViews):
    """访问日志"""

    OutPut = pydantic_model_creator(VisitLog, name="VisitLog")

    not_404 = Response(code=400, msg="日志不存在.")

    @classmethod
    async def all(
        cls, limit: int = 10, page: int = 1, token: str = Depends(check_token)
    ):
        """返回所有"""
        items = await cls.OutPut.from_queryset(
            VisitLog.all().offset((page - 1) * limit).limit(limit)
        )
        total = await VisitLog.all().count()
        return Response(total=total, data=items)

    @classmethod
    async def delete(cls, pk: int, token: str = Depends(check_token)):
        """删除"""
        if await VisitLog.filter(id=pk).delete():
            return Response(msg="删除成功.")
        return cls.not_404

    @classmethod
    async def post(cls, *args, **kwargs):
        pass

    @classmethod
    async def get(cls, pk: int):
        pass

    @classmethod
    async def put(cls, *args, **kwargs):
        pass
