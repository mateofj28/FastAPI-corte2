"""
Este módulo proporciona servicios para realizar operaciones CRUD 
(Crear, Leer, Actualizar, Eliminar) en las entidades Autor y Libro 
utilizando SQLAlchemy y una sesión de base de datos.

Funciones para Autor:
- get_autores: Obtiene todos los autores de la base de datos.
- create_autor: Crea un nuevo autor.
- update_autor: Actualiza un autor existente.
- delete_autor: Elimina un autor.

Funciones para Libro:
- get_libros: Obtiene todos los libros de la base de datos.
- create_libro: Crea un nuevo libro.
- update_libro: Actualiza un libro existente.
- delete_libro: Elimina un libro.
"""

from sqlalchemy.orm import Session
from app.models.models.py import Autor, Libro


# Servicios para Autor
def get_autores(db: Session):
    """
    Obtiene todos los autores de la base de datos.

    Args:
        db (Session): Sesión de la base de datos.

    Returns:
        List[Autor]: Lista de todos los autores existentes en la base de datos.
    """
    return db.query(Autor).all()


def create_autor(db: Session, nombre: str, nacionalidad: str):
    """
    Crea un nuevo autor en la base de datos.

    Args:
        db (Session): Sesión de la base de datos.
        nombre (str): Nombre del autor.
        nacionalidad (str): Nacionalidad del autor.

    Returns:
        Autor: El autor que ha sido creado en la base de datos.
    """
    nuevo_autor = Autor(nombre=nombre, nacionalidad=nacionalidad)
    db.add(nuevo_autor)
    db.commit()
    db.refresh(nuevo_autor)
    return nuevo_autor


def update_autor(db: Session, autor_id: int, nombre: str, nacionalidad: str):
    """
    Actualiza un autor existente en la base de datos.

    Args:
        db (Session): Sesión de la base de datos.
        autor_id (int): ID del autor a actualizar.
        nombre (str): Nuevo nombre del autor.
        nacionalidad (str): Nueva nacionalidad del autor.

    Returns:
        Autor: El autor actualizado o None si no se encontró.
    """
    autor = db.query(Autor).filter(Autor.id == autor_id).first()
    if autor:
        autor.nombre = nombre
        autor.nacionalidad = nacionalidad
        db.commit()
        db.refresh(autor)
    return autor


def delete_autor(db: Session, autor_id: int):
    """
    Elimina un autor de la base de datos.

    Args:
        db (Session): Sesión de la base de datos.
        autor_id (int): ID del autor a eliminar.

    Returns:
        Autor: El autor eliminado o None si no se encontró.
    """
    autor = db.query(Autor).filter(Autor.id == autor_id).first()
    if autor:
        db.delete(autor)
        db.commit()
    return autor


# Servicios para Libro
def get_libros(db: Session):
    """
    Obtiene todos los libros de la base de datos.

    Args:
        db (Session): Sesión de la base de datos.

    Returns:
        List[Libro]: Lista de todos los libros existentes en la base de datos.
    """
    return db.query(Libro).all()


def create_libro(db: Session, titulo: str, autor_id: int, fecha_publicacion: str):
    """
    Crea un nuevo libro en la base de datos.

    Args:
        db (Session): Sesión de la base de datos.
        titulo (str): Título del libro.
        autor_id (int): ID del autor relacionado con el libro.
        fecha_publicacion (str): Fecha de publicación del libro.

    Returns:
        Libro: El libro creado en la base de datos.
    """
    nuevo_libro = Libro(
        titulo=titulo,
        autor_id=autor_id,
        fecha_publicacion=fecha_publicacion
    )
    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)
    return nuevo_libro


def update_libro(db: Session, libro_id: int, titulo: str, autor_id: int, fecha_publicacion: str):
    """
    Actualiza un libro existente en la base de datos.

    Args:
        db (Session): Sesión de la base de datos.
        libro_id (int): ID del libro a actualizar.
        titulo (str): Nuevo título del libro.
        autor_id (int): Nuevo ID del autor relacionado con el libro.
        fecha_publicacion (str): Nueva fecha de publicación del libro.

    Returns:
        Libro: El libro actualizado o None si no se encontró.
    """
    libro = db.query(Libro).filter(Libro.id == libro_id).first()
    if libro:
        libro.titulo = titulo
        libro.autor_id = autor_id
        libro.fecha_publicacion = fecha_publicacion
        db.commit()
        db.refresh(libro)
    return libro


def delete_libro(db: Session, libro_id: int):
    """
    Elimina un libro de la base de datos.

    Args:
        db (Session): Sesión de la base de datos.
        libro_id (int): ID del libro a eliminar.

    Returns:
        Libro: El libro eliminado o None si no se encontró.
    """
    libro = db.query(Libro).filter(Libro.id == libro_id).first()
    if libro:
        db.delete(libro)
        db.commit()
    return libro
