import time
from datetime import datetime
from typing import List, Literal

from models.products import Product
from pydantic import BaseModel, Field

from models.users import User


class OrderIn(BaseModel):
    id_user: int = Field(..., gt=0)
    id_products: List[int]
    date_order: str = Field(default=time.strftime("%Y-%m-%d %H:%M:%S"), format="%Y-%m-%d %H:%M:%S")
    is_status: Literal['canceled', 'in progress', 'done'] = Field(default='in progress')


class Order(BaseModel):
    id: int = Field(..., gt=0)
    user: User
    products: List[Product]
    date_order: datetime = Field(..., format="%Y-%m-%d %H:%M:%S")
    is_status: Literal['canceled', 'in progress', 'done'] = Field(default='in progress')


if __name__ == '__main__':
    order = OrderIn(id_user=1, id_products=[1, 2, 3])
    print(order.model_dump(mode='json'))
    print(order.date_order)
