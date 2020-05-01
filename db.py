import sqlite3


def init():
    with sqlite3.connect('db.sqlite') as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE Users 
                         ( Id TEXT UNIQUE PRIMARY KEY,
                           Name TEXT,
                           Email TEXT UNIQUE,
                           Dob  DATE,
                           Address TEXT,
                           Occupation TEXT,
                           Phone INTEGER UNIQUE,
                           Username TEXT,
                           Password TEXT,
                           OS_Id TEXT NOT NULL UNIQUE
                         );
                      ''')
        db.commit()
        cursor.close()


def collect(id, name, email, dob, address, occupation, phone, os_id):
    sqliteConnection = sqlite3.connect('db.sqlite')
    cursor = sqliteConnection.cursor()
    sqlite_insert_query = """INSERT INTO Users (id, name, email, dob, address, occupation, phone, os_id) 
                             VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
    data = (id, name, email, dob, address, occupation, phone, os_id)
    cursor.execute(sqlite_insert_query, data)
    sqliteConnection.commit()
    cursor.close()
    sqliteConnection.close()

