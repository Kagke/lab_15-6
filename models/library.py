from models.book import Book
import random


library = {}
book1 = Book("Harry Potter" , "JK Rolling" , "Magic" , True)
book2 = Book("Stoicism" , "Aristotelis" , "Educational" , False)


def add_book(book):
    book.book_id = str(random.randint(1000000,9999999))
    while book.book_id in library.keys():
        book.book_id = str(random.randint(1000000,9999999))
    book.url = "/library/book/" + str(book.book_id)
    library[book.book_id] = book

def remove_book(book_id):
    library.pop(book_id)

add_book(book1)
add_book(book2)