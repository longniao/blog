from fastapi import FastAPI, responses
from tortoise import Tortoise

from middlewares import middleware_list
from urls import routes


async def init_orm():
    await Tortoise.init(db_url="sqlite://db.sqlite3", modules={"models": ["models"]})
    await Tortoise.generate_schemas()


app = FastAPI(
    routes=routes,
    middleware=middleware_list,
    on_startup=[init_orm],
    on_shutdown=[Tortoise.close_connections],
    default_response_class=responses.ORJSONResponse,
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True)