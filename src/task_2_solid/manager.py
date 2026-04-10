from interfaces import LibraryInterface
from models import Book


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        self.library.add_book(Book(title, author, year))

    def remove_book(self, title: str) -> bool:
        return self.library.remove_book(title)

    def get_books(self) -> list[Book]:
        return self.library.get_books()
