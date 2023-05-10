from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from models import Base

def test():
    return

engine = create_engine("sqlite:///sql_app.db", echo=True)

Base.metadata.create_all(engine)