from typing import List
from fastapi import APIRouter
from schemas.user import UserOut

api = APIRouter(prefix= "/api")

users: List[UserOut] = [
    UserOut(id=1, first_name= "John", last_name= "Smith", email= "jsmith@gmail.com"),
    UserOut(id=2, first_name= "Jane", last_name= "Doe", email= "jdoe@gmail.com"),
    UserOut(id=3, first_name= "Jack", last_name= "Jones", email= "jjones@gmail.com"),
    UserOut(id=4, first_name= "Sarah", last_name= "Smith", email= "ssmith@gmail.com"),
]

@api.get("/users")
def get_users() -> List[UserOut]:
    return users