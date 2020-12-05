#! /usr/bin/env python3

# Local imports
from booking.data.user_data import UserData


class UserLogic:
    def __init__(self):
        self.UserData = UserData()

    def register(self, email, first_name, last_name, password, role):
        if self.verify_user(email) != True:
            self.UserData.add(email, first_name, last_name, password, role)

    def login(self, email, password):
        if self.verify_user(email):
            if password == self.get_password(email):
                print('login')

    def verify_user(self, email): #verify if a user exsists in the system
        self.emails = [email for t in self.UserData.get_all_emails() for email in t]
        if email in self.emails:
            return True
    
    def get_password(self, email):
        pass