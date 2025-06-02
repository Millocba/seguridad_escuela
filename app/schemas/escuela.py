# schemas/escuela.py
from pydantic import BaseModel
from typing import Optional

class EscuelaBase(BaseModel):
    nombre: str
    direccion: str
    latitud: Optional[float] = None
    longitud: Optional[float] = None
    telefono: Optional[str] = None
    directora_nombre: Optional[str] = None
    directora_dni: Optional[str] = None
    tiene_domos: bool = False
    adicional_policial: bool = False
    seguridad_privada: bool = False

class EscuelaCreate(EscuelaBase):
    pass

class EscuelaUpdate(EscuelaBase):
    pass

class Escuela(EscuelaBase):
    id: int

    class Config:
        from_attributes = True
