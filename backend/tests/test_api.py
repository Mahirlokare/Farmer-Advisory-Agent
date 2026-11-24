from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_languages():
    response = client.get("/api/v1/languages")
    assert response.status_code == 200
    assert len(response.json()) == 6

def test_advisory_does_not_invent_recommendations():
    response = client.post("/api/v1/advisory", json={
        "language":"mr","crop":"cotton","location":"Nashik","question":"How should I plan irrigation?"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "knowledge_base_pending"
    assert response.json()["requires_expert_review"] is True
