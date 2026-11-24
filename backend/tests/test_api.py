import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.config import settings
from app.services import advisory as advisory_service

client = TestClient(app)

def test_root_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert client.head("/").status_code == 200

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert "ai_configured" in response.json()

def test_languages():
    response = client.get("/api/v1/languages")
    assert response.status_code == 200
    assert len(response.json()) == 6

def test_advisory_requires_provider_key(monkeypatch):
    monkeypatch.setattr(settings, "llm_api_key", None)
    response = client.post("/api/v1/advisory", json={
        "language":"mr","crop":"cotton","location":"Nashik","question":"How should I plan irrigation?"
    })
    assert response.status_code == 503
    assert response.json()["detail"]["code"] == "model_not_configured"

def test_advisory_returns_model_generated_answer(monkeypatch):
    async def fake_generate(messages):
        assert "Bharat Krishi AI" in messages[0]["content"]
        assert "Nashik" in messages[-1]["content"]
        return "या आठवड्यातील पाणी व्यवस्थापनासाठी आधी जमिनीतील ओलावा तपासा."
    monkeypatch.setattr(advisory_service, "generate_with_provider", fake_generate)
    response = client.post("/api/v1/advisory", json={
        "language":"mr","crop":"cotton","location":"Nashik","question":"How should I plan irrigation?"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "generated"
    assert "ओलावा" in response.json()["answer"]

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
