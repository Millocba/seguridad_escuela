from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Asegurarse de que el entorno tenga soporte para SSL
try:
    import ssl
except ModuleNotFoundError:
    raise EnvironmentError(
        "El módulo 'ssl' no está disponible en el entorno actual. "
        "Asegúrate de que tu instalación de Python tenga soporte para SSL."
    )

# Importaciones de rutas y base de datos
try:
    from app.db.database import engine, Base
    from app.routes import escuelas, usuarios, reportes
except ModuleNotFoundError as e:
    raise ImportError(
        "Módulos necesarios no encontrados. Verifica que los directorios 'app/db' y 'app/routes' existen "
        "y que todos los módulos están instalados correctamente."
    ) from e

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Registrar routers
app.include_router(escuelas.router, prefix="/api/escuelas", tags=["Escuelas"])
app.include_router(usuarios.router, prefix="/api/usuarios", tags=["Usuarios"])
app.include_router(reportes.router, prefix="/api/reportes", tags=["Reportes"])

# Ruta principal
@app.get("/")
def read_root():
    return {"message": "API Seguridad Escuelas funcionando"}
