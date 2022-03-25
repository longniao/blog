import {defineComponent} from "vue";
import {RouterView} from "vue-router";
import {Service} from "@/client";

export default defineComponent({
    name: "App",
    setup(){
        const url = "//music.163.com/outchain/player?type=0&id=7349994422&auto=1&height=430"
        const style = {
            frameborder:"no",
            border:"0" ,
            marginwidth:"0",
            marginheight:"0",
            width:330,
            height:450,
            overflow: "auto"
        }

        const divStyle = {
            backgroundColor: "#fff",
            border: "1px solid #ccc",
            borderRadius: "4px",
            boxShadow: "0 0 8px rgba(0,0,0,.1)",
            padding: "10px",
            margin: "10px",
            width: "100%",
            height: "100%"
        }

        return () => (
            <>
                <div class={divStyle}>
                <iframe class={style} src={url}/>
                </div>
                <RouterView />
            </>
        )
    }
})