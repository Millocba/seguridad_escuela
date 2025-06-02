# main.py
from fastapi import FastAPI
from app.routes import escuelas, usuarios, reportes, auth

app = FastAPI()

app.include_router(auth.router, prefix="/api", tags=["auth"])
app.include_router(escuelas.router, prefix="/api", tags=["escuelas"])
app.include_router(usuarios.router, prefix="/api", tags=["usuarios"])
app.include_router(reportes.router, prefix="/api", tags=["reportes"])