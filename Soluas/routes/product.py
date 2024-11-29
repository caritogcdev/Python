from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from Soluas.database.connection import get_db
from Soluas.models.product import Product
from Soluas.schemas.product import ProductCreate, ProductUpdate as ProductSchema

router = APIRouter()

@router.post('/product', response_model=ProductSchema)
def create_product(product:ProductCreate, db:Session=Depends(get_db)):
    db_create = Product(**product.diet()) # enviar el objeto completo con los datos obligatorios, lo comparas y luego me los devuelves
    db.add(db_create)
    db.commit()
    db.refresh(db_create)
    return product

# {
#     "name": "arroz",
#     "description": "Hola",
#     "price": 251
# }