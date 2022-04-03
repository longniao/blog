import { defineComponent, reactive, ref } from "vue";
import loginStyle from "./login.module.css";

import { Card, Form, Input, Button } from "ant-design-vue";
import type { LoginForm } from "@/client";
import { useStore} from "@/stores/login"


export default defineComponent({
  name: "Login",
  props: {},
  setup() {

    const store = useStore()

    const loginForm = reactive<LoginForm>({
      username: "admin",
      password: "123456",
    });

    // Form组件对象
    const antdFormRef = ref<InstanceType<typeof Form>>()

    const onSubmit = () => {
        // @ts-ignore
        antdFormRef.value?.validateFields().catch((err) => {
            if (err.errorFields.length === 0) {
                store.loginAsync(loginForm)
            }
            return
        })
    };
    return () => (
      <div class={loginStyle.login}>
        <Card class={loginStyle["login-card"]}>
          <div class={loginStyle.title}>后台管理系统</div>
          <Form name="basic" ref={antdFormRef} model={loginForm} onSubmit={onSubmit}>
            <Form.Item
              label="账号"
              name="username"
              rules={[{ required: true, message: "请输入账号", min: 5 }]}
            >
              <Input
                v-model:value={loginForm.username}
                placeholder="请输入用户名"
              />
            </Form.Item>

            <Form.Item
              label="密码"
              name="password"
              rules={[{ required: true, message: "请输入密码", min: 5 }]}
            >
              <Input.Password
                v-model:value={loginForm.password}
                placeholder="请输入密码"
              />
            </Form.Item>

            <Form.Item>
              <Button type="primary" htmlType="submit">
                Submit
              </Button>
            </Form.Item>
          </Form>
        </Card>
      </div>
    );
  },
});
