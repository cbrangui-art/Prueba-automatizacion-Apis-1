import pytest

def pytest_html_report_title(report):
    report.title = "Reporte de Pruebas API"

def pytest_html_duration_format(duration):
    return f"{duration:.3f}s"

def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata.clear()

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    if hasattr(session.config, "_metadata"):
        session.config._metadata.clear()
