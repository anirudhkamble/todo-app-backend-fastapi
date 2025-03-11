from pydantic import BaseModel


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    password: str


class UserUpdate(BaseModel):
    first_name: str
    last_name: str
    password: str


class TodoCreate(BaseModel):
    item: str
    description: str
    user_id: int


class TodoUpdate(BaseModel):
    item: str
    description: str
    status: bool
    user_id: int
