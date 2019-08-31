import sqlite3

def connect():
    conn = sqlite3.connect('./../Test.db')
    conn.row_factory = sqlite3.Row
    return conn

def close(conn):
    if conn:
        conn.close()
