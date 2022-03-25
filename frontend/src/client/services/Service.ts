/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ArticleIn } from '../models/ArticleIn';
import type { CategoryIn } from '../models/CategoryIn';
import type { CommentIn } from '../models/CommentIn';
import type { LoginForm } from '../models/LoginForm';
import type { ProjectIn } from '../models/ProjectIn';
import type { Response } from '../models/Response';
import type { Response_Article_ } from '../models/Response_Article_';
import type { Response_Category_ } from '../models/Response_Category_';
import type { Response_Comment_ } from '../models/Response_Comment_';
import type { Response_List_abc_Article__ } from '../models/Response_List_abc_Article__';
import type { Response_List_abc_Category__ } from '../models/Response_List_abc_Category__';
import type { Response_List_abc_Comment__ } from '../models/Response_List_abc_Comment__';
import type { Response_List_abc_Project__ } from '../models/Response_List_abc_Project__';
import type { Response_List_abc_VisitLog__ } from '../models/Response_List_abc_VisitLog__';
import type { Response_Project_ } from '../models/Response_Project_';
import type { Response_Token_ } from '../models/Response_Token_';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class Service {

    /**
     * 登录
     * 登录视图
     * @param requestBody 
     * @returns Response_Token_ Successful Response
     * @throws ApiError
     */
    public static loginViewLoginPost(
requestBody: LoginForm,
): CancelablePromise<Response_Token_> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/login',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 文章列表
     * 返回所有文章
     * @param limit 
     * @param page 
     * @returns Response_List_abc_Article__ Successful Response
     * @throws ApiError
     */
    public static methodArticleGet(
limit: number = 10,
page: number = 1,
): CancelablePromise<Response_List_abc_Article__> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/article',
            query: {
                'limit': limit,
                'page': page,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 文章列表
     * 返回所有文章
     * @param limit 
     * @param page 
     * @returns Response_List_abc_Article__ Successful Response
     * @throws ApiError
     */
    public static methodArticleGet1(
limit: number = 10,
page: number = 1,
): CancelablePromise<Response_List_abc_Article__> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/article',
            query: {
                'limit': limit,
                'page': page,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 创建文章
     * 添加文章
     * @param requestBody 
     * @returns Response_Article_ Successful Response
     * @throws ApiError
     */
    public static methodArticlePost(
requestBody: ArticleIn,
): CancelablePromise<Response_Article_> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/article',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 文章详情
     * 返回文章详情
     * @param pk 
     * @returns Response_Article_ Successful Response
     * @throws ApiError
     */
    public static methodArticlePkGet(
pk: number,
): CancelablePromise<Response_Article_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/article/{pk}',
            path: {
                'pk': pk,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 文章详情
     * 返回文章详情
     * @param pk 
     * @returns Response_Article_ Successful Response
     * @throws ApiError
     */
    public static methodArticlePkGet1(
pk: number,
): CancelablePromise<Response_Article_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/article/{pk}',
            path: {
                'pk': pk,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 编辑文章
     * 更新文章
     * @param pk 
     * @param requestBody 
     * @returns Response_Article_ Successful Response
     * @throws ApiError
     */
    public static methodArticlePkPut(
pk: number,
requestBody: ArticleIn,
): CancelablePromise<Response_Article_> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/article/{pk}',
            path: {
                'pk': pk,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 删除文章
     * 删除文章
     * @param pk 
     * @returns Response Successful Response
     * @throws ApiError
     */
    public static methodArticlePkDelete(
pk: number,
): CancelablePromise<Response> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/article/{pk}',
            path: {
                'pk': pk,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 分类列表
     * 返回所有
     * @param limit 
     * @param page 
     * @returns Response_List_abc_Category__ Successful Response
     * @throws ApiError
     */
    public static methodCategoryGet(
limit: number = 10,
page: number = 1,
): CancelablePromise<Response_List_abc_Category__> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/category',
            query: {
                'limit': limit,
                'page': page,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 分类列表
     * 返回所有
     * @param limit 
     * @param page 
     * @returns Response_List_abc_Category__ Successful Response
     * @throws ApiError
     */
    public static methodCategoryGet1(
limit: number = 10,
page: number = 1,
): CancelablePromise<Response_List_abc_Category__> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/category',
            query: {
                'limit': limit,
                'page': page,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 新增分类
     * 更新文章
     * @param pk 
     * @param requestBody 
     * @returns Response_Category_ Successful Response
     * @throws ApiError
     */
    public static methodCategoryPost(
pk: number,
requestBody: CategoryIn,
): CancelablePromise<Response_Category_> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/category',
            query: {
                'pk': pk,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 编辑分类
     * 更新文章
     * @param pk 
     * @param requestBody 
     * @returns Response_Category_ Successful Response
     * @throws ApiError
     */
    public static methodCategoryPkPut(
pk: number,
requestBody: CategoryIn,
): CancelablePromise<Response_Category_> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/category/{pk}',
            path: {
                'pk': pk,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 删除分类
     * 更新文章
     * @param pk 
     * @param requestBody 
     * @returns Response Successful Response
     * @throws ApiError
     */
    public static methodCategoryPkDelete(
pk: number,
requestBody: CategoryIn,
): CancelablePromise<Response> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/category/{pk}',
            path: {
                'pk': pk,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 项目列表
     * 返回所有
     * @param limit 
     * @param page 
     * @returns Response_List_abc_Project__ Successful Response
     * @throws ApiError
     */
    public static methodProjectGet(
limit: number = 10,
page: number = 1,
): CancelablePromise<Response_List_abc_Project__> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/project',
            query: {
                'limit': limit,
                'page': page,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 项目列表
     * 返回所有
     * @param limit 
     * @param page 
     * @returns Response_List_abc_Project__ Successful Response
     * @throws ApiError
     */
    public static methodProjectGet1(
limit: number = 10,
page: number = 1,
): CancelablePromise<Response_List_abc_Project__> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/project',
            query: {
                'limit': limit,
                'page': page,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 创建项目
     * 添加
     * @param requestBody 
     * @returns Response_Project_ Successful Response
     * @throws ApiError
     */
    public static methodProjectPost(
requestBody: ProjectIn,
): CancelablePromise<Response_Project_> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/project',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 项目详情
     * 返回详情
     * @param pk 
     * @returns Response_Project_ Successful Response
     * @throws ApiError
     */
    public static methodProjectPkGet(
pk: number,
): CancelablePromise<Response_Project_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/project/{pk}',
            path: {
                'pk': pk,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 项目详情
     * 返回详情
     * @param pk 
     * @returns Response_Project_ Successful Response
     * @throws ApiError
     */
    public static methodProjectPkGet1(
pk: number,
): CancelablePromise<Response_Project_> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/project/{pk}',
            path: {
                'pk': pk,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 编辑项目
     * 更新
     * @param pk 
     * @param requestBody 
     * @returns Response_Project_ Successful Response
     * @throws ApiError
     */
    public static methodProjectPkPut(
pk: number,
requestBody: ProjectIn,
): CancelablePromise<Response_Project_> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/project/{pk}',
            path: {
                'pk': pk,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 删除项目
     * 删除
     * @param pk 
     * @returns Response Successful Response
     * @throws ApiError
     */
    public static methodProjectPkDelete(
pk: number,
): CancelablePromise<Response> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/project/{pk}',
            path: {
                'pk': pk,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 评论列表
     * 返回所有
     * @param limit 
     * @param page 
     * @returns Response_List_abc_Comment__ Successful Response
     * @throws ApiError
     */
    public static methodCommentGet(
limit: number = 10,
page: number = 1,
): CancelablePromise<Response_List_abc_Comment__> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/comment',
            query: {
                'limit': limit,
                'page': page,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 评论列表
     * 返回所有
     * @param limit 
     * @param page 
     * @returns Response_List_abc_Comment__ Successful Response
     * @throws ApiError
     */
    public static methodCommentGet1(
limit: number = 10,
page: number = 1,
): CancelablePromise<Response_List_abc_Comment__> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/comment',
            query: {
                'limit': limit,
                'page': page,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 评论创建
     * 添加
     * @param requestBody 
     * @returns Response_Comment_ Successful Response
     * @throws ApiError
     */
    public static methodCommentPost(
requestBody: CommentIn,
): CancelablePromise<Response_Comment_> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/comment',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 删除评论
     * 删除
     * @param pk 
     * @returns Response Successful Response
     * @throws ApiError
     */
    public static methodCommentPkDelete(
pk: number,
): CancelablePromise<Response> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/comment/{pk}',
            path: {
                'pk': pk,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * 访问列表
     * 返回所有
     * @param limit 
     * @param page 
     * @returns Response_List_abc_VisitLog__ Successful Response
     * @throws ApiError
     */
    public static methodVisitGet(
limit: number = 10,
page: number = 1,
): CancelablePromise<Response_List_abc_VisitLog__> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/visit',
            query: {
                'limit': limit,
                'page': page,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}