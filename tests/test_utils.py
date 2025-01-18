from src.utils import predict_category

def test_predict_category():
    """Prueba la función de predicción con valores válidos."""
    gender = "Female"
    age = 25
    annual_income = 75000
    prediction = predict_category(gender, age, annual_income)
    assert prediction in ["High", "Low"]
