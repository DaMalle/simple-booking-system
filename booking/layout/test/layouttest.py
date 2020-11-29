from booking.layout.login_page import LoginPage
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    LoginPage(main=root).grid(column=1,row=1)
    root.mainloop()

