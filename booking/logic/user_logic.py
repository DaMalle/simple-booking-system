#! /usr/bin/env python3

# Local imports
from booking.data.user_data import UserData


class UserLogic:
    def __init__(self):
        self.UserData = UserData()

    def register(self, email, first_name, last_name, password, role):
        pass

    def tester(self, email):
        if self.verify_email(email):
            print(f'{email} is used')
        else:
            print(f'{email} is not used')

    def verify_email(self, email): #verify if a user exsists in the system
        self.emails = [email for t in self.UserData.get_all_emails() for email in t]
        if email in self.emails:
            return True

test = UserLogic()
test.tester('Mallerupz@gmail.com')
test.tester('test@mail.dk')