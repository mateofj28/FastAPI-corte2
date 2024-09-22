"""
Database models for the FastAPI application.

This module contains the database models used for the application,
including AuthorModel and BookModel.
"""

from datetime import date
import os
from dotenv import load_dotenv
from peewee import *

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos MySQL
database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)

class BaseModel(Model):  # pylint: disable=too-few-public-methods
    """
    Base model that sets up the database for all tables.

    This class ensures all models inherit the database connection.
    """
    class Meta:
        database = database

class AuthorModel(BaseModel):  # pylint: disable=too-few-public-methods
    """
    Model representing an author.

    Attributes:
        id (int): Primary key for the author.
        name (str): Name of the author.
        nationality (str): Nationality of the author.
    """
    
    id = AutoField(primary_key=True)
    name = CharField(max_length=100)
    nationality = CharField(max_length=100)

    class Meta:
        table_name = "authors"

class BookModel(BaseModel):  # pylint: disable=too-few-public-methods
    """
    Model representing a book.

    Attributes:
        id (int): Primary key for the book.
        title (str): Title of the book.
        author_id (int): Foreign key referencing the author.
        publication_date (date): Date when the book was published.
    """
    
    id = AutoField(primary_key=True)
    title = CharField(max_length=200)
    author_id = ForeignKeyField(AuthorModel, backref="books", on_delete="CASCADE")
    publication_date = DateField(default=date.today)

    class Meta:
        table_name = "books"

# Conectar a la base de datos y crear las tablas si no existen
def initialize_database():
    """
    Connect to the database and create tables if they do not exist.

    This function initializes the connection to the database and ensures that
    the tables for AuthorModel and BookModel are created.
    """
    with database:
        database.create_tables([AuthorModel, BookModel])
