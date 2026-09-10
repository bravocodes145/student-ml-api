from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel


APPLICATION_VERSION = (Path(__file__).parent / "VERSION").read_text().strip()

app = FastAPI(title="student-ml-api", version=APPLICATION_VERSION)


class PredictionRequest(BaseModel):
    value: int | float


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "application_version": APPLICATION_VERSION,
        "model_version": "model-1",
    }


@app.post("/predict")
def predict(request: PredictionRequest) -> dict[str, int | float]:
    return {
        "input": request.value,
        "prediction": request.value * 2,
    }
