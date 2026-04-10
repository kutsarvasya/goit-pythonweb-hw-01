from interfaces import LibraryInterface
from storage import StorageInterface
from models import Book


class Library(LibraryInterface):
    def __init__(self, storage: StorageInterface) -> None:
        self._storage = storage

    def add_book(self, book: Book) -> None:
        self._storage.add(book)

    def remove_book(self, title: str) -> bool:
        return self._storage.remove(title)

    def get_books(self) -> list[Book]:
        return self._storage.get_all()
