import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS clothes (id INTEGER PRIMARY KEY, clothes text, customer text, order_time datetime, retailer text, price text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM clothes")
        rows = self.cur.fetchall()
        return rows

    def insert(self, clothes, customer, order_time, retailer, price):
        self.cur.execute("INSERT INTO clothes VALUES (NULL, ?, ?, ?, ?, ?)",
                         (clothes, customer, order_time, retailer, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM clothess WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, clothes, customer, order_time, retailer, price):
        self.cur.execute("UPDATE clothess SET clothes = ?, customer = ?, retailer = ?, price = ?, order_time = ? WHERE id = ?",
                         (clothes, customer, order_time, retailer, price, order_time, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
