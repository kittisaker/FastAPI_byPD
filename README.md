# FastAPI_byPD : Chapter-4 Pydantic Models

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