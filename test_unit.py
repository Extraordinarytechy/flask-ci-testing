import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    resp = client.get('/')
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, dict)
    assert data.get('message') == 'Flask API Running Successfully'

def test_add_numbers_success(client):
    resp = client.get('/add?a=3&b=7')
    assert resp.status_code == 200
    assert resp.get_json()['result'] == 10

def test_add_numbers_default_values(client):
    resp = client.get('/add')
    assert resp.status_code == 200
    assert resp.get_json()['result'] == 0

def test_add_invalid_input(client):
    resp = client.get('/add?a=x&b=7')
    assert resp.status_code == 400
    assert 'error' in resp.get_json()

def test_greet(client):
    resp = client.get('/greet/Ajay')
    assert resp.status_code == 200
    assert 'Ajay' in resp.get_json().get('message', '')
