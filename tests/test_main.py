def test_healthcheck(client):
    """Prueba el estado del endpoint /healthcheck."""
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "success", "message": "API is running."}
