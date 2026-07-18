class Library:
    def __init__(self):
        self.available_books = ["sabin", "hi", "hello"
        
        ]
    def display_books(self):
        for books in self.available_books:
            print(self.available_books)
    def add_book(self, book_name):
        self.available_books.append(book_name)
        print(f'"{book_name }" has been added successfully.')
    
    def remove_book(self, book_name):
        self.available_books.remove(book_name)
        print(f'"{book_name}" has been removed successfully.')
    
library = Library()

l1=library.add_book("sabin")
l2= library.remove_book("hi")
    
l3=library.display_books()