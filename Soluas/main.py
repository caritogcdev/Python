from fastapi import FastAPI
from Soluas.database.connection import engine
from Soluas.models import product as products_model
from Soluas.routes import product

products_model.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Soluas")

# Definiremos las rutas de nuestro proyecto
app.include_router(product.router, tags=["products"])

