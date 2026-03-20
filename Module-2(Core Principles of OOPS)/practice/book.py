"""
Book Class Demo (Object-Oriented Programming)

This script demonstrates a simple OOP example in Python.

Concepts shown:
- Class and Object
- Private Attributes (Encapsulation)
- Methods (borrow, return, check availability)
- Working with list-based data
"""

class Book:
    def __init__(self, titles: list[str], authors: list[str], isAvailable: list[bool]) -> None:
        self.title = titles
        self.author = authors
        self.__isAvailable = isAvailable  # private attribute

    # Method to borrow a book
    def borrowBook(self, book_name: str) -> None:
        if book_name in self.title:
            bookIndex = self.title.index(book_name)

            if self.__isAvailable[bookIndex]:
                self.__isAvailable[bookIndex] = False
            else:
                print("Book is not available.")
        else:
            print("Book not found.")

    # Method to return a book
    def returnBook(self, book_name: str) -> None:
        if book_name in self.title:
            bookIndex = self.title.index(book_name)
            self.__isAvailable[bookIndex] = True
        else:
            print("Book not found.")

    # Method to check availability
    def getAvailability(self, book_name: str) -> None:
        if book_name in self.title:
            bookIndex = self.title.index(book_name)

            if self.__isAvailable[bookIndex]:
                print("true")
            else:
                print("false")
        else:
            print("Book not found.")


# Driver code
if __name__ == "__main__":

    titles = ["Book1", "Book2", "Book3"]
    authors = ["Author1", "Author2", "Author3"]
    isAvailable = [True, False, True]

    book = Book(titles, authors, isAvailable)

    # Simulating operations
    methodCalls = [
        ["1", "Book1"],  # borrow
        ["3", "Book1"],  # check
        ["2", "Book1"],  # return
        ["3", "Book1"],  # check
        ["1", "Book2"],  # not available
    ]

    for methodCall in methodCalls:
        operation = methodCall[0]
        bookName = methodCall[1]

        if operation == "1":
            book.borrowBook(bookName)
        elif operation == "2":
            book.returnBook(bookName)
        elif operation == "3":
            book.getAvailability(bookName)