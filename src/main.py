from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.database import engine, Base, get_db
from src.models import Customer
from src.schemas import PredictionInput, PredictionOutput
from src.utils import predict_category

app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)


@app.get("/healthcheck")
def healthcheck():
    return {"status": "success", "message": "API is running."}


@app.post("/predict", response_model=PredictionOutput)
def predict(data: PredictionInput, db: Session = Depends(get_db)):

    # Realizar predicción
    prediction = predict_category(data.gender, data.age, data.annual_income)

    # Guardar cliente y predicción en la base de datos
    new_customer = Customer(
        gender=data.gender,
        age=data.age,
        annual_income=data.annual_income,
        prediction=prediction,
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return {"input": data.dict(), "prediction": prediction}
