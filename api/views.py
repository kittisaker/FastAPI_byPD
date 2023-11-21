from typing import List
from fastapi import APIRouter
from schemas.user import UserIn, UserOut

api = APIRouter(prefix= "/api")

users: List[UserOut] = [
    UserOut(id=1, first_name= "John", last_name= "Smith", email= "jsmith@gmail.com"),
    UserOut(id=2, first_name= "Jane", last_name= "Doe", email= "jdoe@gmail.com"),
    UserOut(id=3, first_name= "Jack", last_name= "Jones", email= "jjones@gmail.com"),
    UserOut(id=4, first_name= "Sarah", last_name= "Smith", email= "ssmith@gmail.com"),
]

def save_user(user: UserIn):
    user_data = user.model_dump()
    user_data.pop("password")
    user_id = users[-1].id + 1
    user_out = UserOut(id=user_id, **user_data)
    user.append(user_out)
    return user_out

@api.get("/users")
def get_users() -> List[UserOut]:
    return users

@api.post("/users", status_code=201)
def create_user(user: UserIn) -> UserOut:
    user_out = save_user(user)
    return user_out