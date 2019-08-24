import sqlite3
from contextlib import closing

conn = None

def connect():
    global conn

    if conn:
        return conn.cursor()

    DB_FILE = 'Test.db'
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row

    return conn

def close():
    if conn:
        conn.close()
