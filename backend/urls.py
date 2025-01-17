from typing import List

from fastapi.routing import APIRoute

from views import *

routes = [
    APIRoute(
        "/login",
        endpoint=login_view,
        methods=["POST"],
        summary="登录",
        tags=["管理员"],
        response_model=Response[Token],
    ),
    # 文章
    APIRoute(
        "/article",
        endpoint=ArticleViews.all,
        methods=["GET"],
        summary="文章列表",
        tags=["游客", "管理员"],
        response_model=Response[List[ArticleViews.OutPut]],
    ),
    APIRoute(
        "/article/{pk}",
        endpoint=ArticleViews.get,
        methods=["GET"],
        summary="文章详情",
        tags=["游客", "管理员"],
        response_model=Response[ArticleViews.OutPut],
    ),
    APIRoute(
        "/article",
        endpoint=ArticleViews.post,
        methods=["POST"],
        summary="创建文章",
        tags=["管理员"],
        response_model=Response[ArticleViews.OutPut],
    ),
    APIRoute(
        "/article/{pk}",
        endpoint=ArticleViews.put,
        methods=["PUT"],
        summary="编辑文章",
        tags=["管理员"],
        response_model=Response[ArticleViews.OutPut],
    ),
    APIRoute(
        "/article/{pk}",
        endpoint=ArticleViews.delete,
        methods=["DELETE"],
        summary="删除文章",
        tags=["管理员"],
        response_model=Response,
    ),
    # 分类
    APIRoute(
        "/category",
        CategoryViews.all,
        methods=["GET"],
        summary="分类列表",
        tags=["游客", "管理员"],
        response_model=Response[List[CategoryViews.OutPut]],
    ),
    APIRoute(
        "/category",
        CategoryViews.post,
        methods=["POST"],
        summary="新增分类",
        tags=["管理员"],
        response_model=Response[CategoryViews.OutPut],
    ),
    APIRoute(
        "/category/{pk}",
        CategoryViews.put,
        methods=["PUT"],
        summary="编辑分类",
        tags=["管理员"],
        response_model=Response[CategoryViews.OutPut],
    ),
    APIRoute(
        "/category/{pk}",
        CategoryViews.put,
        methods=["DELETE"],
        summary="删除分类",
        tags=["管理员"],
        response_model=Response,
    ),
    # 项目
    APIRoute(
        "/project",
        ProjectViews.all,
        methods=["GET"],
        summary="项目列表",
        tags=["游客", "管理员"],
        response_model=Response[List[ProjectViews.OutPut]],
    ),
    APIRoute(
        "/project/{pk}",
        ProjectViews.get,
        methods=["GET"],
        summary="项目详情",
        tags=["游客", "管理员"],
        response_model=Response[ProjectViews.OutPut],
    ),
    APIRoute(
        "/project/{pk}",
        ProjectViews.put,
        methods=["PUT"],
        summary="编辑项目",
        tags=["管理员"],
        response_model=Response[ProjectViews.OutPut],
    ),
    APIRoute(
        "/project",
        ProjectViews.post,
        methods=["POST"],
        summary="创建项目",
        tags=["管理员"],
        response_model=Response[ProjectViews.OutPut],
    ),
    APIRoute(
        "/project/{pk}",
        ProjectViews.delete,
        methods=["DELETE"],
        summary="删除项目",
        tags=["管理员"],
        response_model=Response,
    ),
    # 评论
    APIRoute(
        "/comment",
        CommentViews.all,
        methods=["GET"],
        summary="评论列表",
        tags=["游客", "管理员"],
        response_model=Response[List[CommentViews.OutPut]],
    ),
    APIRoute(
        "/comment",
        CommentViews.post,
        methods=["POST"],
        summary="评论创建",
        tags=["游客"],
        response_model=Response[CommentViews.OutPut],
    ),
    APIRoute(
        "/comment/{pk}",
        CommentViews.delete,
        methods=["DELETE"],
        summary="删除评论",
        tags=["管理员"],
        response_model=Response,
    ),
    # 访问记录
    APIRoute(
        "/visit",
        VisitLogViews.all,
        methods=["GET"],
        summary="访问列表",
        tags=["管理员"],
        response_model=Response[List[VisitLogViews.OutPut]],
    ),
]
