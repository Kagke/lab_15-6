from flask import render_template, request
from app import app
from models.library import library, add_book,remove_book
from models.book import Book

@app.route('/')
def index_render():
   return render_template('index.html')

@app.route('/library')
def library_render():
    return render_template('library.html', title='Library', library=library)

@app.route('/admin')
def admin_render():
    return render_template('admin.html', title='Admin',library=library)

@app.route('/library/book/<bookid>')
def book_render(bookid):
    book = library[bookid]
    return render_template('book.html', title=book.title, book=book)

@app.route('/library/add', methods=['POST'])
def add_task():
  book_title = request.form['title']
  book_author = request.form['author']
  book_genre = request.form['genre']
  try:
    book_checked_out = request.form['checked_out']
  except:
    book_checked_out = False
  new_book = Book(book_title,book_author,book_genre,book_checked_out)
  add_book(new_book)
  return render_template('admin.html', title='Admin', library=library)

@app.route("/library/remove/" , methods = ["POST"])
def remove():
   remove_book(request.form['book_id'])
   return render_template('admin.html', title='Admin', library=library)