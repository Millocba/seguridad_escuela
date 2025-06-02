from pydantic import BaseModel
from typing import Optional

class AlarmaBase(BaseModel):
    escuela_id: int
    empresa: str
    telefono_empresa: Optional[str] = None
    es_monitoreada: bool = False
    es_sonora: bool = False
    observaciones: Optional[str] = None

class AlarmaCreate(AlarmaBase):
    pass

class AlarmaUpdate(AlarmaBase):
    pass

class Alarma(AlarmaBase):
    id: int

    class Config:
        from_attributes = True
