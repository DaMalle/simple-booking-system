#! /usr/bin/env python3

# built-in imports
import tkinter as tk

# local imports
from booking.layout.components.table import Table
from booking.logic.reservation_logic import ReservationLogic
from booking.layout.reservation_page import ReservationPage

class BookingPage(tk.Frame):
    """A frame in which you can view bookings in the booking system"""
    def __init__(self, main, user):
        super().__init__(main)
        self.main = main
        self.main.title('Booking')
        self.courses = ["18 hullers bane", "9 hullers bane", "Par 3 bane"]
        self.current_user = user
        self.logic = ReservationLogic()
        self.draw_widgets()


    def draw_widgets(self):

        self.my_reservations_button = tk.Button(self, text="Mine reservationer", command=self.my_reservations)
        self.my_reservations_button.grid(column=3, row=1)

        self.log_out_button = tk.Button(self, text="Logud", command=self.log_out)
        self.log_out_button.grid(column=5, row=1)

        self.table = Table(self, self.current_user)
        self.table.grid(column=2, row=3, columnspan=10)



    def log_out(self):
        self.destroy()
        pass

    def my_reservations(self):
        a = self.logic.get_reservation_list()
        b = []
        for i in a:
            if self.current_user in i:
                b.append(i[0])
        ReservationPage(self.main, b).grid(column=0, row=1, sticky="NEWS")



