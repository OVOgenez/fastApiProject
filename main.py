from fastapi import FastAPI, APIRouter, Depends, Header
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from database import get_db
import schemas
import crud

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World!"}


def user_from_header(user_id: int = Header()) -> int:
    if user_id is None:
        raise HTTPException(status_code=401)
    return user_id


tasks_router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@tasks_router.post("/", response_model=int, status_code=201)
def create_task(task: schemas.TaskCreate, user_id: int = Depends(user_from_header), db: Session = Depends(get_db)):
    return crud.create_task(db, user_id=user_id, task=task).id


@tasks_router.get("/", response_model=list[schemas.TaskRead])
def read_tasks(priority: schemas.Priority = None, sort: schemas.Sort = None, user_id: int = Depends(user_from_header), db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, user_id=user_id, priority=priority, sort=sort)
    return tasks


@tasks_router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, user_id: int = Depends(user_from_header), db: Session = Depends(get_db)):
    error = crud.delete_task(db, user_id=user_id, task_id=task_id)
    if error:
        raise HTTPException(status_code=error)


app.include_router(tasks_router)
