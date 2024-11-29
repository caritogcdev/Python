from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from Soluas.database.connection import Base # importando la conexión

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(200))
    price = Column(Float)
    creat_at = Column(DateTime, default=datetime.utcnow)
    update_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

