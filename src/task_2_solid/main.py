from library import Library
from manager import LibraryManager
from storage import InMemoryStorage
import logging
import logger_config

logger = logging.getLogger(__name__)


def main():
    storage = InMemoryStorage()
    library = Library(storage)
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
                logger.info(f"Book '{title}' added.")
            case "remove":
                title = input("Enter book title to remove: ").strip()
                if manager.remove_book(title):
                    logger.info(f"Book '{title}' removed.")
                else:
                    logger.warning(f"Book '{title}' not found.")
            case "show":
                for book in manager.get_books():
                    logger.info(book)
            case "exit":
                break
            case _:
                logger.warning("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
