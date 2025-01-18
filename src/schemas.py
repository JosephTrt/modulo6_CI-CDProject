from pydantic import BaseModel


class PredictionInput(BaseModel):
    gender: str
    age: int
    annual_income: float


class PredictionOutput(BaseModel):
    input: dict
    prediction: str
