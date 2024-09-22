from peewee import DoesNotExist, IntegrityError
from fastapi import Body, HTTPException
from models.book import Book
from database import BookModel

class BookService:
    def __init__(self):
        self.books = []

    def create_book(self, book):
        self.books.append(book)
        return book

    def get_all_books(self):
        return self.books

    def get_book_by_id(self, book_id):
        return next((b for b in self.books if b.id == book_id), None)

    def update_book(self, book_id, book_data):
        book = self.get_book_by_id(book_id)
        if book:
            book.title = book_data.title
            book.author_id = book_data.author_id
            book.publication_date = book_data.publication_date
        return book

    def delete_book(self, book_id):
        self.books = [b for b in self.books if b.id != book_id]
