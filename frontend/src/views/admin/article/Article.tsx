import { defineComponent, ref } from "vue";
import { Service } from "@/client";
import { Table, Space } from "ant-design-vue";
import type { Article } from "@/client";

export default defineComponent({
    name: "Atricle",
    setup() {
        const columns = [
            {
              title: '文章标题',
              dataIndex: 'title',
              key: 'title'
            },
            {
              title: '访问量',
              dataIndex: 'visit',
              key: 'visit'
            },
            {
              title: '创建时间',
              dataIndex: 'created',
              key: 'created'
            },
            {
              title: '更新时间',
              dataIndex: 'modified',
              key: 'created'
            }
          ];
        
        const data = ref<Article[]>()
        Service.methodArticleGet()
            .then(res => {
            data.value = res.data
            console.log(res);
        })
            .catch(err => {
            console.log(err);
        });
        return () => (
            <div>
                <Table columns={columns} dataSource={data.value} />
            </div>
        );
    }
})