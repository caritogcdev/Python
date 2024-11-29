from sqlalchemy import create_engine # Esta clase permite conectarme al motor SQL de MySQL
from sqlalchemy.ext.declarative import declarative_base # Desde mi archivo models para conectarme a mi DB
from sqlalchemy.orm import sessionmaker # Mapear o hacer una conexión entre mi modelo y mi base de datos
from Soluas.config import settings

# Configuración para conectarme al archivo de configuración
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()
