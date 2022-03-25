import { createRouter, createWebHistory } from 'vue-router'
import localCache from '@/tools'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: () => import("@/views/login/Login")
    },
    {
      path: '/main',
      name: 'Home',
      component: () => import("@/views/admin/Admin")
    }

  ]
})

// 导航守卫, 没登录跳转登录页
router.beforeEach((to) => {
  if (to.path !== '/login') {
    const token = localCache.getCache('token')
    if (!token) {
      return '/login'
    }
  }
})


export default router
