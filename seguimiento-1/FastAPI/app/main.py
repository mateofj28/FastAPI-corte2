from fastapi import FastAPI
from app.routes import routes
from app.database import engine
from app.models.models import Base

app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir las rutas
app.include_router(routes.router)

# Ejecutar el servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

