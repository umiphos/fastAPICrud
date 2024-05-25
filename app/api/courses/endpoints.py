from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from .models import Course
from app.core.database import get_current_user_role

router = APIRouter()


courses_db = {}

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_course(course: Course, username: str = Depends(get_current_user_role)):
    if username != 'professor':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized")
    course_id = len(courses_db) + 1
    course.id = course_id
    courses_db[course_id] = course
    return course

@router.get("/", response_model=List[Course])
def get_courses():
    return list(courses_db.values())

@router.get("/{course_id}", response_model=Course)
def get_course(course_id: int):
    course = courses_db.get(course_id)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return course
