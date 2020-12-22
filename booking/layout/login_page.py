#! /usr/bin/env python3

# built-in imports
import tkinter as tk

# local imports
from booking.logic.user_logic import UserLogic
from booking.layout.registration_page import RegistrationPage
from booking.layout.booking_page import BookingPage
from booking.layout.reservation_page import ReservationPage

class LoginPage(tk.Frame): # The first window the user is greeted with
    """A frame where you can login to the booking system"""
    def __init__(self, main):
        super().__init__(main)
        self.main = main
        self.main.title('Login')
        self.draw_widgets()

    def draw_widgets(self):
        # The label that displays text in case of a failed log-in
        self.error_label = tk.Label(self, text='', fg='red2')
        self.error_label.grid(column=1, columnspan=1, row=4, pady=(0,50))

        # The entry in which the user writes their email
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(column=1, row=1, sticky="W", pady=(50,0))
        self.email_label = tk.Label(self, text="E-mail")
        self.email_label.grid(column=0, row=1, padx=(50,0), pady=(50,0))

        # The entry in which the user writes their password
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.grid(column=1, row=2, sticky="W", pady=(0,0))
        self.password_label = tk.Label(self, text="Password")
        self.password_label.grid(column=0, row=2, padx=(50,0), pady=(0,0))

        # The login button, once pressed an attempt at loging-in will be made
        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.grid(column=2, row=2, padx=(4,0), pady=(0,0))

        # If the user doesn't have a user it can be created by pressing this button
        self.no_user_label = tk.Label(self, text="Har du ikke en bruger så opret én!")
        self.no_user_label.grid(column=1, row=3, pady=(0,0))
        self.no_user_button = tk.Button(self, text="Opret en bruger", command=self.open_registration_page)
        self.no_user_button.grid(column=2, row=3, padx=(0,50), pady=(0,0))

    def login(self):
        # If the login attempt is successfull the user will be taken to the BookingPage
        if UserLogic().login(self.email_entry.get(), self.password_entry.get())[0]:
            self.error_label.configure(text='')
            BookingPage(self.main, self.email_entry.get()).grid(column=0, row=1, sticky="NEWS")

        else: # If the attempt is unsuccessfull an error will be transmitted to the user
            if UserLogic().login(self.email_entry.get(), self.password_entry.get())[1] == 'email':
                self.error_label.configure(text='E-mailen er ikke en gyldig bruger')

            elif UserLogic().login(self.email_entry.get(), self.password_entry.get())[1] == 'password':
                self.error_label.configure(text='passwordet er ikke gyldigt')
                
            else:
                print(UserLogic().login(self.email_entry.get(), self.password_entry.get())[1])

    def open_registration_page(self): # The user is taken to the RegistrationPage
        self.clear_loginpage() # The labels and entries are cleared
        RegistrationPage(self.main).grid(column=0, row=1) # The new page is created on top of the current page

    def clear_loginpage(self):
        self.error_label.configure(text='')
        self.email_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')