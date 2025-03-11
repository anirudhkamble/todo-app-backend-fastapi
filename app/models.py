from datetime import datetime

from sqlalchemy import Column, DATETIME, Integer, String, DATETIME, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id: int = Column(Integer, primary_key=True, index=True)
    first_name: int = Column(String(30), index=True)
    last_name: int = Column(String(30), index=True)
    password: int = Column(String(50), index=True)


class Todo(Base):
    __tablename__ = "todo"

    id: int = Column(Integer, primary_key=True, index=True)
    item: str = Column(String(50), index=True)
    description: str = Column(String(150), index=True)
    user_id: int = Column(Integer, ForeignKey("user.id"), index=True)
    status: bool = Column(Boolean, index=True, default=False)
    created: str = Column(DATETIME, index=True, default=datetime.now)

