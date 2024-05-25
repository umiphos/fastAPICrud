from fastapi import FastAPI
from .core.settings import settings
from .api.courses import endpoints as courses


app = FastAPI(
    title="Curricular control",
    docs_url='/api/v1/scholar_control/docs' if settings.ENV in ("develop") else None
)

app.include_router(courses.router, prefix="/courses", tags=["courses"])
