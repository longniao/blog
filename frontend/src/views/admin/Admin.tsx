import {defineComponent} from "vue";
import {RouterView} from "vue-router";
import { Button, Layout, Menu} from "ant-design-vue";
import adminStyle from "./admin.module.css"
import {UserOutlined,UploadOutlined, AppstoreOutlined, RocketOutlined } from "@ant-design/icons-vue";
import localCache from '@/tools'

import { useRouter } from "vue-router";

export default defineComponent({
    name: "App",
    setup(){

        const router = useRouter();

        const menuItemClick = (item: any) => {
            console.log("menuItemClick", item);
            router.push({name: item.key});
        }
        return () =>  (
            <Layout style={{height:"100%", width: "100%"}}>
            <Layout.Sider
              breakpoint="lg"
              collapsedWidth="0"
              onBreakpoint={broken => {
                console.log(broken);
              }}
              onCollapse={(collapsed, type) => {
                console.log(collapsed, type);
              }}
            >
              <div class={adminStyle.logo}>
                  博客后台
                </div>
              <Menu theme="dark" mode="inline" onClick={(item) => {menuItemClick(item)}}>
                <Menu.SubMenu title={"文章管理"} icon={<RocketOutlined />}>
                <Menu.Item key="AddArticle">
                  新增文章
                </Menu.Item>
                <Menu.Item key="Article">
                  文章列表
                </Menu.Item>
                </Menu.SubMenu>
               
                <Menu.Item key="Category" icon={<AppstoreOutlined />}>
                  分类管理
                </Menu.Item>
                <Menu.Item key="Project" icon={<UploadOutlined />}>
                  项目管理
                </Menu.Item>
                <Menu.Item key="Visit" icon={<UserOutlined />}>
                  访问日志
                </Menu.Item>
              </Menu>
            </Layout.Sider>
            <Layout>
              <Layout.Header class={adminStyle['site-layout-sub-header-background']} style={{ padding: 0 }} >
              <span>还没实现的面包屑</span>
              <Button onClick={()=>{
                localCache.removeCache("token")
                router.push('Login')
              }}>退出</Button>
            </Layout.Header>
              <Layout.Content style={{ margin: '24px 16px 0' }}>
                <div class={adminStyle['site-layout-background']} style={{ padding: 24, minHeight: 360 }}>
                  <RouterView />
                </div>
              </Layout.Content>
              <Layout.Footer style={{ textAlign: 'center' }}>Ant Design ©2018 Created by Ant UED</Layout.Footer>
            </Layout>
          </Layout>
        )
    }
})