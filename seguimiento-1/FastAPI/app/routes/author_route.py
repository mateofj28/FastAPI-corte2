"""
Routes module for managing CRUD operations for the Author entity.

This module provides routes to create, read, update, and delete authors.
"""

from fastapi import APIRouter, Body
from models.author import Author
from services.author_service import AuthorService


author_router = APIRouter()
author_service = AuthorService()

@author_router.post("/author")
def create_author(author: Author):
    """
    Creates a new author and adds it to the system.

    Args:
        author (Author): The author data to create.

    Returns:
        Author: The created author.
    """
    return author_service.create_author(author)

@author_router.get("/author")
def get_authors():
    """
    Retrieves all authors in the system.

    Returns:
        List[Author]: A list of all authors.
    """
    return author_service.get_all_authors()

@author_router.get("/author/{author_id}")
def get_author(author_id: int):
    """
    Retrieves an author by their ID.

    Args:
        author_id (int): The ID of the author to retrieve.

    Returns:
        Author: The author with the given ID, or None if not found.
    """
    return author_service.get_author_by_id(author_id)

@author_router.put("/author/{author_id}")
def update_author(author_id: int, author: Author):
    """
    Updates an existing author with new data.

    Args:
        author_id (int): The ID of the author to update.
        author (Author): The updated author data.

    Returns:
        Author: The updated author.
    """
    return author_service.update_author(author_id, author)

@author_router.delete("/author/{author_id}")
def delete_author(author_id: int):
    """
    Deletes an author from the system by their ID.

    Args:
        author_id (int): The ID of the author to delete.

    Returns:
        None: The author is deleted if found.
    """
    return author_service.delete_author(author_id)
