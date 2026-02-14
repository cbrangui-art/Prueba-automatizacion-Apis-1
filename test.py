import requests
import pytest

# URL BASE
BASE_URL = "https://jsonplaceholder.typicode.com"

# --- PRUEBA 1: OBTENER TODOS LOS POSTS ---
def test_obtener_todos_los_posts():
    url = f"{BASE_URL}/posts"
    response = requests.get(url)
    
    # 1. Validar Status 200
    assert response.status_code == 200, "Error: Status no es 200"
    
    # 2. VALIDACIÓN DE TIEMPO (< 2 segundos)
    tiempo = response.elapsed.total_seconds()
    assert tiempo < 2.0, f"Error: Muy lento ({tiempo}s)"
    
    data = response.json()
    
    # 3. Validar Array y Cantidad
    assert isinstance(data, list), "Error: No es una lista"
    assert len(data) >= 100, "Error: Menos de 100 posts"
    
    # 4. Validar Estructura (Tipos de datos)
    post = data[0]
    assert isinstance(post['userId'], int)
    assert isinstance(post['id'], int)
    assert isinstance(post['title'], str)
    assert isinstance(post['body'], str)

# --- PRUEBA 2: OBTENER UN POST ESPECÍFICO ---
def test_obtener_un_post_especifico():
    url = f"{BASE_URL}/posts/1"
    response = requests.get(url)
    
    # 1. Validar Status 200
    assert response.status_code == 200
    
    # 2. VALIDACIÓN DE TIEMPO (< 2 segundos)
    assert response.elapsed.total_seconds() < 2.0, "Error: Muy lento"
    
    data = response.json()
    
    # 3. Validar ID y Título
    assert data['id'] == 1, "Error: ID incorrecto"
    assert len(data['title']) > 0, "Error: Título vacío"

# --- PRUEBA 3: CREAR UN POST ---
def test_crear_un_post():
    url = f"{BASE_URL}/posts"
    payload = {
        "title": "Prueba Final",
        "body": "Validando tiempos de respuesta",
        "userId": 1
    }
    
    response = requests.post(url, json=payload)
    
    # 1. Validar Status 201
    assert response.status_code == 201, "Error: No se creó (201)"
    
    # 2. VALIDACIÓN DE TIEMPO (< 2 segundos)
    assert response.elapsed.total_seconds() < 2.0, "Error: Muy lento"
    
    data = response.json()
    
    # 3. Validar que tenga ID
    assert 'id' in data, "Error: No devolvió ID"