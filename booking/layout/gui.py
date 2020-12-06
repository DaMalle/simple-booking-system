#! /usr/bin/env python3

# built-in imports
import tkinter as tk

# local imports
from booking.layout.login_page import LoginPage
from booking.layout.components.header import Header


class MainApp(tk.Frame):
    def __init__(self, main):
        super().__init__(main)
        self.main = main
        self.draw_widgets()
        self.main.columnconfigure(0, weight=1)

    def draw_widgets(self):
        Header(self.main).grid(column=0, row=0, sticky="NEW")
        LoginPage(self.main).grid(column=0, row=1)


if __name__ == '__main__':
    root = tk.Tk()
    MainApp(root)
    root.mainloop()
    
