# app/models/escuela.py
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class Escuela(Base):
    __tablename__ = "escuelas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    latitud = Column(Float, nullable=True)
    longitud = Column(Float, nullable=True)
    telefono = Column(String, nullable=True)
    directora_nombre = Column(String, nullable=True)
    directora_dni = Column(String, nullable=True)
    tiene_domos = Column(Boolean, default=False)
    adicional_policial = Column(Boolean, default=False)
    seguridad_privada = Column(Boolean, default=False)

    usuarios = relationship("Usuario", back_populates="escuela")
    alarmas = relationship("Alarma", back_populates="escuela")
    reportes = relationship("Reporte", back_populates="escuela")