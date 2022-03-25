import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/admin',
      name: 'Login',
      component: () => import("@/views/login/Login")
    },

  ]
})

export default router
