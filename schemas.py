from pydantic import BaseModel
import datetime

class CreatePersonaSchema(BaseModel):
    cedula: int
    nombre: str
    fecha: datetime.datetime | None = None
    edad: int

        
class UpdatePersonaSchema(BaseModel):
    nombre: str | None = None
    fecha: datetime.datetime | None = None
    edad: int | None = None