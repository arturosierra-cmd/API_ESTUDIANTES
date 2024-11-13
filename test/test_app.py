import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_crear_estudiante(client):
    response = client.post('/estudiantes', json={'nombre': 'Juan', 'edad': 20})
    assert response.status_code == 201
    assert response.json['nombre'] == 'Juan'

def test_listar_estudiantes(client):
    response = client.get('/estudiantes')
    assert response.status_code == 200
    assert isinstance(response.json, list)
