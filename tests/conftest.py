import sys
import os
import pytest
import openai
import requests

# Ensure project root is on sys.path so tests can import the local packages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class DummyResponse:
    def __init__(self, data=None, status=200):
        self._data = data or {"results": {"bindings": []}}
        self.status_code = status

    def json(self):
        return self._data

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"{self.status_code}")


@pytest.fixture(autouse=True)
def mock_openai_and_requests(monkeypatch):
    """Automatically mock OpenAI and requests.get for tests.

    The mocked OpenAI returns a simple SELECT query string. The mocked requests.get
    returns an empty results JSON. Tests that need to exercise the real network
    behavior can override these fixtures.
    """

    def fake_create(*args, **kwargs):
        return {"choices": [{"message": {"content": "SELECT ?s WHERE { ?s ?p ?o } LIMIT 1"}}]}

    monkeypatch.setattr(openai.ChatCompletion, "create", fake_create)

    def fake_get(*args, **kwargs):
        return DummyResponse()

    monkeypatch.setattr(requests, "get", fake_get)

    yield
