"""Create a Library class that stores a list of books.

Implement add_book(title) and list_books() methods."""

class Library:
    
    # self method
    def __init__(self):
        # book list
        self.book_list = []

    # book method
    def add_book(self, book):
        self.book_list.append(book)

    def list_books(self):
        for book in self.book_list:
            print(book)
    

lib = Library()
lib.add_book("1984")
lib.add_book("Brave New World")
lib.list_books()  # Should list both books
