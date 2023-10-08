from starlette.testclient import TestClient


def test_ping(client: TestClient):
    response = client.get('/v1/ping')
    assert response.status_code == 200
