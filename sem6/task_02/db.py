import sqlalchemy
import databases
from settings import settings

DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String(20)),
    sqlalchemy.Column("last_name", sqlalchemy.String(20)),
    sqlalchemy.Column('birthday', sqlalchemy.Date()),
    sqlalchemy.Column("email", sqlalchemy.String(80)),
    sqlalchemy.Column('address', sqlalchemy.String(250)),
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
metadata.create_all(engine)
