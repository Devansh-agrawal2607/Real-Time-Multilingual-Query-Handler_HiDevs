from fastapi.testclient import TestClient
from backend.server import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_translate_endpoint():
    test_query = "Bonjour"
    response = client.post("/translate", data={"query": test_query})
    assert response.status_code == 200
    assert "original_query" in response.json()
    assert "translated_query" in response.json()
