# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Para permitir peticiones desde el frontend

from app.core.config import settings
from app.api.api_v1 import api_router
from app.db.base import Base # Importar Base
from app.db.database import engine # Importar engine

# --- Creación de Tablas (Opcional, solo para desarrollo/primera ejecución) ---
# En un entorno de producción, usualmente usarías Alembic para migraciones.
# Descomenta las siguientes líneas si quieres que FastAPI cree las tablas
# al iniciar (si no existen). Asegúrate de que los modelos estén importados
# para que Base los conozca.
from app.db.models import camera # Importa tus modelos aquí
Base.metadata.create_all(bind=engine)
# --- Fin Creación de Tablas ---


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Configuración de CORS (Cross-Origin Resource Sharing)
# Ajusta origins según tus necesidades. "*" es permisivo para desarrollo.
origins = [
    "http://localhost",
    "http://localhost:3000", # Si tu frontend React corre en el puerto 3000
    # Añade aquí los dominios de tu frontend en producción
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Permite todos los métodos (GET, POST, PUT, etc.)
    allow_headers=["*"], # Permite todas las cabeceras
)

# Incluir el router de la API v1
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/generar_reporte")
def generar_reporte():
    ruta = generar()
    return {"mensaje": "Reporte generado exitosamente", "archivo": ruta}



@app.get("/", tags=["Root"])
async def read_root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}!"}

# Aquí podrías añadir lógica para iniciar los servicios de procesamiento de video
# al arrancar la aplicación si es necesario. Por ejemplo:
# from app.services import video_processing
# @app.on_event("startup")
# async def startup_event():
#     asyncio.create_task(video_processing.start_camera_monitoring())
