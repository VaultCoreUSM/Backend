# backend/app/core/config.py
import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env si existe
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "VaultCore MVP"
    API_V1_STR: str = "/api/v1"

    # Configuración de la Base de Datos
    # Ejemplo: DATABASE_URL=postgresql://user:password@host:port/database_name
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@postgres:5432/vaultcore_db")

    # Podrías añadir más configuraciones aquí (claves API, etc.)

    class Config:
        case_sensitive = True
        # Si tienes un archivo .env, pydantic-settings puede leerlo directamente
        # env_file = ".env"

settings = Settings()
print("DEBUG: DATABASE_URL en uso por la aplicación:", settings.DATABASE_URL)