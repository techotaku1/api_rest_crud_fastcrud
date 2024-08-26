from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Persona(Base):
        __tablename__ = "personas"
        cedula = Column(Integer, primary_key=True, index=True)
        nombre = Column(String, nullable=False)
        fecha = Column(DateTime, default=func.now())
        edad = Column(Integer, nullable=False)