import tkinter as tk

class Header(tk.Frame):

    def __init__(self, main):
        super().__init__(main)
        self.main = main
        self.config(bg="#af2222")
        self.draw_widgets()

    def draw_widgets(self):
        headertext = tk.Label(self, text="Aarhus Golfclub", bg="#af2222", fg="#ffffff", font=("Roboto Medium", 30, "bold"))
        headertext.pack()

