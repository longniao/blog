class LocalCache {
    /**
     * @description 存数据到localStorage中
     * @param key 类型 字符串
     * @param value 类型 任意 通过json.stringify 转成对象
     */
    setCache(key: string, value: any) {
      window.localStorage.setItem(key, JSON.stringify(value))
    }
  
    /**
     * @description 取数据
     * @param key 类型 字符串
     */
    getCache(key: string) {
      const value = window.localStorage.getItem(key)
      if (value) {
        return JSON.parse(value)
      }
    }
  
    /**
     * @description 删除缓存数据
     * @param key 类型 字符串
     */
    removeCache(key: string) {
      window.localStorage.removeItem(key)
    }
  }
  
  export default new LocalCache()