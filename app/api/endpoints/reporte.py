# app/api/endpoints/reporte.py
from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException, status
from app.automatizacion.reporte import generar

router = APIRouter()

@router.get("/generar_reporte")
def generar_reporte():
    validacion = generar()
    if not validacion[0]:
        raise HTTPException(status_code=500, detail=f"No se pudo generar el archivo.{validacion[1]}")
    return {"mensaje": "Reporte generado exitosamente"}