# backend/app/schemas/camera.py
from pydantic import BaseModel, HttpUrl # HttpUrl para validar URLs
from typing import Optional
from datetime import datetime

# Propiedades base compartidas
class CameraBase(BaseModel):
    name: str
    stream_url: HttpUrl # FastAPI usará esto para validar que es una URL válida
    is_active: Optional[bool] = True

# Propiedades a recibir en la creación
class CameraCreate(CameraBase):
    pass

# Propiedades a recibir en la actualización
class CameraUpdate(CameraBase):
    name: Optional[str] = None
    stream_url: Optional[HttpUrl] = None
    is_active: Optional[bool] = None

# Propiedades almacenadas en la BD (incluye id y timestamps)
class CameraInDBBase(CameraBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True #  Permite a Pydantic leer datos de atributos de objetos (modelos ORM)

# Propiedades a devolver al cliente (puede ser igual a CameraInDBBase o diferente)
class Camera(CameraInDBBase):
    pass