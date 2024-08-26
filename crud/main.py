from fastapi import FastAPI
from fastcrud import FastCRUD, crud_router
from db import get_session, engine
from models import Base, Persona
from schemas import PersonaCreateSchema, PersonaUpdateSchema


# Crear tablas antes de iniciar la app
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

# Crear el enrutador CRUD
persona_router = crud_router(
    session=get_session,
    model=Persona,
    create_schema=PersonaCreateSchema,
    update_schema=PersonaUpdateSchema,
    path="/personas",
    tags=["Personas"],
)

app.include_router(persona_router)
