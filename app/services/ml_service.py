import joblib
import pandas as pd

from app.core.config import settings


class MLService:
    def __init__(self):
        self.model = self._load_model()

    def _load_model(self):
        try:
            model = joblib.load(settings.model_path)
            print(f"Modelo carregado de {settings.model_path}")
            return model
        except Exception as e:
            print(f"Erro ao carregar modelo: {e}")
            return None

    def is_ready(self) -> bool:
        return self.model is not None

    def predict_proba_single(self, data: dict) -> float:
        """
        Recebe um dict com os campos do aluno e devolve a probabilidade de evasão.
        """
        if not self.is_ready():
            raise RuntimeError("Modelo não carregado")

        df = pd.DataFrame([data])
        proba = self.model.predict_proba(df)[:, 1][0]
        return float(proba)


ml_service = MLService()
