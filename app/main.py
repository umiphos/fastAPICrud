from fastapi import FastAPI
from .core.settings import settings
from .api.courses import endpoints as courses
from .api.lessons import endpoints as lessons
from .api.questions import endpoints as questions


app = FastAPI(
    title="Curricular control",
    docs_url='/api/v1/scholar_control/docs' if settings.ENV in ("develop") else None
)

app.include_router(courses.router, prefix="/courses", tags=["courses"])
app.include_router(lessons.router, prefix="/courses/{course_id}/lessons", tags=["lessons"])
app.include_router(questions.router, prefix="/lessons/{lesson_id}/questions", tags=["questions"])
