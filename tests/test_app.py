# tests/test_calculadora.py
import pytest
from app.calculadora import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0

def test_restar():
    assert restar(5, 2) == 3
    assert restar(1, -1) == 2
    assert restar(0, 0) == 0

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 5) == -5
    assert multiplicar(0, 10) == 0

def test_dividir():
    assert dividir(10, 2) == 5.0
    assert dividir(5, -1) == -5.0
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)
Estas pruebas unitarias verifican que las funciones de la calculadora (sumar, restar, multiplicar, dividir) funcionen correctamente. Cada prueba verifica varios casos (números positivos, negativos, cero, división por cero).

Dentro de tests crea un archivo llamado test_app.py:

# tests/test_app.py
import pytest
from app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data  # Assuming the HTML template starts with <!DOCTYPE html>

def test_index_post_sumar(client):
    response = client.post('/', data={'num1': '2', 'num2': '3', 'operacion': 'sumar'})
    assert response.status_code == 200
    assert b'5.0' in response.data

def test_index_post_restar(client):
    response = client.post('/', data={'num1': '5', 'num2': '3', 'operacion': 'restar'})
    assert response.status_code == 200
    assert b'2.0' in response.data

def test_index_post_multiplicar(client):
    response = client.post('/', data={'num1': '2', 'num2': '3', 'operacion': 'multiplicar'})
    assert response.status_code == 200
    assert b'6.0' in response.data

def test_index_post_dividir(client):
    response = client.post('/', data={'num1': '6', 'num2': '3', 'operacion': 'dividir'})
    assert response.status_code == 200
    assert b'2.0' in response.data

def test_index_post_dividir_by_zero(client):
    response = client.post('/', data={'num1': '6', 'num2': '0', 'operacion': 'dividir'})
    assert response.status_code == 200
    assert b'Error: No se puede dividir por cero' in response.data

def test_index_post_invalid_operation(client):
    response = client.post('/', data={'num1': '6', 'num2': '3', 'operacion': 'invalid'})
    assert response.status_code == 200
    assert b'Operaci\xc3\xb3n no v\xc3\xa1lida' in response.data

def test_index_post_invalid_numbers(client):
    response = client.post('/', data={'num1': 'a', 'num2': 'b', 'operacion': 'sumar'})
    assert response.status_code == 200
    assert b'Error: Introduce n\xc3\xbameros v\xc3\xa1lidos' in response.data