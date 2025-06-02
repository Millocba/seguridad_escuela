# routes/reportes.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app import schemas
from app.models import models


router = APIRouter(prefix="/reportes", tags=["Reportes"])

@router.post("/", response_model=schemas.reporte.Reporte)
def crear_reporte(reporte: schemas.reporte.ReporteCreate, db: Session = Depends(get_db)):
    db_reporte = models.Reporte(**reporte.dict())
    db.add(db_reporte)
    db.commit()
    db.refresh(db_reporte)
    return db_reporte

@router.get("/", response_model=list[schemas.reporte.Reporte])
def listar_reportes(db: Session = Depends(get_db)):
    return db.query(models.Reporte).all()
