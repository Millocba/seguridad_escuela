# routes/usuarios.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app import models, schemas
from app.utils.security import get_password_hash

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=schemas.usuario.Usuario)
def crear_usuario(usuario: schemas.usuario.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = db.query(models.usuario.Usuario).filter(models.usuario.Usuario.email == usuario.email).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    hashed_pw = get_password_hash(usuario.password)
    nuevo_usuario = models.usuario.Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        hashed_password=hashed_pw,
        rol=usuario.rol,
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario
