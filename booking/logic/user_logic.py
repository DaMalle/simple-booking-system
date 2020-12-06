#! /usr/bin/env python3

# Local imports
from booking.data.user_data import UserData


class UserLogic:
    def __init__(self):
        self.UserData = UserData()

    def register_member(self, email, first_name, last_name, password):
        return self.register(email, first_name, last_name, password, 'Member')

    def register(self, email, first_name, last_name, password, role):
        if self.verify_user(email) == False:
            self.UserData.add(email, first_name, last_name, password, role)
            return (True, (email, first_name, last_name, password))
        else:
            return (False, 'email')

    def login(self, email, password):
        if self.verify_user(email):
            if self.UserData.get_password(email) == (password,):
                return (True, self.UserData.get_user(email))
            else:
                return (False, 'password')
        else:
            return (False, 'email')

    def verify_user(self, email):
        if (email,) in self.UserData.get_all_emails():
            return True