#! /usr/bin/env python3

# Local imports
from booking.data.database import Database

class ReservationData:
    def __init__(self):
        with Database() as db:
            db.execute('''CREATE TABLE IF NOT EXISTS Reservation (
                            time text Not NULL,
                            email text NOT NULL
                           ''')

    def add(self, time, email):
        with Database() as db:
            db.execute('INSERT INTO Reservation (time, email, first_name, last_name) VALUES (?,?)', (time, email))

    def get_all_reservations(self):
        with Database() as db:
            db.execute('''SELECT time FROM Reservation''')
            return db.fetchall()