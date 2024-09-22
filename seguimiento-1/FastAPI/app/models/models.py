"""
This module contains the database models for the application.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# pylint: disable=too-few-public-methods
class Author(Base):
    """
    Model for the authors table. Each author can have multiple books.
    """

    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    nationality = Column(String)

    books = relationship("Book", back_populates="author")


# pylint: disable=too-few-public-methods
class Book(Base):
    """
    Model for the books table. Each book is associated with an author.
    """

    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    publication_date = Column(Date)

    author = relationship("Author", back_populates="books")
