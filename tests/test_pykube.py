import pytest

from pykube import pykube


@pytest.fixture
def client():
    with pykube.app.test_client() as client:
        yield client


def test_hello(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, World!"
