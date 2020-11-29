class login_window: #
    def __init__(self):
        self.root = Tk()
        self.user_entry = Entry(self.root)
        self.user_entry.grid(column=1, row=1, pady=(50,0))
        self.user_label = Label(self.root, text="Username")
        self.user_label.grid(column=0, row=1, padx=(50,0), pady=(50,0))

        self.pass_entry = Entry(self.root)
        self.pass_entry.grid(column=1, row=2, pady=(0,50))
        self.pass_label = Label(self.root, text="Password")
        self.pass_label.grid(column=0, row=2, padx=(50,0), pady=(0,50))

        self.login_button = Button(self.root,text="Login", command=self.login)
        self.login_button.grid(column=2, row=2, padx=(0,50), pady=(0,50))

        self.root.mainloop()