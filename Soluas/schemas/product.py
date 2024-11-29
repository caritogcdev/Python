from pydantic import BaseModel
from datetime import datetime
from typing import Optional # Permite definirle opcionalmente un tipo de dato por ejemplo entero o sino un null

class ProductBase(BaseModel):
    name : str
    description : str
    price : float

class ProductCreate(ProductBase):
    pass 

class ProductUpdate(BaseModel):
    name : Optional[str] = None
    description : Optional[str] = None
    price : Optional[float] = None

class Product(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True