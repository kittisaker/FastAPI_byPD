# FastAPI_byPD : Chapter-1 Create app instance and run server

## Python dependency management
```shell
> poetry init
Package name [fastapi_bypd]:
Version [0.1.0]:
Description []:
Author [kittisaker <kittisak.hanheam@gmail.com>, n to skip]:
License []:
Compatible Python versions [^3.12]:

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no

Do you confirm generation? (yes/no) [yes] yes
```

```shell
> poetry add fastapi uvicorn email-validator
```

```shell
$ poetry shell
(fastapi-bypd-py3.12) D:\Projects_Python\FastAPI\Document_githubFastAPI\FastAPI_byPD>
```

## Create app instance
Create : main.py
```python
from fastapi import FastAPI
import uvicorn

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host= "localhost",
        port= 8080,
        reload= True
    )
```

## run server

```python
python main.py
```

Web Browser
```json
{"detail":"Not Found"}
```

---