#! /usr/bin/env python3

# Local imports
from booking.data.database import Database

class UserData:
    def __init__(self):
        with Database() as db:
            db.execute('''CREATE TABLE IF NOT EXISTS Users (
                            email text NOT NULL,
                            first_name text NOT NULL,
                            last_name text NOT NULL,
                            password text NOT NULL,
                            role text NOT NULL)
                           ''')

    def add(self, email, first_name, last_name, password, role):
        with Database() as db:
            db.execute('INSERT INTO Users (email, first_name, last_name, password, role) VALUES (?,?,?,?,?)', (email, first_name, last_name, password, role))

    def get_all_emails(self):
        with Database() as db:
            return db.query('''SELECT email FROM Users''')

    def get_password(self, email):
        with Database() as db:
            db.execute('''SELECT password FROM Users WHERE email=?''', (email,))
            return db.fetchone()

    def get_user(self, email):
        with Database() as db:
            db.execute('''SELECT * FROM Users WHERE email=?''', (email,))
            return db.fetchone()

    def delete_user(self, email):
        with Database() as db:
            db.execute('''DELETE FROM users WHERE email=?''', (email,))
