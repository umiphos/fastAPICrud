from enum import Enum
from typing import List, Optional
from pydantic import BaseModel

# Enums for Question Types
class QuestionType(str, Enum):
    BOOLEAN = "boolean"
    MULTIPLE_CHOICE_ONE = "multiple_choice_one"
    MULTIPLE_CHOICE_MULTIPLE = "multiple_choice_multiple"
    MULTIPLE_CHOICE_ALL_CORRECT = "multiple_choice_all_correct"

# Models
class Question(BaseModel):
    id: Optional[int]
    type: QuestionType
    text: str
    options: Optional[List[str]] = None
    correct_answers: List[str]
    score: int
