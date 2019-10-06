import random
import string
from credentials import Credentials
from user import User

def create_user(login, pin):
    pass

def login_to_app(login, pin):
    pass

def create_credentials(paltform, email, username, password):
    pass

def pass_gen(credential, length):
    credential.generate_password(length)

def add_credentials(credentials):
    credentials.add_credentials()

def remove_credentials(credentials):
    credentials.remove_credentials()

def find_credentials(name):
    Credentials.find_credential(name)

def check_if_credential_exists(name):
    Credentials.credential_exists(name)

def display_credentials():
    pass


