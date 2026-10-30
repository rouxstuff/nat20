from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings

if settings.database_url.startswith("sqlite"):
     connect_args ={"check_same_thread": False} 
else:
    connect_args = {}

engine = create_engine(settings.database_url, connect_args=connect_args)

class Base(DeclarativeBase):
     pass

def get_db():
     pass