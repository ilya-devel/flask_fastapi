import uvicorn
from fastapi import FastAPI

from db import database, users, products, order_products, orders
from routers.products import router as router_products
from routers.users import router as router_users
from routers.orders import router as router_orders

app = FastAPI()


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.get('/fill-db/')
async def fill_db():
    for i in range(1, 10):
        q = users.insert().values(
            first_name=f'user_{i}',
            last_name=f'last_{i}',
            email=f'email{i}@email.com',
            password='password'
        )
        await database.execute(q)
    for i in range(1, 20):
        q = products.insert().values(
            name=f'product_{i}',
            description=f'description_{i}',
            price=i
        )
        await database.execute(q)
    for i in range(1, 5):
        q = orders.insert().values(
            id_user=i,
            is_status='in progress'
        )
        await database.execute(q)
    for i in range(1, 5):
        for j in range(1, 4):
            q = order_products.insert().values(
                id_order=i,
                id_product=j
            )
            await database.execute(q)


app.include_router(router_users, tags=['users'])
app.include_router(router_products, tags=['products'])
app.include_router(router_orders, tags=['orders'])

if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        host='localhost',
        port=8000,
        reload=True
    )
