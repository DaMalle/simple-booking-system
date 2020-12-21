import tkinter as tk
class Table_field:

    def __init__(self, parent, x, y, text):
        self.parent = parent
        self.text = text
        self.x = x
        self.y = y
        self.button = tk.Button(self.parent, text=self.text, width=3, command=self.but_pos)
        self.button.grid(column=self.x, row=self.y+2)

    def but_pos(self): #prints the coordinates of the button
        print(f"{self.x+9}:{self.text}")
        if self.parent.reserve_status == True:




class Table(tk.Frame):
    """A frame in which you can view bookings in the booking system"""
    def __init__(self, main):
        super().__init__(main)
        self.main = main
        self.time_list = ["00", "07", "15", "22", "30", "37", "45", "52"]
        self.reserve_status = False


        self.draw_widgets()


    def draw_widgets(self):
        hour = 9
        for i in range(10):
            tk.Button(self, text=str(hour), width=3, height=2,  bg="#72DBFF").grid(column=i, row=1)
            hour += 1
        for x in range(10):
            for y in range(8):
                Table_field(self, x, y, text=self.time_list[y])
        self.reserve_button = tk.Button(self, text="Reserver tider", command=self.reserve)
        self.reserve_button.grid(column=12, row=8)

    def reserve(self):
        if self.reserve_status == False:
            self.reserve_button.config(relief="sunken")
            self.reserve_status = True
        elif self.reserve_status == True:
            self.reserve_button.config(relief="raised")
            self.reserve_status = False

