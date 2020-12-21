from booking.logic.user_logic import UserLogic

"""class TestCase:
    def __init__(self):
        self.userlogic = UserLogic

    def test_Uregister(self):
        self.userlogic.register(self, 'email', 'first_name', 'last_name', 'password', 'member')"""

UserLogic().register('email', 'first_name', 'last_name', 'password', 'member')
from booking.data.user_data import UserData

print(UserLogic().verify_user('email'))
UserData().add('email', 'first_name', 'last_name', 'password', 'member')

print(UserLogic().verify_user('email'))