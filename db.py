### Module to comunicate with the database

import sqlite3


class Database_connection:
    def __init__(self):
        self.connection = sqlite3.connect('brews.db')
        self.cursor = self.connection.cursor()

    def open_brews(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS brews (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        DATE TEXT NOT NULL,
        TIME TEXT NOT NULL,
        TIME_OF_BREWING INTEGER,
        GRINDER_SETTINGS varchar2 NOT NULL,
        coffee INTEGER
        )''')

        self.cursor.execute('''INSERT INTO brews (DATE, TIME, TIME_OF_BREWING, GRINDER_SETTINGS)
        VALUES('17.06.2026', '15:00', 45, '1.1.0')''')

        self.cursor.execute('''SELECT * FROM brews''')
        for row in self.cursor.fetchall():
            print(row)


    def commit(self):
        self.connection.commit()

x = Database_connection()
x.open_brews()
x.commit()
