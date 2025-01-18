def test_predict_valid_input(client):
    """Prueba el endpoint /predict con entrada válida."""
    payload = {
        "gender": "Female",
        "age": 30,
        "annual_income": 60000
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "input" in response.json()
    assert "prediction" in response.json()
    assert response.json()["input"] == payload

def test_predict_invalid_input(client):
    """Prueba el endpoint /predict con entrada inválida."""
    payload = {
        "gender": "InvalidGender",
        "age": "invalid_age",
        "annual_income": -1000
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422  
