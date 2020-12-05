#! /usr/bin/env python3

# built-in imports
import tkinter as tk

# local imports
from booking.logic.user_logic import register_user


class RegistrationPage(tk.Frame):
    """A frame in which you can register a new user in the booking system"""
    def __init__(self, main):
        super().__init__(main)
        self.main = main
        self.main.title('Registrer')
        self.draw_widgets()

    def draw_widgets(self):
        self.fornavn_entry = tk.Entry(self)
        self.fornavn_entry.grid(column=1, row=1, pady=(0,0))
        self.fornavn_label = tk.Label(self, text="Fornavn")
        self.fornavn_label.grid(column=0, row=1, padx=(50,0), pady=(0,0))

        self.efternavn_entry = tk.Entry(self)
        self.efternavn_entry.grid(column=1, row=2, pady=(0,0))
        self.efternavn_label = tk.Label(self, text="Efternavn")
        self.efternavn_label.grid(column=0, row=2, padx=(50,0), pady=(0,0))

        self.email_entry = tk.Entry(self)
        self.email_entry.grid(column=1, row=3, pady=(0,0))
        self.email_label = tk.Label(self, text="E-mail")
        self.email_label.grid(column=0, row=3, padx=(50,0), pady=(0,0))

        self.password_entry = tk.Entry(self)
        self.password_entry.grid(column=1, row=4, pady=(0,0))
        self.password_label = tk.Label(self, text="Password")
        self.password_label.grid(column=0, row=4, padx=(50,0), pady=(0,0))

        self.register_button = tk.Button(self, text="Opret", command=self.register)
        self.register_button.grid(column=2, row=4, padx=(0, 50), pady=(0, 0))

    def register(self):
        register_user(self.email_entry.get(), self.password_entry.get())
        self.destroy()