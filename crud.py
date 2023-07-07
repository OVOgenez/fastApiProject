from sqlalchemy.orm import Session
import schemas
import models


def create_task(db: Session, user_id: int, task: schemas.TaskCreate):
    db_task = models.Task(content=task.content, priority=task.priority, user_id=user_id)
    db.add(db_task)
    db.commit()
    return db_task


def get_tasks(db: Session, user_id: int, priority: schemas.Priority, sort: schemas.Sort):
    query = db.query(models.Task).filter_by(user_id=user_id)
    if priority:
        query = query.filter_by(priority=priority)
    if sort:
        query = query.order_by(sort)
    return query.all()


def delete_task(db: Session, user_id: int, task_id: id):
    db_task = db.query(models.Task).filter_by(id=task_id).first()
    if not db_task:
        return 404
    if db_task.user_id != user_id:
        return 403
    else:
        db.delete(db_task)
        db.commit()
