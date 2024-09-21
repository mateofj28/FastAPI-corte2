"""
Este módulo define las rutas de la API para gestionar autores y libros en la base de datos.

Incluye las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para las entidades Autor y Libro,
y utiliza los servicios correspondientes para interactuar con la base de datos.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services import services
from app.database import get_db  # Función para obtener la sesión de la DB

router = APIRouter()


# Rutas para Autor
@router.get("/autores")
def get_all_autores(db: Session = Depends(get_db)):
    """
    Obtiene todos los autores registrados en la base de datos.

    Args:
        db (Session): Sesión de la base de datos proporcionada automáticamente.

    Returns:
        List[Autor]: Una lista con todos los autores existentes.
    """
    return services.get_autores(db)


@router.post("/autores")
def create_autor(nombre: str, nacionalidad: str, db: Session = Depends(get_db)):
    """
    Crea un nuevo autor en la base de datos.

    Args:
        nombre (str): Nombre del autor.
        nacionalidad (str): Nacionalidad del autor.
        db (Session): Sesión de la base de datos proporcionada automáticamente.

    Returns:
        Autor: El objeto Autor que ha sido creado.
    """
    return services.create_autor(db, nombre, nacionalidad)


@router.put("/autores/{autor_id}")
def update_autor(
    autor_id: int, nombre: str, nacionalidad: str, db: Session = Depends(get_db)
):
    """
    Actualiza un autor existente en la base de datos.

    Args:
        autor_id (int): ID del autor a actualizar.
        nombre (str): Nuevo nombre del autor.
        nacionalidad (str): Nueva nacionalidad del autor.
        db (Session): Sesión de la base de datos proporcionada automáticamente.

    Returns:
        Autor: El objeto Autor actualizado.
    """
    return services.update_autor(db, autor_id, nombre, nacionalidad)


@router.delete("/autores/{autor_id}")
def delete_autor(autor_id: int, db: Session = Depends(get_db)):
    """
    Elimina un autor de la base de datos por su ID.

    Args:
        autor_id (int): ID del autor a eliminar.
        db (Session): Sesión de la base de datos proporcionada automáticamente.

    Returns:
        Autor: El autor eliminado, o None si no se encontró.
    """
    return services.delete_autor(db, autor_id)


# Rutas para Libro
@router.get("/libros")
def get_all_libros(db: Session = Depends(get_db)):
    """
    Obtiene todos los libros registrados en la base de datos.

    Args:
        db (Session): Sesión de la base de datos proporcionada automáticamente.

    Returns:
        List[Libro]: Una lista con todos los libros existentes.
    """
    return services.get_libros(db)


@router.post("/libros")
def create_libro(
    titulo: str, autor_id: int, fecha_publicacion: str, db: Session = Depends(get_db)
):
    """
    Crea un nuevo libro en la base de datos.

    Args:
        titulo (str): Título del libro.
        autor_id (int): ID del autor relacionado con el libro.
        fecha_publicacion (str): Fecha de publicación del libro.
        db (Session): Sesión de la base de datos proporcionada automáticamente.

    Returns:
        Libro: El objeto Libro que ha sido creado.
    """
    return services.create_libro(db, titulo, autor_id, fecha_publicacion)


@router.put("/libros/{libro_id}")
def update_libro(
    libro_id: int,
    titulo: str,
    autor_id: int,
    fecha_publicacion: str,
    db: Session = Depends(get_db),
):
    """
    Actualiza un libro existente en la base de datos.

    Args:
        libro_id (int): ID del libro a actualizar.
        titulo (str): Nuevo título del libro.
        autor_id (int): ID del autor relacionado con el libro.
        fecha_publicacion (str): Nueva fecha de publicación del libro.
        db (Session): Sesión de la base de datos proporcionada automáticamente.

    Returns:
        Libro: El objeto Libro actualizado.
    """
    return services.update_libro(db, libro_id, titulo, autor_id, fecha_publicacion)


@router.delete("/libros/{libro_id}")
def delete_libro(libro_id: int, db: Session = Depends(get_db)):
    """
    Elimina un libro de la base de datos por su ID.

    Args:
        libro_id (int): ID del libro a eliminar.
        db (Session): Sesión de la base de datos proporcionada automáticamente.

    Returns:
        Libro: El libro eliminado, o None si no se encontró.
    """
    return services.delete_libro(db, libro_id)
