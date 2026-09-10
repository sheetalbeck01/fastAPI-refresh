from fastapi import FastAPI

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