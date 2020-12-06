#! /usr/bin/env python3

# built-in imports
import tkinter as tk

# local imports
from booking.layout.login_page import LoginPage
from booking.layout.registration_page import RegistrationPage


class MainApp(tk.Frame):
    def __init__(self, main):
        super().__init__(main)
        self.main = main
        self.draw_widgets()

    def draw_widgets(self):
        LoginPage(self.main).grid(column=0, row=1)


if __name__ == '__main__':
    root = tk.Tk()
    MainApp(root)
    root.mainloop()
    
