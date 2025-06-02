# app/models/usuario.py
from sqlalchemy import Column, Integer, String, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
import enum

class RolEnum(str,enum.Enum):
    DIRECTIVO = "DIRECTIVO"
    AUDITOR = "AUDITOR"
    ADMIN = "ADMIN"

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefono = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    rol = Column(Enum(RolEnum), default=RolEnum.DIRECTIVO)
    is_active = Column(Boolean, default=True)
    aprobado = Column(Boolean, default=False)
    escuela_id = Column(Integer, ForeignKey("escuelas.id"), nullable=True)

    escuela = relationship("Escuela", back_populates="usuarios")
    reportes = relationship("Reporte", back_populates="usuario")
