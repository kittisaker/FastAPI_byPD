# FastAPI_byPD : Chapter-2 Creating a simple route

## Simple route
```python
from fastapi import FastAPI
import uvicorn

app = FastAPI()

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

Web browser : url "http://localhost:8080/hello"
```
{"hello":"world"}
```

## Document
Web browser : url "http://localhost:8080/docs"

---