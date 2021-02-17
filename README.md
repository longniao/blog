# blog
FastAPI Blog后端API

**账号 admin 密码 123456**

**线上服务地址: http://49.232.203.244:8001**

**线上接口文档地址: http://49.232.203.244:8001/docs**

# 部署

```shell
1. git clone https://github.com/zy7y/blog.git
2. cd blog
3. docker build -t blog .
4. docker run -d --name blog-api -p 8001:80 blog
```

![](https://gitee.com/zy7y/blog_images/raw/master/img/20210204163912.png)

# 问题
1. 目前评论相关接口存在问题.
~~2. 各接口应该丰富返回数据.~~

# 更新
1. 添加虚拟数据生成方法
2. 修改表结构
3. 修改接口返回内容(由于个人不熟悉ORM及SQL的应用，故查询数据库次数存在冗余，但接口返回相比之前清晰不少)

