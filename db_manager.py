import sqlite3

class DBManager:
    def __init__(self, db_path="library.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT,
                                author TEXT,
                                genre TEXT,
                                pub_date TEXT,
                                read_date TEXT,
                                rating INTEGER,
                                pages INTEGER)''')
        self.conn.commit()

    def add_book(self, title, author, genre, pub_date, read_date, rating, pages):
        self.cursor.execute("INSERT INTO books (title, author, genre, pub_date, read_date, rating, pages) VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (title, author, genre, pub_date, read_date, rating, pages))
        self.conn.commit()

    def get_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    def update_book(self, book_id, title, author, genre, pub_date, read_date, rating, pages):
        self.cursor.execute('''UPDATE books SET title=?, author=?, genre=?, pub_date=?, read_date=?, rating=?, pages=? WHERE id=?''',
                            (title, author, genre, pub_date, read_date, rating, pages, book_id))
        self.conn.commit()

    def delete_book(self, book_id):
        self.cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
        self.conn.commit()

    def search_books(self, query):
        query = f"%{query}%"
        self.cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", (query, query))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
