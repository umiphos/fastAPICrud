from fastapi import APIRouter, HTTPException, Depends, status
from .models import Lesson
from app.api.courses.endpoints import courses_db
from app.core.database import get_current_user_role


router = APIRouter()

lessons_db = {}

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_lesson(course_id: int, lesson: Lesson, username: str = Depends(get_current_user_role)):
    if username != 'professor':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    course = courses_db.get(course_id)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    lesson_id = len(lessons_db) + 1
    lesson.id = lesson_id
    lessons_db[lesson_id] = lesson
    course.lessons.append(lesson)
    return lesson
