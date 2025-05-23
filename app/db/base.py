# backend/app/db/base.py
from sqlalchemy.orm import declarative_base

# Base para que todos los modelos la hereden
Base = declarative_base()