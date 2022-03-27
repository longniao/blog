import { createRouter, createWebHistory } from "vue-router";
import localCache from "@/tools";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/login",
      name: "Login",
      component: () => import("@/views/login/Login"),
    },
    {
      path: "/admin",
      name: "Home",
      component: () => import("@/views/admin/Admin"),
      children: [
        {
          path: "article/list",
          name: "Article",
          component: () => import("@/views/admin/article/Article"),
        },
        {
          path: "article/add",
          name: "AddArticle",
          component: () => import("@/views/admin/article/Add"),
        },
        {
          path: "article/edit/:id",
          name: "EditArticle",
          component: () => import("@/views/admin/article/Edit"),
        },
        {
          path: "category",
          name: "Category",
          component: () => import("@/views/admin/category/Category"),
        },
        {
          path: "project",
          name: "Project",
          component: () => import("@/views/admin/project/Project"),
        },
        {
          path: "visit",
          name: "Visit",
          component: () => import("@/views/admin/visit/Visit"),
        },
      ],
    },
  ],
});

// 导航守卫, 没登录跳转登录页
router.beforeEach((to) => {
  if (to.path !== "/login") {
    const token = localCache.getCache("token");
    if (!token) {
      return "/login";
    }
  }
});

export default router;
