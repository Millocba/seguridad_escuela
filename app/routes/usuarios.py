# routes/usuarios.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app import schemas
from app.models import models
from app.utils.security import get_password_hash

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=schemas.usuario.Usuario)
def crear_usuario(usuario: schemas.usuario.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.email == usuario.email).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    hashed_pw = get_password_hash(usuario.password)
    nuevo_usuario = models.Usuario(
        nombre=usuario.nombre,
        apellido=usuario.apellido,
        email=usuario.email,
        telefono=usuario.telefono,
        rol=usuario.rol,
        aprobado=usuario.aprobado,
        escuela_id=usuario.escuela_id,
        hashed_password=hashed_pw,
    )
    print(f"Creando usuario: {nuevo_usuario.nombre} {nuevo_usuario.apellido} con rol {nuevo_usuario.rol}")
    db.add(nuevo_usuario)
    db.commit()
    print(F"Usuario agregado a la base de datos: {nuevo_usuario.nombre} {nuevo_usuario.apellido} con rol {nuevo_usuario.rol}")
    db.refresh(nuevo_usuario)
    return nuevo_usuario
