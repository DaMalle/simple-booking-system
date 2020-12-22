import unittest 
from booking.data.user_data import UserData

class db_test(unittest.TestCase):

    def setUp(self):
        UserData().add("test@email.com", "Sherlock", "Holmes", "mystery123", "Member")

    def test_email(self):
        self.assertEqual(UserData().get_user("test@email.com")[0], "test@email.com")

    def test_firstName(self):
        self.assertEqual(UserData().get_user("test@email.com")[1], "Sherlock")

    def test_lastName(self):
        self.assertEqual(UserData().get_user("test@email.com")[2], "Holmes")

    def test_password(self):
        self.assertEqual(UserData().get_user("test@email.com")[3], "mystery123")

    def test_role(self):
        self.assertEqual(UserData().get_user("test@email.com")[4], "Member")

    def tearDown(self):
        UserData.delete_user(self, "test@email.com")

if __name__ == "__main__":
    unittest.main()
