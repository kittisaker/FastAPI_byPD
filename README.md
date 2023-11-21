# FastAPI_byPD : Chapter-3 Creating an APIRouter

## Creating an APIRouter
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

---