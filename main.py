from fastapi import FastAPI
from app.routes import escuelas, usuarios, reportes

app = FastAPI()

app.include_router(escuelas.router)
app.include_router(usuarios.router)
app.include_router(reportes.router)
