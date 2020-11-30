from booking.layout.login_page import LoginPage
from booking.layout.components.header import Header

import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.rowconfigure(0, weight=0)
    root.columnconfigure(1, weight=1000)
    LoginPage(root).grid(column=1, row=2)
    Header(root).grid(column=1, row=1, sticky="NEW")
    root.mainloop()
