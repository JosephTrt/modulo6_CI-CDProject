import pytest
from fastapi.testclient import TestClient
from src.main import app


@pytest.fixture
def client():
    """Cliente de pruebas para interactuar con la API."""
    return TestClient(app)
