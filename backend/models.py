from tortoise import fields, models


class BaseModel(models.Model):
    id = fields.IntField(pk=True)
    created = fields.DatetimeField(null=True, auto_now_add=True, description="创建时间")
    modified = fields.DatetimeField(null=True, auto_now=True, description="更新时间")

    class Meta:
        abstract = True


class VisitLog(BaseModel):
    host = fields.CharField(max_length=60, description="访问者IP")
    url = fields.CharField(max_length=200, description="请求地址")
    method = fields.CharField(max_length=10, description="请求方式")
    headers = fields.JSONField(description="请求头")
    status_code = fields.IntField(description="响应状态码")

    class Meta:
        table_description = "访问日志"


class Article(BaseModel):
    title = fields.CharField(max_length=50, description="标题")
    content = fields.TextField(description="文章内容")
    visit = fields.IntField(default=0, description="访问量")
    category = fields.ForeignKeyField(
        "models.Category", on_delete=fields.SET_NULL, null=True
    )

    class Meta:
        table_description = "文章表"


class Category(BaseModel):
    name = fields.CharField(max_length=10, description="分类名称")

    class Meta:
        table_description = "分类"


class Project(BaseModel):
    name = fields.CharField(max_length=30, description="项目名称")
    desc = fields.TextField(description="项目描述")

    class Meta:
        table_description = "开源项目"


class Comment(BaseModel):
    host = fields.CharField(max_length=100, description="访问者IP")
    content = fields.TextField(description="评论内容")
    prent = fields.ForeignKeyField("models.Comment", on_delete=fields.CASCADE)

    class Meta:
        table_description = "评论表"
