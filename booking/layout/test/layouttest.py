from booking.layout.login_page import LoginPage
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    LoginPage(main=root).grid(column=1, row=1)
    header = tk.Label(root, text="   Aarhus Golfclub    ", bg="#af2222", fg="#ffffff", font=("Roboto Medium", 30, "bold"))
    header.grid(column=1, row=0, columnspan=3)
    root.mainloop()

