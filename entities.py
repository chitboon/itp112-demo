from settings import *
import firebase_admin
from firebase_admin import credentials, db

class Book:
    def __init__(self):
        self.id = ''
        self.title = ''
        self.description = ''
        self.price = 0
        self.rating = 0

def init_firebase():
    cred = credentials.Certificate(FIRE_BASE_CRED)
    fb_url = {'databaseURL': 'https://it3178.firebaseio.com/'}
    default_app = firebase_admin.initialize_app(cred, fb_url)

# get book list from file, books.txt
def get_book_list():
    f = open(BOOK_FILE)
    book_list = []
    # iterate through the file
    for line in f:
        # split each line with the ',' and store in the list element
        # 4 elements in the list, refer to books.txt for details
        # potentially this will give runtime error if the file does not have the right format
        list = line.split(',')
        b = Book()
        b.title = list[0]
        b.price = float(list[1])
        b.description = list[2]
        b.rating = int(list[3])
        book_list.append(b)
    return book_list

# get book list from firebase
def get_books():
    root = db.reference('/book')
    books = root.get()
    book_list = []
    for book_id in books:
        book_dict = books.get(book_id)
        book = Book()
        book.id = book_id
        book.title = book_dict.get('title')
        book.description = book_dict.get('description')
        book.price = float(book_dict.get('price'))
        book.rating = int(book_dict.get('rating'))
        book_list.append(book)
    return book_list

init_firebase()
