from pydantic import BaseModel
from datetime import datetime

class ReporteProgramadoBase(BaseModel):
    nombre: str
    fecha_proxima: datetime
    frecuencia: str

class ReporteProgramadoCreate(ReporteProgramadoBase):
    pass

class ReporteProgramadoOut(ReporteProgramadoBase):
    id: int
    activo: bool

    class Config:
        orm_mode = True
