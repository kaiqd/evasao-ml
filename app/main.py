from fastapi import FastAPI

from app.views import prediction_view
from app.core.config import settings

app = FastAPI(
    title=settings.api_name,
    version=settings.api_version,
)


# Rotas
app.include_router(prediction_view.router)


@app.get("/")
def root():
    return {
        "message": "API de Predição de Evasão",
        "docs": "/docs",
    }
