# db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde un archivo .env
load_dotenv()

# Obtiene la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("La variable de entorno DATABASE_URL no está configurada.")

# Determina si se deben usar connect_args (solo para SQLite)
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

# Crea el motor de la base de datos
engine = create_engine(DATABASE_URL, connect_args=connect_args)

# Configura la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declaración base para los modelos
Base = declarative_base()

# Función para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función para inicializar la base de datos y crear las tablas
def init_db():
    Base.metadata.create_all(bind=engine)

# Ejecuta la creación de tablas al cargar el módulo
init_db()
