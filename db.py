#! /user/bin/env Python 3.7
# Module to connect to the SQL database and functions for running the SQL scripts.
import sys
import os
import sqlite3
from contextlib import *

from mod_ProfessionObjects import *

conn = None

def connect():
    global conn
    if not conn:
        if sys.platform == "win32":
            DB_FILE = '''C:/SQLite/Databases/Test.db'''
        else:
            HOME = os.environ["Home"]
            DB_FILE = HOME + "/Documents//SQLite/Databases/Test.db"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        return c

def close():
    if conn:
        conn.close()

def make_Profession(row):
    return Profession(row['ProfessionID'], row['Profession'])

def get_Profession():
    query = '''SELECT Profession 
                FROM tbl_Professions'''
    c = connect()
    c.execute(query)
    results = c.fetchall()
    close()

    professions = []
    for row in results:
        professions.append(make_Profession(row))
    return professions
