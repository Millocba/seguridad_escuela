# schemas/usuario.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

class RolEnum(str, Enum):
    DIRECTIVO = "DIRECTIVO"
    AUDITOR = "AUDITOR"
    ADMIN = "ADMIN"

class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    telefono: Optional[str]
    rol: RolEnum
    is_active: bool
    aprobado: bool
    escuela_id: Optional[int]

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioUpdate(UsuarioBase):
    password: Optional[str] = None

class Usuario(UsuarioBase):
    id: int
    class Config:
        from_attributes = True
        use_enum_values = True