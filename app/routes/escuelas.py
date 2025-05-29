# routes/escuelas.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app import models, schemas

router = APIRouter(prefix="/escuelas", tags=["Escuelas"])

@router.post("/", response_model=schemas.escuela.Escuela)
def crear_escuela(escuela: schemas.escuela.EscuelaCreate, db: Session = Depends(get_db)):
    db_escuela = models.escuela.Escuela(**escuela.dict())
    db.add(db_escuela)
    db.commit()
    db.refresh(db_escuela)
    return db_escuela

@router.get("/", response_model=list[schemas.escuela.Escuela])
def listar_escuelas(db: Session = Depends(get_db)):
    return db.query(models.escuela.Escuela).all()
