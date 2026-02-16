import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import pytest

# URL BASE
BASE_URL = "https://jsonplaceholder.typicode.com"

# Sesión reutilizable con reintentos automáticos
session = requests.Session()
retries = Retry(total=3, backoff_factor=0.5)
session.mount("https://", HTTPAdapter(max_retries=retries))

# Warmup: precalentar conexión TCP+TLS antes de las pruebas
@pytest.fixture(autouse=True, scope="session")
def warmup():
    session.get(f"{BASE_URL}/posts/1")

# --- PRUEBA 1: OBTENER TODOS LOS POSTS ---
def test_obtener_todos_los_posts():
    url = f"{BASE_URL}/posts"
    response = session.get(url)
    
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
    response = session.get(url)
    
    # 1. Validar Status 200
    assert response.status_code == 200
    
    # 2. VALIDACIÓN DE TIEMPO (< 2 segundos)
    tiempo = response.elapsed.total_seconds()
    assert tiempo < 2.0, "Error: Muy lento"
    
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
    
    response = session.post(url, json=payload)
    
    # 1. Validar Status 201
    assert response.status_code == 201, "Error: No se creó (201)"
    
    # 2. VALIDACIÓN DE TIEMPO (< 2 segundos)
    tiempo = response.elapsed.total_seconds()
    assert tiempo < 2.0, "Error: Muy lento"
    
    data = response.json()
    
    # 3. Validar que tenga ID
    assert 'id' in data, "Error: No devolvió ID"

    #####################################
# --- PRUEBA 4: VALIDAR POST INEXISTENTE ---
def test_validar_post_inexistente():
    # 1. Buscamos un post que NO existe
    url = f"{BASE_URL}/posts/999999"
    
    # 2. Hacemos la petición
    response = session.get(url)
    
    # 3. Debe devolver 404 
    assert response.status_code == 404, "Error: Se esperaba status 404 (Not Found)"
    
    # 4. Validar que la respuesta esté vacía (no encontró el post)
    data = response.json()
    assert data == {}, "Error: La respuesta debería estar vacía"