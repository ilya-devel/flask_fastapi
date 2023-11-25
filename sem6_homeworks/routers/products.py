from fastapi import APIRouter, HTTPException
from models.products import Product, ProductIn

from db import database, products

router = APIRouter()


@router.get('/products/', response_model=list[Product])
async def get_products():
    products_ = products.select()
    return await database.fetch_all(products_)


@router.get('/products/{id}/', response_model=Product)
async def get_product(id: int):
    query = products.select().where(products.c.id == id)
    result = await database.fetch_one(query)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Product not found")


@router.post('/products/')
async def add_product(product: ProductIn):
    query = products.insert().values(**product.dict())
    await database.execute(query)
    return {'message': 'Product added'}


@router.put('/products/{id}/', response_model=Product)
async def update_product(id: int, product: ProductIn):
    query = products.update().where(products.c.id == id).values(**product.dict())
    result = await database.execute(query)
    if result:
        return {**product.dict(), 'id': id}
    raise HTTPException(status_code=404, detail="Product not found")


@router.delete('/products/')
async def delete_product(id: int):
    query = products.delete().where(products.c.id == id)
    result = await database.execute(query)
    if result:
        return {'message': 'Product deleted'}
    raise HTTPException(status_code=404, detail='Product not found')
