#local import
from booking.logic.user_logic import register_user
#built-in imports
import tkinter as tk
class RegistrationPage(tk.Frame):
    """A frame in which you can register a new user in the booking system"""
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
        self.password_entry.grid(column=1, row=2, pady=(0,50))
        self.password_label = tk.Label(self, text="Password")
        self.password_label.grid(column=0, row=2, padx=(50,0), pady=(0,50))

        self.register_button = tk.Button(self, text="Opret", command=self.register())
        self.register_button.grid(column=2, row=2, padx=(0, 50), pady=(0, 50))

    def register(self):
        register_user(self.username_entry.get(), self.password_entry.get())

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destoy()