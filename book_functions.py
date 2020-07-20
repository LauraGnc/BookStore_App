import sqlite3

class Database:

    def __init__(self, db_path):
        self.con = sqlite3.connect(db_path)
        self.cursor = self.con.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)')
        self.con.commit()


    def view(self):
        self.cursor.execute('SELECT * FROM book')
        rows = self.cursor.fetchall()
        return rows

    def search(self, title='', author='', year='', isbn=''):
        self.cursor.execute('SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?', (title, author, year, isbn))
        rows = self.cursor.fetchall()
        return rows

    def insert(self, title, author, year, isbn):
        self.cursor.execute('INSERT INTO book VALUES (NULL, ?, ?, ?, ?)', (title, author, year, isbn))
        self.con.commit()

    def update(self, id, title, author, year, isbn):
        self.cursor.execute('UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?', (title, author, year, isbn, id))
        self.con.commit()

    def delete(self, id):
        self.cursor.execute('DELETE FROM book WHERE id=?', (id,))
        self.con.commit()

    def __del__(self):
        self.con.close()

