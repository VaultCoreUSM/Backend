# app/crud/crud_reporte_generado.py

from sqlalchemy.orm import Session
from app.db.models.reportes import ReporteGenerado

from datetime import datetime
import json

def crear_reporte_generado(
    db: Session,
    nombre: str,
    periodo: str = None,
    tipo: str = "Automático",
    parametros: dict = None,
    generado: bool = False
):
    nuevo = ReporteGenerado(
        nombre=nombre,
        fecha_hora=datetime.utcnow(),
        periodo=periodo,
        tipo=tipo,
        generado=generado,
        parametros=json.dumps(parametros) if parametros else None
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_reportes_generados(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ReporteGenerado).order_by(ReporteGenerado.fecha_hora.desc()).offset(skip).limit(limit).all()

def obtener_reporte_generado_por_id(db: Session, id: int):
    return db.query(ReporteGenerado).filter(ReporteGenerado.id == id).first()

def marcar_como_generado(db: Session, id: int):
    reporte = db.query(ReporteGenerado).filter(ReporteGenerado.id == id).first()
    if reporte:
        reporte.generado = True
        db.commit()
        db.refresh(reporte)
    return reporte
