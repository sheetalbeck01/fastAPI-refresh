from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'The Alchemist', 'author': 'Paulo Coelho', 'category': 'Fiction'},
    {'title': 'Atomic Habits', 'author': 'James Clear', 'category': 'Self Help'},
    {'title': 'The Psychology of Money', 'author': 'Morgan Housel', 'category': 'Finance'},
    {'title': 'Rich Dad Poor Dad', 'author': 'Robert Kiyosaki', 'category': 'Finance'},
    {'title': 'Deep Work', 'author': 'Cal Newport', 'category': 'Productivity'},
    {'title': 'Meditations', 'author': 'Marcus Aurelius', 'category': 'Philosophy'},
    {'title': 'The Art of War', 'author': 'Sun Tzu', 'category': 'Strategy'},
    {'title': '1984', 'author': 'George Orwell', 'category': 'Fiction'},
    {'title': 'Sapiens', 'author': 'Yuval Noah Harari', 'category': 'History'},
    {'title': 'Ikigai', 'author': 'Hector Garcia', 'category': 'Self Help'},
    {'title': 'Think and Grow Rich', 'author': 'Napoleon Hill', 'category': 'Self Help'},
    {'title': 'The Power of Habit', 'author': 'Charles Duhigg', 'category': 'Productivity'},
    {'title': 'Clean Code', 'author': 'Robert C. Martin', 'category': 'Programming'},
    {'title': 'Python Crash Course', 'author': 'Eric Matthes', 'category': 'Programming'},
    {'title': 'The Pragmatic Programmer', 'author': 'Andrew Hunt', 'category': 'Programming'}
]

@app.get("/books")
def get_all_books():
    return BOOKS


# Path Parameters
@app.get("/books/{book_title}")
def get_book(book_title: str): # Must be a string
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

# Query Parameters
@app.get("/books/")
def query_by_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Path parameter & a query parameter
@app.get("/books/{book_author}/")
def query_by_category_and_author(book_author:str, category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():

            books_to_return.append(book)

    return books_to_return

# Creating Books
@app.post("/books/create_book")
def create_book(new_book=Body()):
    BOOKS.append(new_book)

# Updating Books
@app.put("/books/update_book")
def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.get('title').casefold():
            BOOKS[i] = update_book


# Deleting Book
@app.delete("/books/delete_book/{book_title}")
def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break