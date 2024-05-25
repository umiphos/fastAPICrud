from typing import Optional
from pydantic import BaseModel

class Course(BaseModel):
    id: Optional[int]
    title: str
    description: str
