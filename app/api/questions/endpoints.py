from fastapi import APIRouter, HTTPException, Depends, status
from .models import Question
from app.core.database import get_current_user_role
from app.api.lessons.endpoints import lessons_db


router = APIRouter()

# Dummy in-memory storage
questions_db = {}

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_question(lesson_id: int, question: Question, username: str = Depends(get_current_user_role)):
    if username != 'professor':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    lesson = lessons_db.get(lesson_id)
    if not lesson:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lesson not found")
    question_id = len(questions_db) + 1
    question.id = question_id
    questions_db[question_id] = question
    lesson.questions.append(question)
    return question
