#! /usr/bin/env python3

# Local imports
from booking.data.reservation_data import ReservationData


class ReservationLogic:
    def __init__(self):
        self.ReservationData = ReservationData()

    def reservate(self, timestamp, email):
        if self.check_reservation(timestamp) == False or self.check_reservation(timestamp) == None:
            self.ReservationData.add(timestamp, email)
    
    def check_reservation(self, timestamp):
        if (timestamp,) in self.ReservationData.get_all_time():
            return True

    def get_reservation_list(self):
        return self.ReservationData.get_all_reservations()

    def delete_reservation(self, timestamp):
        if self.check_reservation(timestamp):
            self.ReservationData.delete(timestamp)