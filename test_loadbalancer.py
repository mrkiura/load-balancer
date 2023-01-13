import pytest


from loadbalancer import loadbalancer


@pytest.fixture
def client():
    with loadbalancer.test_client() as client:
        yield client

def test_host_routing_tururu(client):
    result = client.get('/', headers={'Host': 'tururu.com'})
    assert b'tururu' in result.data

def test_host_routing_wawawa(client):
    result = client.get('/',  headers={'Host': 'wawawa.com'})

def test_hello_routing_not_found(client):
    result = client.get('/', headers={'Host': 'wuuuuui.com'})
    assert b'Not Found' in result.data
    assert 404 == result.status_code


def test_path_routing_tururu(client):
    result = client.get('/tururu')
    assert b'This is a tururu application.' in result.data


def test_path_routing_wawawa(client):
    result = client.get('/wawawa')
    assert b'This is a wawawa application.' in result.data


def test_path_routing_not_found(client):
    result = client.get('/wuuuuui')
    assert b'Not Found' in result.data
    assert 404 == result.status_code
