from peewee import DoesNotExist, IntegrityError
from fastapi import Body, HTTPException
from models.author import Author
from database import AuthorModel

class AuthorService:
    def __init__(self):
        self.authors = []

    def create_author(self, author):
        self.authors.append(author)
        return author

    def get_all_authors(self):
        return self.authors

    def get_author_by_id(self, author_id):
        return next((a for a in self.authors if a.id == author_id), None)

    def update_author(self, author_id, author_data):
        author = self.get_author_by_id(author_id)
        if author:
            author.name = author_data.name
            author.nationality = author_data.nationality
        return author

    def delete_author(self, author_id):
        self.authors = [a for a in self.authors if a.id != author_id]
