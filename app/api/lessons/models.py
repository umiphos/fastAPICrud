from typing import Optional
from pydantic import BaseModel


class Lesson(BaseModel):
    id: Optional[int]
    title: str
    approval_threshold: int
