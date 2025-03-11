from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db_instance, engine
from app.models import Todo, User
from app.schema import TodoCreate, TodoUpdate, UserCreate, UserUpdate



app = FastAPI()


@app.get("/users")
async def get_users(db: Session = Depends(get_db_instance)):
    return db.query(User).all()

@app.post("/user")
async def create_user(user: UserCreate, db: Session = Depends(get_db_instance)):
    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": f"Created user: {user.first_name} {user.last_name}"}


@app.get("/todos")
async def get_todos(db: Session = Depends(get_db_instance)):
    return db.query(Todo).all()

@app.post("/todo")
async def create_todo(todo: TodoCreate, db: Session = Depends(get_db_instance)):
    new_todo = Todo(
        item=todo.item,
        description=todo.description,
        user_id=todo.user_id
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo
