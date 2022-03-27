import { OpenAPI, type LoginForm } from '@/client'
import { Service } from '@/client'
import { defineStore } from 'pinia'
import localCache from '@/tools'
import router from '@/router'

import {message} from "ant-design-vue"

export const useStore = defineStore({
  id: 'login',
  state: () => ({
    counter: 0,
    token: '',
  }),
  getters: {
    doubleCount: (state) => state.counter * 2
  },
  actions: {
    increment() {
      this.counter++
    },
    async loginAsync(payload: LoginForm) {
      const loginResult = await Service.loginViewLoginPost(payload)

      // ?? - 左侧为null 或者 undefined时  返回 右侧内容 '' ~ 空值合并符
      // ?. 在null 和 undefined时  返回undefined ~ 可用链操作符
      if (loginResult.code === 200) {
          this.token = loginResult.data?.access_token ?? ''
          localCache.setCache('token', this.token)
          message.success('登录成功')
          OpenAPI.TOKEN = this.token
          router.push('/admin/article/list')
      }
      else{
          message.error(loginResult?.msg ?? '登录失败')
      }
    },
    loadLocalCache() {
      this.token = localCache.getCache('token')
      OpenAPI.TOKEN = this.token
    }
  }
})
