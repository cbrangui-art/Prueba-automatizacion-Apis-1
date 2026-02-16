import pytest
import json

def pytest_html_report_title(report):
    report.title = "Reporte de Pruebas API"

def pytest_html_duration_format(duration):
    return f"{duration:.3f}s"

# Captura automática de respuestas HTTP para el reporte
_ultima_respuesta = None

def _patch_session():
    """Intercepta las peticiones HTTP para capturar la última respuesta"""
    from test import session
    _original_request = session.request

    def _request_wrapper(*args, **kwargs):
        global _ultima_respuesta
        response = _original_request(*args, **kwargs)
        _ultima_respuesta = response
        return response

    session.request = _request_wrapper

_patch_session()

@pytest.fixture(autouse=True)
def imprimir_resumen_automatico():
    """Imprime automáticamente el resumen de la respuesta HTTP al final de cada test"""
    global _ultima_respuesta
    _ultima_respuesta = None
    yield
    if _ultima_respuesta is not None:
        r = _ultima_respuesta
        tiempo = r.elapsed.total_seconds()
        print(f"\n✅ Status: {r.status_code}")
        print(f"⏱️ Tiempo de respuesta: {tiempo:.3f}s")
        try:
            data = r.json()
            if isinstance(data, list):
                print(f"📦 Elementos: {len(data)}")
            elif isinstance(data, dict) and data:
                for key, value in data.items():
                    texto = str(value)
                    print(f"   {key}: {texto[:80]}{'...' if len(texto) > 80 else ''}")
            else:
                print(f"📝 Respuesta: {data}")
        except Exception:
            pass

def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata.clear()

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    if hasattr(session.config, "_metadata"):
        session.config._metadata.clear()
