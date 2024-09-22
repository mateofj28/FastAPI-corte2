"""Database models for the FastAPI application.

This module contains the database models used for the application,
including StoreModel and InventoryModel.
"""

from datetime import date
import os
from dotenv import load_dotenv
from peewee import *

load_dotenv()

# Database configuration
database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)

class BookModel(Model):
    """Model representing a book.

    Attributes:
        id (AutoField): Primary key for the book.
        title (CharField): Title of the book.
        author (ForeignKeyField): Relationship to the author of the book.
        publication_date (DateField): Date of publication of the book.
    """

    id = AutoField(primary_key=True)
    title = CharField(max_length=100, index=True) 
    author = ForeignKeyField(AuthorModel, backref='authors')
  
    publication_date = DateField()

    class Meta:
        database = database
        table_name = "books"



class AuthorModel(Model):
    """Model representing a store user.

    Attributes:
        id (AutoField): Primary key for the user.
        name (CharField): Name of the user.
        nationality (CharField): Nationality of the user.
        books (ForeignKeyField): Relationship to books written by the user.
    """

    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    nationality = CharField(max_length=50)
    books = ForeignKeyField(BookModel, backref='books')
    

    class Meta:
        database = database
        table_name = "author"


