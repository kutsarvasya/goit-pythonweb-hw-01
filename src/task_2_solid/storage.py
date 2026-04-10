from abc import ABC, abstractmethod
from models import Book


class StorageInterface(ABC):

    @abstractmethod
    def add(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove(self, title: str) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> list[Book]:
        pass


class InMemoryStorage(StorageInterface):
    def __init__(self) -> None:
        self._books: list[Book] = []

    def add(self, book: Book) -> None:
        self._books.append(book)

    def remove(self, title: str) -> bool:
        for book in self._books:
            if book.title == title:
                self._books.remove(book)
                return True
        return False

    def get_all(self) -> list[Book]:
        return self._books
