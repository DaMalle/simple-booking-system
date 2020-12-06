#! /usr/bin/env python3

# built-in imports
import tkinter as tk

# local imports
from booking.logic.user_logic import UserLogic
from booking.layout.components.header import Header

class RegistrationPage(tk.Frame):
    """A frame in which you can register a new user in the booking system"""
    def __init__(self, main):
        super().__init__(main)
        self.main = main
        self.main.title('Registrer')
        self.draw_widgets()

    def draw_widgets(self):
        #Header(self).grid()

        #The entry in which the user writes their first name
        self.first_name_entry = tk.Entry(self)
        self.first_name_entry.grid(column=1, row=1, pady=(50,0))
        self.first_name_label = tk.Label(self, text="Fornavn")
        self.first_name_label.grid(column=0, row=1, padx=(100,0), pady=(50,0))

        ##The entry in which the user writes their last name
        self.last_name_entry = tk.Entry(self)
        self.last_name_entry.grid(column=1, row=2, pady=(0,0))
        self.last_name_label = tk.Label(self, text="Efternavn")
        self.last_name_label.grid(column=0, row=2, padx=(100,0), pady=(0,0))

        # The entry in which the user writes their email
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(column=1, row=3, pady=(0,0))
        self.email_label = tk.Label(self, text="E-mail")
        self.email_label.grid(column=0, row=3, padx=(100,0), pady=(0,0))

        # The entry in which the user writes their password
        self.password_entry = tk.Entry(self)
        self.password_entry.grid(column=1, row=4, pady=(0,0))
        self.password_label = tk.Label(self, text="Password")
        self.password_label.grid(column=0, row=4, padx=(100,0), pady=(0,0))

        # Once clicked a new user will be created with the credentials written by the user
        self.register_button = tk.Button(self, text="Opret bruger", command=self.new_user)
        self.register_button.grid(column=2, row=4, padx=(0,0), pady=(0,0))

        self.cancel_button = tk.Button(self, text="Annullér", command=self.cancel)
        self.cancel_button.grid(column=3, row=4, padx=(0,0))

    def cancel(self):
        self.destroy()

    def new_user(self):
        # The new user is registered
        UserLogic().register_member(self.email_entry.get(),
                                  self.firstname_entry.get(),
                                  self.lastname_entry.get(),
                                  self.password_entry.get()
                                  )
        # The page is destroyed and returns the previous page
        self.destroy()