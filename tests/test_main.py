from fastapi.testclient import TestClient
from ai_insurance_claims_processing_system.main import app 

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to the AI insurance Claims Processing system"