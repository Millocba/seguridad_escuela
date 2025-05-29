import os

# Estructura de carpetas y archivos
estructura = {
    "app": [
        "__init__.py",
        "main.py",
        "db/__init__.py",
        "db/database.py",
        "db/models.py",
        "core/__init__.py",
        "core/config.py",
        "core/security.py",
        "schemas/__init__.py",
        "schemas/escuela.py",
        "schemas/usuario.py",
        "schemas/reporte.py",
        "routes/__init__.py",
        "routes/escuelas.py",
        "routes/usuarios.py",
        "routes/reportes.py",
        "routes/auth.py",
        "services/__init__.py",
        "services/escuela_service.py",
        "services/usuario_service.py",
        "services/reporte_service.py",
        "utils/__init__.py",
        "utils/geolocalizacion.py",
        "utils/media_handler.py"
    ],
    "alembic": [],
    "tests": [
        "__init__.py",
        "test_usuarios.py",
        "test_escuelas.py",
        "test_reportes.py"
    ],
    ".": [
        ".env",
        "requirements.txt",
        "README.md",
        "run.sh"
    ]
}

# Crear carpetas y archivos
for base, archivos in estructura.items():
    for archivo in archivos:
        ruta = os.path.join(base, archivo)
        carpeta = os.path.dirname(ruta)
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        with open(ruta, "w", encoding="utf-8") as f:
            if archivo.endswith(".py"):
                f.write("# " + archivo)
            elif archivo == "README.md":
                f.write("# SEGURIDAD_ESCUELAS\n\nProyecto FastAPI para gestión de incidentes en escuelas públicas.")
            elif archivo == "requirements.txt":
                f.write("fastapi\nuvicorn\nsqlalchemy\npydantic\npython-dotenv\nalembic\npasslib[bcrypt]\npyjwt\n")
            elif archivo == ".env":
                f.write("# Variables de entorno del proyecto")
            elif archivo == "run.sh":
                f.write("#!/bin/bash\nuvicorn app.main:app --reload")

print("✅ Estructura de proyecto creada correctamente.")
