from typing import List

from fastapi import APIRouter, HTTPException

from app.schemas.student_schema import StudentInput
from app.schemas.prediction_schema import (
    PredictionOutput,
    BatchPredictionInput,
    BatchPredictionOutputItem,
)
from app.controllers import prediction_controller
from app.services.ml_service import ml_service

router = APIRouter(tags=["Predição de Evasão"])


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "model_loaded": ml_service.is_ready(),
    }


@router.post("/predict", response_model=PredictionOutput)
def predict(student: StudentInput):
    if not ml_service.is_ready():
        raise HTTPException(status_code=500, detail="Modelo não carregado")

    return prediction_controller.predict_single(student)


@router.post("/predict_batch", response_model=List[BatchPredictionOutputItem])
def predict_batch(batch: BatchPredictionInput):
    if not ml_service.is_ready():
        raise HTTPException(status_code=500, detail="Modelo não carregado")

    return prediction_controller.predict_batch(batch)
