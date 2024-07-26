from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class Todo(BaseModel):
    name: str
    description: str
    complete: bool
