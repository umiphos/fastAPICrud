from typing import List, Optional
from pydantic import BaseModel
from app.api.lessons.models import Lesson

class Course(BaseModel):
    id: Optional[int]
    title: str
    description: str
    lessons: Optional[List[Lesson]]
