import unittest
from booking.logic.user_logic import UserLogic
from booking.data.user_data import UserData
class db_test(unittest.TestCase):

    def test_register_member(self):
        self.assertEqual(UserLogic().register_member("test@email.com", "Sherlock", "Holmes", "mystery123"), (False, "email"))

    def test_register(self):
        self.assertEqual(UserLogic().register("test@email.com", "Sherlock", "Holmes", "mystery123", "Member"), (False, "email"))

    def test_verify_user(self):
        self.assertEqual(UserLogic().verify_user("test@email.com"), True)

if __name__ == "__main__":
    unittest.main()