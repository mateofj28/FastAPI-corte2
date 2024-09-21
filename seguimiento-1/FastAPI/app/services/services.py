from sqlalchemy.orm import Session
from app.models.models import Autor, Libro

# Servicios para Autor
def get_autores(db: Session):
    return db.query(Autor).all()

def create_autor(db: Session, nombre: str, nacionalidad: str):
    nuevo_autor = Autor(nombre=nombre, nacionalidad=nacionalidad)
    db.add(nuevo_autor)
    db.commit()
    db.refresh(nuevo_autor)
    return nuevo_autor

def update_autor(db: Session, autor_id: int, nombre: str, nacionalidad: str):
    autor = db.query(Autor).filter(Autor.id == autor_id).first()
    if autor:
        autor.nombre = nombre
        autor.nacionalidad = nacionalidad
        db.commit()
        db.refresh(autor)
    return autor

def delete_autor(db: Session, autor_id: int):
    autor = db.query(Autor).filter(Autor.id == autor_id).first()
    if autor:
        db.delete(autor)
        db.commit()
    return autor

# Servicios para Libro
def get_libros(db: Session):
    return db.query(Libro).all()

def create_libro(db: Session, titulo: str, autor_id: int, fecha_publicacion: str):
    nuevo_libro = Libro(titulo=titulo, autor_id=autor_id, fecha_publicacion=fecha_publicacion)
    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)
    return nuevo_libro

def update_libro(db: Session, libro_id: int, titulo: str, autor_id: int, fecha_publicacion: str):
    libro = db.query(Libro).filter(Libro.id == libro_id).first()
    if libro:
        libro.titulo = titulo
        libro.autor_id = autor_id
        libro.fecha_publicacion = fecha_publicacion
        db.commit()
        db.refresh(libro)
    return libro

def delete_libro(db: Session, libro_id: int):
    libro = db.query(Libro).filter(Libro.id == libro_id).first()
    if libro:
        db.delete(libro)
        db.commit()
    return libro
