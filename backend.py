import sqlite3

class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, author INTEGER, year INTEGER, isbn INTEGER)")
        self.conn.commit()
        
    def insert(self, title,author,year,isbn):
        self.cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)", (title,author,year,isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM books ORDER BY id DESC")
        return self.cur.fetchall()

    def search(self, title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        return self.cur.fetchall()

    def delete(self, id):
        self.cur.execute("DELETE FROM books WHERE id=?",(id,))
        self.conn.commit()

    def update(self, id,title,author,year,isbn):
        self.cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    #connect()
    #insert("The sky","bruce",1001,32323233234)
    #update(1,"The Sun","william",2000,32323233232)
    #delete(1)
    #print(view())
    #print(search(title="The sun"))
