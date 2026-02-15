# Automatización de Pruebas API

Proyecto de automatización de pruebas para la API pública [JSONPlaceholder](https://jsonplaceholder.typicode.com/) usando Python y Pytest.

---

## Requisitos

| Herramienta | Versión |
|-------------|---------|
| Python | 3.14.2 |
| pytest | 7.4.4 |
| requests | 2.31.0 |
| pytest-html | 4.2.0 |

---

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/cbrangui-art/Prueba-automatizacion-Apis.git
cd Prueba-automatizacion-Apis
```

2. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

---

## Cómo ejecutar las pruebas

Ejecutar todos los tests:
```bash
python -m pytest test.py -v
```

Ejecutar y generar reporte HTML:
```bash
python -m pytest test.py -v --html=reporte.html --self-contained-html
```

---

## Pruebas incluidas

| # | Prueba | Validaciones |
|---|--------|-------------|
| 1 | Obtener todos los posts (`GET /posts`) | Status 200, respuesta es array, mínimo 100 elementos, estructura del objeto (userId, id, title, body) |
| 2 | Obtener un post específico (`GET /posts/1`) | Status 200, id correcto, título no vacío |
| 3 | Crear un post (`POST /posts`) | Status 201, respuesta contiene id |

---

## Estructura del proyecto

```
├── test.py              # Archivo con las pruebas automatizadas
├── conftest.py          # Configuración de pytest y del reporte
├── requirements.txt     # Dependencias del proyecto
├── .gitignore           # Archivos ignorados por Git
└── README.md            # Este archivo
```

---

## Versión del lenguaje

- **Lenguaje:** Python 3.14.2
- **Framework de testing:** Pytest 7.4.4
- **Librería HTTP:** Requests 2.31.0
