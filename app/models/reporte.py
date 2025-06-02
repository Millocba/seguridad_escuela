# app/models/reporte.py
from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime, Enum, String
from sqlalchemy.orm import relationship
import datetime
import enum
from .base import Base

class TipoIncidenteEnum(enum.Enum):
    ROBO = "robo"
    DISTURBIO = "disturbio"
    DAÑO = "daño"
    OTRO = "otro"

class Reporte(Base):
    __tablename__ = "reportes"

    id = Column(Integer, primary_key=True, index=True)
    escuela_id = Column(Integer, ForeignKey("escuelas.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tipo_incidente = Column(Enum(TipoIncidenteEnum), nullable=False)
    descripcion = Column(Text, nullable=False)
    fecha = Column(DateTime, default=datetime.datetime.utcnow)
    imagen_url = Column(String, nullable=True)

    escuela = relationship("Escuela", back_populates="reportes")
    usuario = relationship("Usuario", back_populates="reportes")