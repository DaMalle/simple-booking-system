#! /usr/bin/env python3

# Local imports
from booking.data.database import Database

class ReservationData:
    def __init__(self):
        with Database() as db:
            db.execute('''CREATE TABLE IF NOT EXISTS Reservation (
                            time text Not NULL,
                            email text NOT NULL)
                           ''')

    def add(self, time, email):
        with Database() as db:
            db.execute('INSERT INTO Reservation (time, email) VALUES (?,?)', (time, email))

    def get_all_time(self):
        with Database() as db:
            return db.query('SELECT time FROM Reservation')

    def get_all_reservations(self):
        with Database() as db:
            return db.query('SELECT * FROM Reservation')

    def delete(self, timestamp):
        with Database() as db:
            db.execute('DELETE * FROM tasks WHERE time=?', (timestamp))