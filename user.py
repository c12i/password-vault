from credentials import Credentials

class User:
    """
    User class

    Args:
    login_name: To sign into the application.(str)
    pin : To sign into the application.(str)
    """

    account_creds = [] # this is a list of dictionaries; with each dictionary key as the login_name and the value as the credentials list

    def __init__(self, login_name, pin):
        self.login_name = login_name
        self.pin = pin

    def create_new_user(self, creds):#### might fail
        creds = {self.login_name: Credentials.credential_list}
        User.account_creds.append(creds)

    def delete_user(self, creds): #### might fail
        creds = {self.login_name: Credentials.credential_list}
        User.account_creds.remove(creds)

    def user_signin(self, username, password):
        if self.pin == self.pin and self.login_name == username:
            return True
        else:
            return False

    @classmethod
    def view_users(cls):
        return User.account_creds

    def change_pin(self, oldpin, newpin):
        if self.pin == oldpin:
            self.pin = newpin
        # else:
        #     return "The pins do not match"