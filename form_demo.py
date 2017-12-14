from settings import *
from entities import *
from flask import Flask, render_template, request
from wtforms import Form
from forms import BookForm

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def default():
    form = BookForm(request.form)
    if (request.method == 'POST' and form.validate() ):
        print(form.data)
        add_book(form.data)
        book_list = get_books()
        return render_template('/home.html', bks=book_list)
    return render_template('create.html', form=form)


if __name__ == '__main__':
    app.secret_key = 'Python'
    app.run()
