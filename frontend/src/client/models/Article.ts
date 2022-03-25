/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type Article = {
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
     * 标题
     */
    title: string;
    /**
     * 文章内容
     */
    content: string;
    /**
     * 访问量
     */
    visit?: number;
};