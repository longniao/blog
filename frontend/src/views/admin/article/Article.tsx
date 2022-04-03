import { defineComponent, ref } from "vue";
import { useRouter } from "vue-router";
import { Service } from "@/client";
import { Table, Space, message } from "ant-design-vue";
import type { Article } from "@/client";

interface Pagination {
  current: number; // 当前页数
  pageSize: number; // 每页条数
  total: number;  // 总条数
}


export default defineComponent({
  name: "Atricle",
  setup() {
    const columns = [
      {
        title: "文章标题",
        dataIndex: "title",
        key: "title",
      },
      {
        title: "访问量",
        dataIndex: "visit",
        key: "visit",
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
    ];

    const router = useRouter();
    const data = ref<Article[]>();
    const loadData = () => {
      Service.methodArticleGet()
        .then((res) => {
          data.value = res.data;
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    };
    loadData();

    const deleteArticle = (id: number) => {
      Service.methodArticlePkDelete(id)
        .then((res) => {
          message.success("删除成功");
          loadData();
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const slots = {
      bodyCell: (data: any) => {
        if (data.column.key === "action") {
          return (
            <Space>
              <a
                onClick={() => {
                  router.push({
                    name: "EditArticle",
                    params: { ...data.record },
                  });
                }}
              >
                编辑
              </a>
              <a onClick={() => deleteArticle(data.record.id)}>删除</a>
            </Space>
          );
        }
      },
    };
    return () => (
      <div>
        <Table columns={columns} dataSource={data.value} v-slots={slots} />
      </div>
    );
  },
});
