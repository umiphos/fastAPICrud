from typing import List, Optional
from pydantic import BaseModel
from app.api.questions.models import Question

class Lesson(BaseModel):
    id: Optional[int]
    title: str
    approval_threshold: int
    questions: List[Question]
