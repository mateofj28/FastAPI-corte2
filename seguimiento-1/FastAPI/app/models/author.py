"""
This module defines the Author model for the FastAPI application.

The Author model includes the fields:
- id: Unique identifier for the author
- name: Name of the author
- nationality: Nationality of the author
"""

from pydantic import BaseModel

class Author(BaseModel):
    """
    Author model representing the details of an author.

    Attributes:
    - id: int, unique identifier for the author
    - name: str, the name of the author
    - nationality: str, the nationality of the author
    """
    id: int
    name: str
    nationality: str
