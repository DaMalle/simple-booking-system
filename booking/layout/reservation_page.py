
#built-in imports
import tkinter as tk

class ReservationPage(tk.Frame): # The first window the user is greeted with
    """A frame where you can login to the booking system"""
    def __init__(self, main, reservations):
        super().__init__(main)
        self.main = main
        self.main.title('Mine Reservationer')

        self.reservations = reservations
        self.draw_widgets()

    def draw_widgets(self):
        self.title_label = tk.Label(self, text="Mine Reservationer")
        self.title_label.grid(column=0, row=1)

        self.listvar = tk.StringVar()
        self.listvar.set(self.reservations[0])
        self.reservation_option = tk.OptionMenu(self, self.listvar, *self.reservations)
        self.reservation_option.grid(column=2, row=2)

