import tkinter as tk

class Table(tk.Frame):
    """A frame in which you can view bookings in the booking system"""
    def __init__(self, main):
        super().__init__(main)
        self.main = main
        self.time_list = ["00", "07", "15", "22", "30", "37", "45", "52"]


        self.draw_widgets()


    def draw_widgets(self):
        hour = 9
        for i in range(10):
            tk.Button(self, text=str(hour), width=3, height=2,  bg="#72DBFF").grid(column=i, row=1)
            hour += 1
        for x in range(10):
            for y in range(8):
                tk.Button(self, text=self.time_list[y], width=3).grid(column=x, row=y+2)
