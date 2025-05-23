# backend/app/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Crear el motor de SQLAlchemy
# El argumento connect_args es específico para SQLite, puedes quitarlo para PostgreSQL
# engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False}) # Para SQLite
engine = create_engine(settings.DATABASE_URL)


# Crear una clase SessionLocal que se utilizará para crear sesiones de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función de dependencia para obtener una sesión de base de datos en los endpoints de la API
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()