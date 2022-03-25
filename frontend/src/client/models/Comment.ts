/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type Comment = {
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
     * 评论内容
     */
    content: string;
};