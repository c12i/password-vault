import unittest
from user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User("user100", "1100")
    
    def test_init(self):
        self.assertEqual(self.new_user.login_name, "user100")
        self.assertEqual(self.new_user.pin, "1100")
    
    # def tearDown(self):
    #     User.account_creds = []

if __name__ == "__main__":
    unittest.main()