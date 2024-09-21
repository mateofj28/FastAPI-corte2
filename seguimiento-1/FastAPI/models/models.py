from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Autor(Base):
    __tablename__ = "autores"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    nacionalidad = Column(String)

    libros = relationship("Libro", back_populates="autor")


class Libro(Base):
    __tablename__ = "libros"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    autor_id = Column(Integer, ForeignKey("autores.id"))
    fecha_publicacion = Column(Date)

    autor = relationship("Autor", back_populates="libros")
