import tkinter as tk
class Table_field:

    def __init__(self, root, x, y, text):
        self.x = x
        self.y = y
        self.button = tk.Button(root, text=text, width=3, command=self.but_pos)
        self.button.grid(column=self.x, row=self.y)

    def but_pos(self): #prints the coordinates of the button
        print(f"{self.x},{self.y}")



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
                Table_field(self, x, y+2, text=self.time_list[y])
