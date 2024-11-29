from pydantic_settings import BaseSettings # para tipar

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://user:password@localhost/dbname"

    class Config:
        env_file = ".env"
    
settings = Settings()