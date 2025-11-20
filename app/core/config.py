from pathlib import Path
from pydantic import BaseModel


class Settings(BaseModel):
    api_name: str = "API de Predição de Evasão"
    api_version: str = "1.0"
    model_path: Path = Path("model/logistic_model.pkl")


settings = Settings()
