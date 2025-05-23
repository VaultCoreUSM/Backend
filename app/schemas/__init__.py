# backend/app/schemas/__init__.py

from .camera import CameraBase, CameraCreate, CameraUpdate, CameraInDBBase, Camera

# Cuando crees los esquemas para Eventos, los añadirás aquí también, por ejemplo:
# from .event import EventBase, EventCreate, EventUpdate, EventInDBBase, Event

# Puedes añadir cualquier otra clase de esquema que quieras que esté disponible
# directamente bajo el módulo 'schemas'