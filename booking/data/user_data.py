#! /usr/bin/env python3

# Local imports
from booking.data.database import Database

class UserData:
    def __init__(self):
        with Database('Database.db') as db:
            db.execute('''CREATE TABLE IF NOT EXISTS Users (
                            id INTEGER NOT NULL PRIMARY KEY,
                            name text NOT NULL,
                            password text NOT NULL,
                            role text NOT NULL)
                           ''')

    def add(self, id, name, password, role):
        with Database('Database.db') as db:
            db.execute('INSERT INTO Users (id, name, password, role) VALUES (?,?,?,?)', (id, name, password, role))

    def delete(self):
        pass

    def edit(self):
        pass