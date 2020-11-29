#! /usr/bin/env python3

# built-in imports
import sqlite3
import pathlib

# local imports
import booking

class Database:
    def __init__(self):
        self.path = f'{pathlib.Path(booking.__file__).resolve().parent}/data/Database.db'
        self._connection = sqlite3.connect(self.path)
        self._cursor = self._connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    @property
    def connection(self):
        return self._connection

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
