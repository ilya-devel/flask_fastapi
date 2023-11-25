from pydantic import BaseModel, Field


class ProductIn(BaseModel):
    name: str = Field(..., min_length=2)
    description: str = Field(default=' ')
    price: float = Field(..., gt=0, le=10000)


class Product(ProductIn):
    id: int
