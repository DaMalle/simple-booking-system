# built-in imports
import tkinter as tk

# local imports
import booking.logic.user_logic as user_logic

class LoginPage(tk.Frame):
    """A frame where you can login to the booking system"""
    def __init__(self, main=None):
        super().__init__(main)
        self.main = main
        self.draw_widgets()

    def draw_widgets(self): #! change variable names
        self.user_entry = tk.Entry(self)
        self.user_entry.grid(column=1, row=1, pady=(50,0))
        self.user_label = tk.Label(self, text="Username")
        self.user_label.grid(column=0, row=1, padx=(50,0), pady=(50,0))

        self.pass_entry = tk.Entry(self)
        self.pass_entry.grid(column=1, row=2, pady=(0,50))
        self.pass_label = tk.Label(self, text="Password")
        self.pass_label.grid(column=0, row=2, padx=(50,0), pady=(0,50))

        self.login_button = tk.Button(self,text="Login", command=self.login)
        self.login_button.grid(column=2, row=2, padx=(0,50), pady=(0,50))

    def login(self):
        user_logic.verify_user(self.user_entry.get(), self.pass_entry.get())

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destoy()
