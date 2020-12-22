import unittest
from booking.logic.user_logic import UserLogic
from booking.data.user_data import UserData
class db_test(unittest.TestCase):

    def setUp(self):
        UserLogic().register_member("test@email.com", "Sherlock", "Holmes", "mystery123")

    def test_register_mem(self):
        self.assertEqual(UserData().get_user("test@email.com")[0], "test@email.com")

    def test_register(self):
        self.assertEqual(UserData().get_user("test@email.com")[0], "test@email.com")

    def tearDown(self):
        UserData.delete_user(self, "test@email.com")

if __name__ == "__main__":
    unittest.main()