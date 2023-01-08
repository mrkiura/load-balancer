import pytest


from loadbalancer import loadbalancer


@pytest.fixture
def client():
    with loadbalancer.test_client() as client:
        yield client


def test_hello_client(client):
    response = client.get('/')
    assert "hello" in response.data.decode('utf-8').lower()