from settings import *
from entities import *
from flask import Flask, render_template

app = Flask(__name__)
print(__name__)
@app.route('/')
def default():
    # gets a list of books from the file books.txt
    book_list = get_books()
    return render_template('/home.html', bks = book_list)


@app.route('/book')
def home():
#    book_list = get_book_list()
    book_list = get_books()
    return render_template('/index.html', books = book_list)


@app.route('/book/<title>')
def get_book(title):
    return render_template('/book.html')

@app.route('/test/<function>')
def test(function):
    if function == 'create':
        book = {
            'bkx12': {'title': 'Basic Javascript', 'description': 'Javascript for dummies', 'price': '21',
                      'rating': '1'},
            'bkx22': {'title': 'Basic Java', 'description': 'Good for Java beginner', 'price': '12',
                      'rating': '2'},
            'bkx52': {'title': 'Basic Python', 'description': 'Best introductory Python book', 'price': '29',
                      'rating': '3'},
            'bkx26': {'title': 'Advanced Python', 'description': 'More tips and tricks for python', 'price': '39',
                      'rating': '4'},
        }
        create_book(book)
        return 'Create Book Store Successful'
    elif function == 'add':
        book = {
            'title': 'Intermediate Python', 'description': 'Make you a better Python Developer', 'price': '35',
                      'rating': '4'

        }
        add_book(book)
        return 'Add a book successful'
    elif function == 'update':
        dict = {'price':'1'}
        update_book(dict)
        return 'Update a book'

if __name__ == '__main__':
    app.secret_key = 'Python'
    app.run(port=80)
