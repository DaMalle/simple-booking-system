#! /usr/bin/env python3

# Local imports
from booking.data.database import Database

class UserData:
    def __init__(self):
        with Database() as db:
            db.execute('''CREATE TABLE IF NOT EXISTS Users (
                            mail text NOT NULL,
                            first_name text NOT NULL,
                            last_name text NOT NULL,
                            password text NOT NULL,
                            role text NOT NULL)
                           ''')

    def add(self, mail, first_name, last_name, password, role):
        with Database() as db:
            db.execute('INSERT INTO Users (mail, first_name, last_name, password, role) VALUES (?,?,?,?,?)', (mail, first_name, last_name, password, role))