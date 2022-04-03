import { defineComponent, reactive, ref, watch } from "vue";
import { Service } from "@/client";
import { Table, Space, Tag, Drawer } from "ant-design-vue";
import type { VisitLog } from "@/client";

interface Pagination {
    current: number; // 当前页数
    pageSize: number; // 每页条数
    total: number;  // 总条数
}


export default defineComponent({
  name: "Visit",
  setup() {
    const columns = [
      {
        title: "HOST",
        dataIndex: "host",
        key: "host",
      },
      {
        title: "URL",
        dataIndex: "url",
        key: "url",
      },
      {
        title: "METHOD",
        dataIndex: "method",
        key: "method",
      },
      {
        title: "状态码",
        dataIndex: "status_code",
        key: "status_code",
      },
      {
        title: "创建时间",
        dataIndex: "created",
        key: "created",
      },
      {
        title: "操作",
        dataIndex: "action",
        key: "action",
      },
    ];
    const data = ref<VisitLog[]>();
    const showDrawer = ref(false);
    const pagination = reactive<Pagination>({
        current: 1,
        pageSize: 10,
        total: 0
    })
    const loadData = () => {
        console.log(pagination, "请求")
      Service.methodVisitGet(pagination.pageSize, pagination.current)
        .then((res) => {
          data.value = res.data;
          pagination.total = res.total ?? 0;
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    };
    loadData();

    const slots = {
      bodyCell: (data: any) => {
        if (data.column.key === "status_code") {
          return (
            <Space>
              <Tag
                color={data.record.status_code !== 200 ? "error" : "success"}
              >
                {data.record.status_code}
              </Tag>
            </Space>
          );
        } else if (data.column.key === "action") {
          return (
            <Space>
              <a
                onClick={() => {
                  showDrawer.value = true;
                }}
              >
                查看请求头
              </a>

              <Drawer v-model:visible={showDrawer.value} title="请求头">
                  {data}
                {data.record.headers}
              </Drawer>
            </Space>
          );
        }
      },
    };
    return () => (
      <div>
        <Table columns={columns} dataSource={data.value} v-slots={slots} 
        pagination={pagination}/>
      </div>
    );
  },
});
