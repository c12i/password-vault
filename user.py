class User:
    """
    User class

    Args:
    login_name: To sign into the application.(str)
    pin : To sign into the application.(str)
    """
    user_list = []

    def __init__(self, login_name, pin):
        self.login_name = login_name
        self.pin = pin

    def user_signin(self, username, password):
        if self.pin == self.pin and self.login_name == username:
            return True
        else:
            return False

    @classmethod
    def view_users(cls):
        return User.user_list

    def change_pin(self, oldpin, newpin):
        if self.pin == oldpin:
            self.pin = newpin
        # else:
        #     return "The pins do not match"