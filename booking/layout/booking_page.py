#! /usr/bin/env python3

# built-in imports
import tkinter as tk

# local imports
from booking.layout.components.table import Table

class BookingPage(tk.Frame):
    """A frame in which you can view bookings in the booking system"""
    def __init__(self, main, user):
        super().__init__(main)
        self.main = main
        self.main.title('Booking')
        self.courses = ["18 hullers bane", "9 hullers bane", "Par 3 bane"]
        self.current_user = user

        self.draw_widgets()


    def draw_widgets(self):

        self.course_label = tk.Label(self, text="Vælg bane")
        self.course_label.grid(column=1, row=1)

        self.coursevar = tk.StringVar(self) # The var for the course_option OptionMenu
        self.coursevar.set(self.courses[0]) # Sets default value

        self.course_option = tk.OptionMenu(self, self.coursevar, *self.courses, command=self.update_table)
        self.course_option.grid(column=2, row=1)

        self.my_reservations_button = tk.Button(self, text="Mine reservationer", command=self.my_reservations)
        self.my_reservations_button.grid(column=3, row=1)

        self.my_page_button = tk.Button(self, text="Min side", command=self.my_page)
        self.my_page_button.grid(column=4, row=1)

        self.log_out_button = tk.Button(self, text="Logud", command=self.log_out)
        self.log_out_button.grid(column=5, row=1)

        self.table = Table(self)
        self.table.grid(column=2, row=3, columnspan=10)



    def update_table(self, a):
        print(a)
        pass

    def log_out(self):
        self.destroy()
        pass

    def my_reservations(self):
        pass

    def my_page(self):
        pass

