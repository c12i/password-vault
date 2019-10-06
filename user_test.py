import unittest
from user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User("user100", "1100")
    
    def test_init(self):
        self.assertEqual(self.new_user.login_name, "user100")
        self.assertEqual(self.new_user.pin, "1100")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_user_auth(self):
        self.assertTrue(self.new_user.user_auth("user100","1100"))

if __name__ == "__main__":
    unittest.main()