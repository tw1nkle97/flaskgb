from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID, uuid4

# Модель задачи с Pydantic
class Task(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    title: str
    description: str
    completed: bool = False

# Модель для обновления задачи
class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]

# Создание экземпляра FastAPI
app = FastAPI()

# Хранилище задач
tasks = {}

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/tasks", response_model=List[Task])
async def read_tasks():
    return list(tasks.values())

@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: UUID):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    tasks[task.id] = task
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: UUID, task_update: TaskUpdate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task = tasks[task_id]
    task_data = task.dict()
    update_data = task_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        task_data[key] = value
    
    tasks[task_id] = Task(**task_data)
    return tasks[task_id]

@app.delete("/tasks/{task_id}", response_model=Task)
async def delete_task(task_id: UUID):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks.pop(task_id)
