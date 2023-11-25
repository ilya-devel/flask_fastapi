from pydantic import BaseModel, Field


class TaskIn(BaseModel):
    title: str
    description: str
    done: bool = Field(default=False)


class Task(TaskIn):
    id: int
