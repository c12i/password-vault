import random
import string

class Credentials:
    """
    Credential class

    Args:
    platform_name: The name of the plaform of which the user has crredentials.(str)
    email : The email the user uses to sign in or make the account.(str)
    number: The username of the user.(int)
    password : The password of the user for the given platform.(str)
    """

    credential_list = []

    def __init__(self, platform_name, email, username, password):
        self.platform_name = platform_name
        self.email = email
        self.username = username
        self.password = password

    def add_credential(self):
        """
        this method appends a new credential to the credential_list
        """
        Credentials.credential_list.append(self)
    
    def delete_credential(self):
        """
        this method removes a credential from the credential list
        """
        Credentials.credential_list.remove(self)

    def generate_password(self, length):
        """
        this method uses the string method to generate a password of random digits and letters
        the length of the password is determined by the length passed in the function's parameter 
        """
        letters_and_numbers = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_numbers) for i in range(length))

    @classmethod
    def find_credential(cls, name):
        """
        this class metod finds user credentials based on the query provided which
        is matched against the platform name.(str)
        """
        for cred in Credentials.credential_list:
            if cred.platform_name == name:
                return cred
    
    @classmethod
    def in_list(cls, name):
        """
        this method checks if a particlar platform has it's credentials saved
        """
        for cred in Credentials.credential_list:
            if cred.platform_name == name:
                return True
        return False

    @classmethod
    def show_credentials(cls):
        """
        this class method returns the array of credentials
        """

        return cls.credential_list
