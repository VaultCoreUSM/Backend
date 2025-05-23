# backend/app/crud/crud_camera.py
from sqlalchemy.orm import Session
from app.db.models.camera import Camera as CameraModel
from app.schemas.camera import CameraCreate, CameraUpdate

def get_camera(db: Session, camera_id: int):
    return db.query(CameraModel).filter(CameraModel.id == camera_id).first()

def get_camera_by_stream_url(db: Session, stream_url: str):
    return db.query(CameraModel).filter(CameraModel.stream_url == stream_url).first()

def get_cameras(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CameraModel).offset(skip).limit(limit).all()

def create_camera(db: Session, camera: CameraCreate):
    db_camera = CameraModel(
        name=camera.name,
        stream_url=str(camera.stream_url), # Convertir HttpUrl a string para guardar
        is_active=camera.is_active
    )
    db.add(db_camera)
    db.commit()
    db.refresh(db_camera)
    return db_camera

def update_camera(db: Session, db_camera: CameraModel, camera_in: CameraUpdate):
    update_data = camera_in.model_dump(exclude_unset=True) # Usar model_dump para Pydantic v2+
    for key, value in update_data.items():
        if value is not None: # Solo actualizar campos que vienen en la petición
             if key == "stream_url" and value is not None:
                setattr(db_camera, key, str(value)) # Convertir HttpUrl a string
             else:
                setattr(db_camera, key, value)
    db.add(db_camera)
    db.commit()
    db.refresh(db_camera)
    return db_camera

def delete_camera(db: Session, camera_id: int):
    db_camera = db.query(CameraModel).filter(CameraModel.id == camera_id).first()
    if db_camera:
        db.delete(db_camera)
        db.commit()
    return db_camera