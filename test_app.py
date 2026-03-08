from app import app


def test_home_returns_200():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200


def test_health_returns_200():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200


def test_health_body():
    client = app.test_client()
    response = client.get('/health')
    assert response.data == b'Server is up and running'
