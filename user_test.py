import unittest
from user import User
from credentials import Credentials

class UserTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User("user100", "1100")
    
    def test_init(self):
        self.assertEqual(self.new_user.login_name, "user100")
        self.assertEqual(self.new_user.pin, "1100")

    def test_create_new_user(self):
        self.new_user.create_new_user(Credentials("Instagram","d@test","user100","12pass"))
        self.assertEqual(len(User.account_creds),1)
        # print(User.account_creds)

    def test_multiple_users(self):
        self.second_user = User("collins","2342")
        self.second_user.create_new_user(Credentials("Facebook","collo@l.l","collins","lastpass"))
        self.assertEqual(len(User.account_creds),2)
        # print(User.account_creds)

    def test_pin_change(self):
        self.new_user.create_new_user(Credentials("Instagram","d@test","user100","12pass"))
        self.new_user.change_pin("100","1234")
        self.assertEqual(self.new_user.pin,"1234")
    
    # def tearDown(self):
    #     User.account_creds = []

if __name__ == "__main__":
    unittest.main()