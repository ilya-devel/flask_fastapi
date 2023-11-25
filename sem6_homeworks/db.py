import time
from datetime import datetime

import databases
import sqlalchemy
from sqlalchemy.sql import func

from settings import settings

DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('first_name', sqlalchemy.String(20)),
    sqlalchemy.Column('last_name', sqlalchemy.String(20)),
    sqlalchemy.Column('email', sqlalchemy.String(100), unique=True),
    sqlalchemy.Column('password', sqlalchemy.String(255))
)

products = sqlalchemy.Table(
    'products',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String(255)),
    sqlalchemy.Column('description', sqlalchemy.Text),
    sqlalchemy.Column('price', sqlalchemy.DECIMAL)
)

orders = sqlalchemy.Table(
    'orders',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('id_user', sqlalchemy.Integer, sqlalchemy.ForeignKey(users.c.id)),
    sqlalchemy.Column('date_order', sqlalchemy.DateTime(timezone=True),
                      server_default=func.now(), onupdate=func.current_timestamp()),
    sqlalchemy.Column('is_status', sqlalchemy.String(20))
)

order_products = sqlalchemy.Table(
    'order_products',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('id_order', sqlalchemy.ForeignKey(orders.c.id)),
    sqlalchemy.Column('id_product', sqlalchemy.ForeignKey(products.c.id)),
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
metadata.create_all(engine)
