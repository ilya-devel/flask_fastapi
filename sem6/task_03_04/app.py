from fastapi import FastAPI
import uvicorn
from db import database
from routers.tasks import router as router_tasks


app = FastAPI()


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

app.include_router(router_tasks, tags=["tasks"])

if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host='localhost',
        port=8000,
        reload=True
    )
