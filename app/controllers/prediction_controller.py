from typing import List

from app.schemas.student_schema import StudentInput
from app.schemas.prediction_schema import (
    PredictionOutput,
    BatchPredictionInput,
    BatchPredictionOutputItem,
)
from app.services.ml_service import ml_service

THRESHOLD = 0.5


def predict_single(student: StudentInput) -> PredictionOutput:
    data_dict = student.model_dump()
    prob = ml_service.predict_proba_single(data_dict)
    classe = 1 if prob >= THRESHOLD else 0

    return PredictionOutput(
        prob_evasao=prob,
        classe_prevista=classe,
        threshold=THRESHOLD,
    )


def predict_batch(batch: BatchPredictionInput) -> List[BatchPredictionOutputItem]:
    outputs: List[BatchPredictionOutputItem] = []

    for idx, student in enumerate(batch.alunos):
        data_dict = student.model_dump()
        prob = ml_service.predict_proba_single(data_dict)
        classe = 1 if prob >= THRESHOLD else 0

        outputs.append(
            BatchPredictionOutputItem(
                aluno_index=idx,
                prob_evasao=prob,
                classe_prevista=classe,
            )
        )

    return outputs
