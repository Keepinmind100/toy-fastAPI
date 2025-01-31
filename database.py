from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import get_settings
from urllib.parse import quote_plus

settings = get_settings()

SQLALCHEMY_DATABASE_URL = (
    "mysql+mysqldb://"f"{settings.database_username}:{ quote_plus(settings.database_password)}""@127.0.0.1/fastAPI"
)

print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
