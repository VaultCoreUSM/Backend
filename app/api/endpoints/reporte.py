# app/api/endpoints/reporte.py
from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException, status
from app.automatizacion.reporte import generar
from fastapi.responses import FileResponse

router = APIRouter()

@router.get("/generar_reporte",response_class=FileResponse)
def generar_reporte():
    validacion = generar()
    if not validacion[0]:
        raise HTTPException(status_code=500, detail=f"No se pudo generar el archivo.{validacion[1]}")
    return FileResponse(
        validacion[1],
        media_type="application/pdf",
        filename="reporte.pdf"
    )