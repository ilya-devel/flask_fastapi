from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


# class LoginData(BaseModel):
#     username: str
#     password: str
#
#
# @app.post("/login/")
# async def login(login_data: Annotated[LoginData, Form()]):
#     return {"username": login_data.username}
#
#
# @app.post('/users/')
# def create_users(request: Request, name: Annotated[str, Form()], email: Annotated[str, Form()]):
#     user = User(id=len(collection) + 1, email=email, name=name)
#     collection.append(user)
#     return templates.TemplateResponse("users.html", {"request": request, "users": collection})


@app.get('/')
async def root():
    return {'message': 'hello'}
