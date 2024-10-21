from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Влад, возраст: 18'}


@app.get("/")
async def main_page():
    return 'Главная страница'


@app.get("/users")
async def get_all_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=3, max_length=20, description="Username",
                                                    example="Vladislav")],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='28')]) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f'Имя: {username}, Возраст: {age}'
    return f'User {current_index} is registered'


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='User ID', example='25')],
                      username: Annotated[str, Path(min_length=3, max_length=20, description="Username",
                                                    example="Vladislav")],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='28')]) -> str:
    if str(user_id) in users:
        users[str(user_id)] = f'Имя: {username}, Возраст: {age}'
        return f"The user {user_id} is registered"
    return f'User {user_id} does not exist'


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='User ID', example='25')]) -> str:
    users.pop(str(user_id))
    return f"User {user_id} has been deleted"
