from fastapi.testclient import TestClient
from mcpgh.main import app

client = TestClient(app)


def test_lists_and_refuses_apply():
    assert "list_issues" in client.get("/tools").json()["tools"]
    ok = client.post("/call", json={"name": "list_issues", "arguments": {"q": "status"}}).json()
    assert ok["ok"] is True
    assert ok["applied"] is False
    refused = client.post("/call", json={"name": "list_issues", "arguments": {"cmd": "kubectl apply"}}).json()
    assert refused["ok"] is False
