from pydantic import BaseModel
from datetime import date


class PersonaCreateSchema(BaseModel):
    cedula: int
    nombre: str
    edad: int
    fecha: date


class PersonaUpdateSchema(BaseModel):
    nombre: str
    edad: int
    fecha: date
