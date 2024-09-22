"""
Routes module for managing CRUD operations for the Book entity.

This module provides routes to create, read, update, and delete books.
"""

from fastapi import APIRouter
from models.book import Book
from services.book_service import BookService

book_router = APIRouter()
book_service = BookService()

@book_router.post("/book")
def create_book(book: Book):
    """
    Creates a new book and adds it to the system.

    Args:
        book (Book): The book data to create.

    Returns:
        Book: The created book.
    """
    return book_service.create_book(book)

@book_router.get("/book")
def get_books():
    """
    Retrieves all books in the system.

    Returns:
        List[Book]: A list of all books.
    """
    return book_service.get_all_books()

@book_router.get("/book/{book_id}")
def get_book(book_id: int):
    """
    Retrieves a book by its ID.

    Args:
        book_id (int): The ID of the book to retrieve.

    Returns:
        Book: The book with the given ID, or None if not found.
    """
    return book_service.get_book_by_id(book_id)

@book_router.put("/book/{book_id}")
def update_book(book_id: int, book: Book):
    """
    Updates an existing book with new data.

    Args:
        book_id (int): The ID of the book to update.
        book (Book): The updated book data.

    Returns:
        Book: The updated book.
    """
    return book_service.update_book(book_id, book)

@book_router.delete("/book/{book_id}")
def delete_book(book_id: int):
    """
    Deletes a book from the system by its ID.

    Args:
        book_id (int): The ID of the book to delete.

    Returns:
        None: The book is deleted if found.
    """
    return book_service.delete_book(book_id)
