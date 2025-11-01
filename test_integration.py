import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add_then_greet(client):
    add_resp = client.get('/add?a=5&b=6')
    assert add_resp.status_code == 200
    total = add_resp.get_json()['result']

    greet_resp = client.get(f'/greet/Result_{total}')
    assert greet_resp.status_code == 200
    assert f'Result_{total}' in greet_resp.get_json().get('message', '')
