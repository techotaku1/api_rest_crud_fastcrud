from typing import AsyncGenerator
from fastapi import FastAPI
from fastcrud import crud_router
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Persona
from schemas import CreatePersonaSchema, UpdatePersonaSchema

# Configuración de la base de datos
DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Dependencia para la sesión de la base de datos
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
            yield session

            # Crear tablas antes de iniciar la app
async def lifespan(app: FastAPI):
                async with engine.begin() as conn:
                        await conn.run_sync(Base.metadata.create_all)
                        yield

                            # Configuración de la aplicación FastAPI
app = FastAPI(lifespan=lifespan)

                            # CRUD router
persona_router = crud_router(
                                session=get_session,
                                    model=Persona,
                                        create_schema=CreatePersonaSchema,
                                            update_schema=UpdatePersonaSchema,
                                                path="/personas",
                                                    tags=["Personas"],
                                                    )

app.include_router(persona_router)