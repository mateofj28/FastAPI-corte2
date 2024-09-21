"""
Este módulo inicializa y configura la aplicación FastAPI, crea las tablas en la base de datos 
utilizando SQLAlchemy, y define el punto de entrada para ejecutar el servidor con Uvicorn.

- app: Instancia principal de la aplicación FastAPI.
- Base.metadata.create_all: Crea las tablas en la base de datos si no existen.
- app.include_router: Incluye las rutas definidas en el archivo routes.py.
- uvicorn.run: Ejecuta el servidor FastAPI cuando el script es ejecutado directamente.
"""

from fastapi import FastAPI
from app.routes import routes
from app.database import engine
from app.models.models import Base

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Crear las tablas en la base de datos
# Si no existen las tablas, SQLAlchemy las creará automáticamente
Base.metadata.create_all(bind=engine)

# Incluir las rutas definidas en el archivo routes.py
app.include_router(routes.router)

# Punto de entrada principal de la aplicación
# Ejecutar el servidor utilizando Uvicorn
if __name__ == "__main__":
    # Ejecuta el servidor FastAPI usando Uvicorn
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
