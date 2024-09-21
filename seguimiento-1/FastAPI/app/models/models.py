"""
Este módulo contiene los modelos de base de datos para la aplicación.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# pylint: disable=too-few-public-methods
class Autor(Base):
    """
    Modelo para la tabla de autores. Cada autor puede tener varios libros.
    """

    __tablename__ = "autores"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    nacionalidad = Column(String)

    libros = relationship("Libro", back_populates="autor")


# pylint: disable=too-few-public-methods
class Libro(Base):
    """
    Modelo para la tabla de libros. Cada libro está asociado con un autor.
    """

    __tablename__ = "libros"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    autor_id = Column(Integer, ForeignKey("autores.id"))
    fecha_publicacion = Column(Date)

    autor = relationship("Autor", back_populates="libros")
