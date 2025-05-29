# SEGURIDAD_ESCUELAS

Proyecto FastAPI para gestión de incidentes en escuelas públicas.

# SEGURIDAD ESCUELAS

Aplicación web para registrar escuelas públicas, reportes de incidentes, métricas y gestión de seguridad institucional en Córdoba.

## Características

- Registro y administración de escuelas públicas.
- Gestión de usuarios con distintos roles.
- Reporte de incidentes.
- Seguridad y autenticación (con posibilidad de 2FA).
- Estructura modular y escalable con FastAPI.

## Requisitos

- Python 3.10+
- MySQL
- pip

## Instalación

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
