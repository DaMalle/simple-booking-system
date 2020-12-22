# built-in imports
import tkinter as tk
# local imports
from booking.logic.reservation_logic import ReservationLogic


class ReservationPage(tk.Frame):  # The first window the user is greeted with
    """A frame where you can login to the booking system"""

    def __init__(self, main, reservations, table):
        super().__init__(main)
        self.main = main
        self.main.title('Mine Reservationer')

        self.table = table
        self.reservations = reservations
        if len(self.reservations) == 0:
            self.reservations.append("du har ingen reserveret tid")
        self.logic = ReservationLogic()

        self.draw_widgets()

    def draw_widgets(self):
        self.title_label = tk.Label(self, text="Mine Reservationer")
        self.title_label.grid(column=0, row=1)

        self.listvar = tk.StringVar()
        self.listvar.set(self.reservations[0])
        self.reservation_option = tk.OptionMenu(self, self.listvar, *self.reservations)
        self.reservation_option.grid(column=1, row=2)

        self.remove_button = tk.Button(self, text="Slet valgt reservation", command=self.delete)
        self.remove_button.grid(column=2, row=2)

        self.back_button = tk.Button(self, text="Gå tilbage til Booking", command=self.back)
        self.back_button.grid(column=3, row=2)

    def back(self):
        self.table.update_fields()
        self.destroy()

    def delete(self):
        a = self.listvar.get()
        self.logic.delete_reservation(a)
        for i in self.reservations:
            if a in i:
                self.reservations.remove(i)
                self.listvar.set(self.reservations[0])
        print(self.reservations)


