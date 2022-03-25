/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type Category = {
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
     * 分类名称
     */
    name: string;
};