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

    def save_user(self):
        User.user_list.append(self)

    @classmethod
    def user_auth(cls,name,pin):
        for user in cls.user_list:
            if user.login_name == name and user.pin == pin:
                return True
        return False

    @classmethod
    def view_users(cls):
        return cls.user_list