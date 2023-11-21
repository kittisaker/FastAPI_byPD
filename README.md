# FastAPI_byPD : Chapter-3 Creating an APIRouter

## APIRouter
Create a folder name "api", then add file name "views.py"

views.py :
```python
from fastapi import APIRouter

api = APIRouter(prefix= "/api")
```

main.py :
```python
from fastapi import FastAPI
import uvicorn
from api.views import api

app = FastAPI()

app.include_router(api)

@app.get("/hello")
def hello():
    return {"hello": "world"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host= "localhost",
        port= 8080,
        reload= True
    )
```

## Pydantic Models
Create a folder name "schemas", then add file name "user.py"

user.py :
```python
from pydantic import BaseModel, EmailStr


class UserIn(BaseModel):
    first_name: str
    last_name : str
    email: EmailStr
    password: str

class UserIn(BaseModel):
    id: int
    first_name: str
    last_name : str
    email: EmailStr

class UpdateUser(BaseModel):
    first_name: str
    last_name : str
```

---