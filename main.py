from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid

app = FastAPI(title="Todo API", version="1.0.0")

# CORS middleware - FIXED CONFIGURATION
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://todos-eight-eta.vercel.app",
        "http://localhost:3000"  # For local development
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
    expose_headers=["*"]  # Expose all headers to the frontend
)

# Enhanced Todo model with more fields
class TodoItem(BaseModel):
    id: str
    task: str
    completed: bool = False
    created_at: datetime
    updated_at: datetime
    priority: int = 1  # 1-5 scale
    due_date: Optional[datetime] = None

class TodoCreate(BaseModel):
    task: str
    priority: int = 1
    due_date: Optional[datetime] = None

class TodoUpdate(BaseModel):
    task: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[int] = None
    due_date: Optional[datetime] = None

# In-memory database
todos = {}

@app.get("/")
def read_root():
    return {"message": "Todo API is running", "version": "1.0.0"}

@app.options("/todos")
async def options_todos():
    return {"message": "OK"}

@app.options("/todos/{todo_id}")
async def options_todo_id():
    return {"message": "OK"}

@app.get("/todos", response_model=List[TodoItem])
def get_all_todos(completed: Optional[bool] = None):
    if completed is not None:
        return [todo for todo in todos.values() if todo.completed == completed]
    return list(todos.values())

@app.get("/todos/{todo_id}", response_model=TodoItem)
def get_todo_by_id(todo_id: str):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[todo_id]

@app.post("/todos", response_model=TodoItem)
def create_new_todo(todo: TodoCreate):
    todo_id = str(uuid.uuid4())
    now = datetime.now()
    new_todo = TodoItem(
        id=todo_id,
        task=todo.task,
        priority=todo.priority,
        due_date=todo.due_date,
        created_at=now,
        updated_at=now
    )
    todos[todo_id] = new_todo
    return new_todo

@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo(todo_id: str, todo_update: TodoUpdate):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo = todos[todo_id]
    update_data = todo_update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(todo, field, value)
    
    todo.updated_at = datetime.now()
    todos[todo_id] = todo
    
    return todo

@app.delete("/todos/{todo_id}")
def delete_todo_by_id(todo_id: str):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
    return {"message": f"Todo with id {todo_id} deleted"}

@app.get("/todos/search/{query}")
def search_todos(query: str):
    results = []
    for todo in todos.values():
        if query.lower() in todo.task.lower():
            results.append(todo)
    return results

@app.get("/stats")
def get_stats():
    total = len(todos)
    completed = sum(1 for todo in todos.values() if todo.completed)
    pending = total - completed
    high_priority = sum(1 for todo in todos.values() if todo.priority >= 4)
    
    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "high_priority": high_priority
    }