from typing import List
from pydantic import BaseModel, Field

from app.schemas.student_schema import StudentInput


class PredictionOutput(BaseModel):
    prob_evasao: float = Field(..., ge=0, le=1, description="Probabilidade de evasão")
    classe_prevista: int = Field(..., description="Classe prevista (0 = permanece, 1 = evadiu)")
    # threshold: float = Field(..., description="Threshold usado para classificar")


class BatchPredictionInput(BaseModel):
    alunos: List[StudentInput]


class BatchPredictionOutputItem(BaseModel):
    aluno_index: int
    prob_evasao: float
    classe_prevista: int
