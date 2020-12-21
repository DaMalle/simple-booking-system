#! /usr/bin/env python3

# Local imports
from booking.data.reservation_data import ReservationData


class ReservationLogic:
    def __init__(self):
        self.ReservationData = ReservationData()

    def reservate(self, time, email, first_name, last_name):
        self.ReservationData.add(time, email, first_name, last_name)
