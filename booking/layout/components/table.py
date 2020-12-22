# built-in imports
import tkinter as tk
# local imports
from booking.logic.reservation_logic import ReservationLogic


class Table_field:

    def __init__(self, parent, x, y, text):
        self.parent = parent
        self.text = text
        self.x = x
        self.y = y
        self.time = f"{self.x + 9}:{self.text}"
        self.button = tk.Button(self.parent, text=self.text, width=3, bg="white", command=self.but_pos)
        self.button.grid(column=self.x, row=self.y + 2)

    def but_pos(self):
        if self.parent.reserve_status == True:
            self.button.config(bg="blue")
            self.parent.reserve_status = False
            self.parent.reserve_button.config(relief="raised")
            self.parent.new_reservations.append(self)


class Table(tk.Frame):
    """A frame in which you can view bookings in the booking system"""

    def __init__(self, main, user):
        super().__init__(main)
        self.main = main
        self.user = user
        self.time_list = ["00", "07", "15", "22", "30", "37", "45", "52"]
        self.reserve_status = False
        self.logic = ReservationLogic()
        self.fields = []
        self.new_reservations = []

        self.draw_widgets()
        self.update_fields()

    def draw_widgets(self):
        hour = 9
        for i in range(10):
            tk.Button(self, text=str(hour), state="disabled", width=3, height=2, bg="#72DBFF").grid(column=i, row=1)
            hour += 1
        for x in range(10):
            for y in range(8):
                self.fields.append(Table_field(self, x, y, text=self.time_list[y]))

        print(self.logic.get_reservation_list())

        self.reserve_button = tk.Button(self, text="Reserver tider", command=self.reserve)
        self.reserve_button.grid(column=12, row=8)

        self.accept_button = tk.Button(self, text="Godkend", command=self.accept)
        self.accept_button.grid(column=12, row=9)

        self.cancel_button = tk.Button(self, text="Annullér", command=self.cancel)
        self.cancel_button.grid(column=13, row=9)

    def reserve(self):
        if self.reserve_status == False:
            self.reserve_button.config(relief="sunken")
            self.reserve_status = True
        elif self.reserve_status == True:
            self.reserve_button.config(relief="raised")
            self.reserve_status = False

    def accept(self):
        for i in self.new_reservations:
            self.logic.reservate(i.time, self.user)
            i.button.config(state="disabled", bg="green")
        self.new_reservations = []

    def cancel(self):
        for i in self.new_reservations:
            i.button.config(bg="white")
        self.new_reservations = []

    def update_fields(self):
        a = self.logic.get_reservation_list()
        print(a)
        for i in self.fields:
            i.button.config(bg="white", state="normal")
            for j in a:
                if i.time in j and self.user not in j:
                    i.button.config(bg="red", state="disabled")
                elif i.time in j and self.user in j:
                    i.button.config(bg="green", state="disabled")




