"""
This module defines the Book model for the FastAPI application.

The Book model includes the fields:
- id: Unique identifier for the book
- title: Title of the book
- author_id: Foreign key referencing the Author model
- publication_date: Date when the book was published
"""

from datetime import date  # estándar
from pydantic import BaseModel  # terceros

class Book(BaseModel):
    """
    Book model representing the details of a book.

    Attributes:
    - id: int, unique identifier for the book
    - title: str, title of the book
    - author_id: int, foreign key linking to the author of the book
    - publication_date: date, the date the book was published
    """
    id: int
    title: str
    author_id: int  # Foreign Key
    publication_date: date
