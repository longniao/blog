import { defineComponent, reactive } from "vue";
import { useRoute, useRouter } from "vue-router";
import { Service } from "@/client";
import { message, Input, Divider } from "ant-design-vue";
import type { ArticleIn } from "@/client";
import MdEditor from "md-editor-v3";

export default defineComponent({
  name: "ArticleEdit",
  setup() {
    //  当前route 对象
    const route = useRoute();
    const currentArticle = {
      title: "",
      content: "",
      ...route.params,
    };
    const router = useRouter();
    const article = reactive<ArticleIn>({
      title: currentArticle.title ?? "",
      content: currentArticle.content ?? "",
    });
    const onSave = () => {
      // todo 校验标题是否为空，
      if (article.title.trim().length === 0 && article.content.length === 0) {
        message.error("请检查是否填写完整");
        return;
      }
      Service.methodArticlePkPut(Number(route.params.id), article)
        .then((res) => {
          if (res.code === 200) {
            message.success(res.msg ?? "操作成功");
            router.push({
              name: "Article",
            });
          }
        })
        .catch((err) => console.log(err));
    };

    return () => (
      <>
        <Input
          placeholder={"标题，发布文章点击下面的保存图标"}
          v-model:value={article.title}
        />
        <Divider type="vertical" />
        <MdEditor
          modelValue={article.content}
          onChange={(v: string) => (article.content = v)}
          style={{ height: "650px" }}
          onSave={onSave}
        />
      </>
    );
  },
});
