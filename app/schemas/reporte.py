# schemas/reporte.py
from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime

class TipoIncidenteEnum(str, Enum):
    ROBO = "robo"
    DISTURBIO = "disturbio"
    DAÑO = "daño"
    OTRO = "otro"

class ReporteBase(BaseModel):
    escuela_id: int
    usuario_id: int
    tipo_incidente: TipoIncidenteEnum
    descripcion: str
    imagen_url: Optional[str] = None

class ReporteCreate(ReporteBase):
    pass

class ReporteUpdate(ReporteBase):
    pass

class Reporte(ReporteBase):
    id: int
    fecha: datetime

    class Config:
        from_attributes = True
