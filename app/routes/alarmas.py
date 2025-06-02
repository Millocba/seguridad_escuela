# routes/alarmas.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app import schemas
from app.models import models

router = APIRouter(prefix="/alarmas", tags=["Alarmas"])
@router.post("/", response_model=schemas.Alarma)
def crear_alarma(alarma: schemas.alarma.AlarmaCreate, db: Session = Depends(get_db)):
    db_alarma = models.Alarma(**alarma.dict())
    db.add(db_alarma)
    db.commit()
    db.refresh(db_alarma)
    return db_alarma
@router.get("/", response_model=list[schemas.alarma.Alarma])
def listar_alarmas(db: Session = Depends(get_db)):
    return db.query(models.Alarma).all()
@router.get("/{id}", response_model=schemas.Alarma)
def obtener_alarma(id: int, db: Session = Depends(get_db)):
    db_alarma = db.query(models.Alarma).filter(models.Alarma.id == id).first()
    if not db_alarma:
        raise HTTPException(status_code=404, detail="Alarma no encontrada")
    return db_alarma
