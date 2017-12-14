from settings import *
from entities import *
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
#    book_list = get_book_list()
    book_list = get_books()
    return render_template('/index.html', books = book_list)


@app.route('/book/<title>')
def get_book(title):
    return render_template('/book.html')

if __name__ == '__main__':
    app.secret_key = 'Python'
    app.run()
