from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    head_response = client.head("/")
    assert head_response.status_code == 200

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

def test_advisory_cors_preflight():
    response = client.options(
        "/api/v1/advisory",
        headers={
            "Origin": "http://localhost:5173",
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "content-type",
        },
    )
    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == "http://localhost:5173"
    assert "POST" in response.headers["access-control-allow-methods"]
