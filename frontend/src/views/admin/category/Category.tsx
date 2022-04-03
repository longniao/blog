import { defineComponent } from "vue";
import {Table, Button} from "ant-design-vue";
export default defineComponent({
    name: "Category",
    setup() {
        const columns = [
            {
                title: "Name",
                dataIndex: "name",
                key: "name",
            },
            {
                title: "创建时间",
                dataIndex: "created",
                key: "created",
              },
              {
                title: "更新时间",
                dataIndex: "modified",
                key: "created",
              },
              {
                title: "操作",
                dataIndex: "action",
                key: "action",
              },
        ]
        const dataSource = [
            {
                key: "1",
                name: "John Brown",
            },
        ]
        return () => (
            <div>
                <Button style={{marginBottom: "8px"}}>新增分类</Button>
                <Table bordered data-source={dataSource} columns={columns}/>
            </div>
        );
    }
})