from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services import services
from app.models.models import Autor, Libro
from app.database import get_db  # Función para obtener la sesión de la DB

router = APIRouter()

# Rutas para Autor
@router.get("/autores")
def get_all_autores(db: Session = Depends(get_db)):
    return services.get_autores(db)

@router.post("/autores")
def create_autor(nombre: str, nacionalidad: str, db: Session = Depends(get_db)):
    return services.create_autor(db, nombre, nacionalidad)

@router.put("/autores/{autor_id}")
def update_autor(autor_id: int, nombre: str, nacionalidad: str, db: Session = Depends(get_db)):
    return services.update_autor(db, autor_id, nombre, nacionalidad)

@router.delete("/autores/{autor_id}")
def delete_autor(autor_id: int, db: Session = Depends(get_db)):
    return services.delete_autor(db, autor_id)

# Rutas para Libro
@router.get("/libros")
def get_all_libros(db: Session = Depends(get_db)):
    return services.get_libros(db)

@router.post("/libros")
def create_libro(titulo: str, autor_id: int, fecha_publicacion: str, db: Session = Depends(get_db)):
    return services.create_libro(db, titulo, autor_id, fecha_publicacion)

@router.put("/libros/{libro_id}")
def update_libro(libro_id: int, titulo: str, autor_id: int, fecha_publicacion: str, db: Session = Depends(get_db)):
    return services.update_libro(db, libro_id, titulo, autor_id, fecha_publicacion)

@router.delete("/libros/{libro_id}")
def delete_libro(libro_id: int, db: Session = Depends(get_db)):
    return services.delete_libro(db, libro_id)
