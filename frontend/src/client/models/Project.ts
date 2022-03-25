/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type Project = {
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
     * 项目名称
     */
    name: string;
    /**
     * 项目描述
     */
    desc: string;
};