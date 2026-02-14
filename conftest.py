import pytest

def pytest_html_report_title(report):
    """Cambia el título del reporte"""
    report.title = "Reporte de Pruebas API"

def pytest_configure(config):
    """Elimina los metadatos para quitar la sección Environment"""
    if hasattr(config, "_metadata"):
        config._metadata.clear()

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """Limpia metadata al finalizar la sesión para que no aparezca Environment"""
    if hasattr(session.config, "_metadata"):
        session.config._metadata.clear()
