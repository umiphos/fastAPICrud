from fastapi import FastAPI
from .core.settings import settings


app = FastAPI(
    title="Curricular control",
    docs_url='/api/v1/scholar_control/docs' if settings.ENV in ("develop") else None
)
