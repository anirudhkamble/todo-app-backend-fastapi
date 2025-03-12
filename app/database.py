from pydantic import BaseModel
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from app.models import Base

DB_URL = "sqlite:///user.db"

engine = create_engine(DB_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(engine)

_inspect = inspect(engine)
for _table in _inspect.get_table_names():
    print(_table)


def get_db_instance():
    db = session()
    try:
        yield db
    finally:
        db.close()
