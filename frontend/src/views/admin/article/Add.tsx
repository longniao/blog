import { defineComponent, reactive } from "vue";
import {Divider, Input, message } from "ant-design-vue"
import MdEditor from 'md-editor-v3';
import type { ArticleIn } from "@/client";
import { Service } from "@/client";
import { useRouter } from "vue-router";

export default defineComponent({
    name: 'Add',
    setup(){
        
        const article = reactive<ArticleIn>({
            title: '',
            content: ''
        })

        const router = useRouter()

        const onSave = ()=>{
            // todo 校验标题是否为空， 
            if (article.title.trim.length === 0 && article.content.length === 0){
                message.error("请检查是否填写完整")
                return
            }

            Service.methodArticlePost(article).then(r => {
                if (r.code === 200) {
                    message.success(r?.msg ?? '操作成功')
                    router.push({
                        name: "Article"
                    })
                }
            }).catch(e => console.log(e))
        }
        return () => (
            <>
            <Input placeholder={"标题，发布文章点击下面的保存图标"} v-model:value={article.title}/>
            <Divider type="vertical"/>
            <MdEditor modelValue={article.content} onChange={(v: string) => (article.content = v)} style={
                {height: "650px"}
            } onSave={onSave}/>
            </>
        )
    }
})