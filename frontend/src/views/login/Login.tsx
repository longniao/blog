import { defineComponent } from "vue";
import loginStyle from "./login.module.css";

import { Card, Form, Input, Button } from "ant-design-vue";

export default defineComponent({
  name: "Login",
  props: {},
  setup() {


    return () => (
        <Card class={loginStyle.login}>
            <div class={loginStyle.title}>后台管理系统</div>
        <Form name="basic">
        <Form.Item
          label="Username"
          name="username"
          rules={[{ required: true, message: "Please input your username!" }]}
        >
          <Input />
        </Form.Item>

        <Form.Item
          label="Password"
          name="password"
          rules={[{ required: true, message: "Please input your password!" }]}
        >
          <Input.Password />
        </Form.Item>

        <Form.Item>
          <Button type="primary" htmlType="submit">
            Submit
          </Button>
        </Form.Item>
      </Form>
        </Card>
    );
  },
});
