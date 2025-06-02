# app/models/alarma.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from .base import Base

class Alarma(Base):
    __tablename__ = "alarmas"

    id = Column(Integer, primary_key=True, index=True)
    escuela_id = Column(Integer, ForeignKey("escuelas.id"))
    empresa = Column(String, nullable=False)
    telefono_empresa = Column(String, nullable=True)
    es_monitoreada = Column(Boolean, default=False)
    es_sonora = Column(Boolean, default=False)
    observaciones = Column(Text, nullable=True)

    escuela = relationship("Escuela", back_populates="alarmas")