from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

class Message(BaseModel):
    id: int = None
    text: str


@app.get("/")
def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}")
def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id - 1]})
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')



@app.post("/user/{username}/{age}")
def create_user(new_user: User, username: Annotated[str, Path(min_length=3, max_length=20, description="Username",
                                                              example="Vladislav")],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='28')]) -> User:
    new_user.id = len(users) + 1
    new_user.username = username
    new_user.age = age
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='User ID', example='25')],
                      username: Annotated[str, Path(min_length=3, max_length=20, description="Username",
                                                    example="Vladislav")],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='28')]):
    try:
        user: User = users[user_id - 1]
        user.username = username
        user.age = age
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete("/user/{user_id}")
def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='User ID', example='25')]) -> User:
    try:
        user = users[user_id - 1]
        users.pop(user_id - 1)
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')