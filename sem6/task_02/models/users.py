import datetime

from pydantic import BaseModel, Field, EmailStr


class UserIn(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=20)
    last_name: str = Field(..., min_length=2, max_length=20)
    birthday: datetime.date = Field(..., format='%Y-%m-%d')
    email: str = EmailStr
    address: str = Field(..., min_length=5)


class User(UserIn):
    id: int
