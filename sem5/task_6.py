import uvicorn
from typing import Annotated
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import logging
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory='templates')


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = [User(id=1, name="test", email="test", password="Test")]


@app.get('/users/')
def get_users(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'users': users})


@app.post('/users/')
def add_user(
        request: Request,
        id: Annotated[int, Form()],
        name: Annotated[str, Form()],
        email: Annotated[str, Form()],
        password: Annotated[str, Form()]
):
    users.append(User(id=id, name=name, email=email, password=password))
    return templates.TemplateResponse('index.html', {'request': request, 'users': users})


if __name__ == '__main__':
    uvicorn.run("task_6:app", host='localhost', port=8000, reload=True)
