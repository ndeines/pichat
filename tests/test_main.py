from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_query_endpoint():
    response = client.post("/query", json={"query": "Show me paintings by Rembrandt"})
    assert response.status_code == 200
    assert "results" in response.json()
