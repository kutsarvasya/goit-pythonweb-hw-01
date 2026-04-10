from abc import ABC, abstractmethod
from models import Book


class LibraryInterface(ABC):

    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> bool:
        pass

    @abstractmethod
    def get_books(self) -> list[Book]:
        pass
