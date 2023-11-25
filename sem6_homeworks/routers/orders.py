from datetime import datetime

from fastapi import APIRouter, HTTPException

from db import database, orders, users, products, order_products
from models.orders import Order, OrderIn
from models.users import User, UserIn
from models.products import Product, ProductIn

router = APIRouter()


@router.get('/orders/', response_model=list[Order])
async def get_orders():
    results = []
    orders_ = orders.select()
    for order in await database.fetch_all(orders_):
        result = {
            'id': order.id,
            'date_order': order.date_order,
            'is_status': order.is_status,
        }
        user = users.select().where(users.c.id == order.id_user)
        result['user'] = await database.fetch_one(user)
        result['products'] = []
        query = order_products.select().where(order_products.c.id_order == order.id)
        for product in await database.fetch_all(query):
            product_ = products.select().where(products.c.id == product.id_product)
            result['products'].append(await database.fetch_one(product_))
        results.append(result)
    return results


@router.get('/orders/{id}', response_model=Order)
async def get_order(id: int):
    order = orders.select().where(orders.c.id == id)
    order = await database.fetch_one(order)
    if order:
        result = {
            'id': order.id,
            'date_order': order.date_order,
            'is_status': order.is_status,
        }
        user = users.select().where(users.c.id == order.id_user)
        result['user'] = await database.fetch_one(user)
        result['products'] = []
        query = order_products.select().where(order_products.c.id_order == order.id)
        for product in await database.fetch_all(query):
            product_ = products.select().where(products.c.id == product.id_product)
            result['products'].append(await database.fetch_one(product_))
        return result
    raise HTTPException(status_code=404, detail='Order not found')


@router.delete('/orders/')
async def delete_order(id: int):
    order = orders.delete().where(orders.c.id == id)
    lst_product = order_products.delete().where(order_products.c.id_order == id)
    result = await database.execute(query=order)
    if not result:
        raise HTTPException(status_code=404, detail='Order not found')
    result = await database.execute(query=lst_product)
    if not result:
        raise HTTPException(status_code=404, detail='List products by order not found')
    return {'message': 'Order deleted'}


@router.post('/orders/')
async def add_order(order: OrderIn):
    user = await database.fetch_one(users.select().where(users.c.id == order.id_user)),
    result = {
        'id_user': order.id_user,
        'date_order': datetime.strptime(order.date_order, "%Y-%m-%d %H:%M:%S"),
        'is_status': order.is_status
    }
    new_order = orders.insert().values(**result)
    result['user'] = user
    result['id'] = await database.execute(new_order)
    result['products'] = []
    for product in order.id_products:
        new_position = order_products.insert().values(
            id_order=result['id'],
            id_product=product,
        )
        await database.execute(new_position)
        result['products'].append(await database.fetch_one(products.select().where(products.c.id == product)))
    return result


@router.put('/orders/{id}')
async def update_order(id: int, order: OrderIn):
    user = await database.fetch_one(users.select().where(users.c.id == order.id_user)),
    result = {
        'id_user': order.id_user,
        'date_order': datetime.strptime(order.date_order, "%Y-%m-%d %H:%M:%S"),
        'is_status': order.is_status
    }
    update_order = orders.update().where(orders.c.id == id).values(**result)
    if await database.execute(update_order):
        result['user'] = user
        result['id'] = id
        print('update order')
        del_old_products = order_products.delete().where(order_products.c.id_order == id)
        await database.execute(del_old_products)
        result['products'] = []
        for product in order.id_products:
            new_position = order_products.insert().values(
                id_order=result['id'],
                id_product=product,
            )
            await database.execute(new_position)
            result['products'].append(await database.fetch_one(products.select().where(products.c.id == product)))
        return result
    HTTPException(status_code=404, detail='Order not found')
