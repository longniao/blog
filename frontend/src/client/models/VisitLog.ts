/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type VisitLog = {
    id: number;
    /**
     * 创建时间
     */
    readonly created?: string | null;
    /**
     * 更新时间
     */
    readonly modified?: string | null;
    /**
     * 访问者IP
     */
    host: string;
    /**
     * 请求地址
     */
    url: string;
    /**
     * 请求方式
     */
    method: string;
    /**
     * 请求头
     */
    headers?: any;
    /**
     * 响应状态码
     */
    status_code: number;
};