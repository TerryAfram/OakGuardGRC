from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "active"

def test_telemetry_endpoint():
    response = client.get("/telemetry")
    assert response.status_code == 200
    data = response.json()
    assert "signals" in data
    assert len(data["signals"]) > 0

def test_triage_endpoint():
    payload = {"description": "Unauthorized privilege escalation detected."}
    response = client.post("/triage", json=payload)
    assert response.status_code == 200
    assert response.json()["risk_score"] == "High"
