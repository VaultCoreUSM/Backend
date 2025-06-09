# app/crud/crud_reporte_programado.py

from sqlalchemy.orm import Session
from app.db.models.reportes import ReporteProgramado
from datetime import datetime

def crear_reporte_programado(
    db: Session,
    nombre: str,
    fecha_proxima: datetime,
    frecuencia: str,
    activo: bool = True
):
    nuevo = ReporteProgramado(
        nombre=nombre,
        fecha_proxima=fecha_proxima,
        frecuencia=frecuencia,
        activo=activo
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_reportes_programados(db: Session, solo_activos: bool = False):
    query = db.query(ReporteProgramado)
    if solo_activos:
        query = query.filter(ReporteProgramado.activo == True)
    return query.order_by(ReporteProgramado.fecha_proxima.asc()).all()

def obtener_programado_por_id(db: Session, id: int):
    return db.query(ReporteProgramado).filter(ReporteProgramado.id == id).first()

def actualizar_fecha_proxima(db: Session, reporte: ReporteProgramado, nueva_fecha: datetime):
    reporte.fecha_proxima = nueva_fecha
    db.commit()
    db.refresh(reporte)
    return reporte

def desactivar_reporte_programado(db: Session, id: int):
    reporte = obtener_programado_por_id(db, id)
    if reporte:
        reporte.activo = False
        db.commit()
        db.refresh(reporte)
    return reporte
