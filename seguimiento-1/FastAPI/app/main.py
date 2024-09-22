"""
Main module for FastAPI application setup.

This module sets up the FastAPI application, manages the database connection
lifecycle, and includes routes.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from helpers.api_key_auth import get_api_key
from starlette.responses import RedirectResponse
from database import database as connection
from routes.author_route import author_router
from routes.book_route import book_router

@asynccontextmanager
async def manage_lifespan(_app: FastAPI):
    """
    Manage the lifespan of the FastAPI application.

    Ensures the database connection is opened and closed properly.
    """
    if connection.is_closed():
        connection.connect()
    try:
        yield
    finally:
        if not connection.is_closed():
            connection.close()

app = FastAPI(
    title="Microservicio de libros",
    version="2.0",
    contact={
        "name": "julian andres arango",
        "url": "https://github.com/Julian-Aa",
        "email": "julian.arango.re@gmail.com",
    },
    lifespan=manage_lifespan
)

@app.get("/")
async def read_root():
    """
    Redirect the root path to the API documentation.

    Returns a redirection response to the documentation page.
    """
    return RedirectResponse(url="/docs")

app.include_router(author_router,
                   prefix="/authors",
                   tags=["Authors"],
                   dependencies=[Depends(get_api_key)])

app.include_router(book_router,
                   prefix="/books",
                   tags=["Books"],
                   dependencies=[Depends(get_api_key)])