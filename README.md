# FastAPI_byPD : Chapter-6 Fetch all users

## Fetch all users
views.py :
```python
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
def get_users():
    return users
```

docs : "http://localhost:8080/docs"
try  : "http://localhost:8080/api/users"

```json
[
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Smith",
    "email": "jsmith@gmail.com"
  },
  {
    "id": 2,
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "jdoe@gmail.com"
  },
  {
    "id": 3,
    "first_name": "Jack",
    "last_name": "Jones",
    "email": "jjones@gmail.com"
  },
  {
    "id": 4,
    "first_name": "Sarah",
    "last_name": "Smith",
    "email": "ssmith@gmail.com"
  }
]
```

views.py :
```python
@api.get("/users")
def get_users():
    return users
```

try  : "http://localhost:8080/api/users"

```json
[
  {
    "id": 0,
    "first_name": "string",
    "last_name": "string",
    "email": "user@example.com"
  }
]
```

---