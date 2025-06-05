# app/db/models/reportes.py

from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from datetime import datetime
from app.db.base import Base

class ReporteGenerado(Base):
    __tablename__ = "reportes_generados"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    fecha_hora = Column(DateTime, default=datetime.utcnow)
    periodo = Column(String, nullable=True)  # mensual, semanal, etc.
    parametros = Column(Text, nullable=True)  # JSON serializado
    tipo = Column(String, nullable=False, default="Automático")  # Manual o Automático
    generado = Column(Boolean, nullable=False, default=False)


class ReporteProgramado(Base):
    __tablename__ = "reportes_programados"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    fecha_proxima = Column(DateTime, nullable=False)
    frecuencia = Column(String, nullable=False)  # mensual, semanal, diario
    activo = Column(Boolean, default=True)
