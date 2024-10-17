from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def main_page():
    return 'Главная страница'


@app.get("/user/{user_id}")
async def user_enter(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=25)]):
    return f'Вы вошли как пользователь № {user_id}'


@app.get("/user/{username}/{age}")
async def user_info(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
                                                  example="Vladislav")],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='28')]):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
