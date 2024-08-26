from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Persona(Base):
    __tablename__ = "personas"
    cedula = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    edad = Column(Integer)
    fecha = Column(Date)
