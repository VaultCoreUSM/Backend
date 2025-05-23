# backend/app/api/endpoints/cameras.py
from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app import schemas
from app.db.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Camera, status_code=status.HTTP_201_CREATED)
def create_new_camera(
    *,
    db: Session = Depends(get_db),
    camera_in: schemas.CameraCreate,
) -> Any:
    """
    Create new camera.
    """
    camera = crud.crud_camera.get_camera_by_stream_url(db, stream_url=str(camera_in.stream_url))
    if camera:
        raise HTTPException(
            status_code=400,
            detail="A camera with this stream URL already exists.",
        )
    new_camera = crud.crud_camera.create_camera(db=db, camera=camera_in)
    return new_camera

@router.get("/", response_model=List[schemas.Camera])
def read_cameras(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve cameras.
    """
    cameras = crud.crud_camera.get_cameras(db, skip=skip, limit=limit)
    return cameras

@router.get("/{camera_id}", response_model=schemas.Camera)
def read_camera_by_id(
    camera_id: int,
    db: Session = Depends(get_db),
) -> Any:
    """
    Get a specific camera by id.
    """
    camera = crud.crud_camera.get_camera(db, camera_id=camera_id)
    if not camera:
        raise HTTPException(status_code=404, detail="Camera not found")
    return camera

@router.put("/{camera_id}", response_model=schemas.Camera)
def update_existing_camera(
    *,
    db: Session = Depends(get_db),
    camera_id: int,
    camera_in: schemas.CameraUpdate,
) -> Any:
    """
    Update a camera.
    """
    db_camera = crud.crud_camera.get_camera(db, camera_id=camera_id)
    if not db_camera:
        raise HTTPException(status_code=404, detail="Camera not found")
    
    # Verificar si la nueva URL de stream ya existe en otra cámara (si se está actualizando)
    if camera_in.stream_url:
        existing_camera_with_url = crud.crud_camera.get_camera_by_stream_url(db, stream_url=str(camera_in.stream_url))
        if existing_camera_with_url and existing_camera_with_url.id != camera_id:
            raise HTTPException(status_code=400, detail="Another camera with this stream URL already exists.")

    updated_camera = crud.crud_camera.update_camera(db=db, db_camera=db_camera, camera_in=camera_in)
    return updated_camera

@router.delete("/{camera_id}", response_model=schemas.Camera)
def delete_existing_camera(
    *,
    db: Session = Depends(get_db),
    camera_id: int,
) -> Any:
    """
    Delete a camera.
    """
    camera = crud.crud_camera.get_camera(db, camera_id=camera_id)
    if not camera:
        raise HTTPException(status_code=404, detail="Camera not found")
    deleted_camera = crud.crud_camera.delete_camera(db=db, camera_id=camera_id)
    return deleted_camera