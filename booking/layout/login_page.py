# built-in imports
import tkinter as tk

# local imports
from booking.logic.user_logic import verify_user
from booking.layout.registration_page import RegistrationPage

class LoginPage(tk.Frame):
    """A frame where you can login to the booking system"""
    def __init__(self, main):
        super().__init__(main)
        self.main = main
        self.draw_widgets()

    def draw_widgets(self):
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(column=1, row=1, pady=(50,0))
        self.username_label = tk.Label(self, text="Username")
        self.username_label.grid(column=0, row=1, padx=(50,0), pady=(50,0))

        self.password_entry = tk.Entry(self)
        self.password_entry.grid(column=1, row=2, pady=(0,0))
        self.password_label = tk.Label(self, text="Password")
        self.password_label.grid(column=0, row=2, padx=(50,0), pady=(0,0))

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.grid(column=2, row=2, padx=(4,0), pady=(0,0))

        self.no_user_label = tk.Label(self, text="Har du ikke en bruger så opret én!")
        self.no_user_label.grid(column=1, row=3, pady=(0,50))
        self.no_user_button = tk.Button(self, text="Opret en bruger", command=self.open_registration_page)
        self.no_user_button.grid(column=2, row=3, padx=(0,50), pady=(0,50))

    def login(self):
        verify_user(self.username_entry.get(), self.password_entry.get())

    def open_registration_page(self):
        self.clear_frame()
        RegistrationPage(self).grid(column=1,row=1)

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
