import random
import pyperclip
import time
from credential import Credential
from user import User

def create_user(login_name, pin):
    """
    Function to create a new user
    """
    new_user = User(login_name,pin)
    return new_user

def save_user(user):
    """
    Function to save user details
    """
    user.save_user()

def create_credential(platform,username,email,password):
    """
    Function to create a new credential
    """
    new_credential = Credential(platform,username,email,password)
    return new_credential


def save_credential(credential):
    """
    Function to save credential
    """
    credential.save_credential()


def delete_credential(credential):
    """
    Function to delete a credential
    """
    credential.delete_credential()


def find_credentials(platform):
    """
    Function that finds a credential by platform name and returns the credentials
    """
    return Credential.find_by_platform(platform)


def check_existing_credential(platform):
    """
    Function that check if a credential exists with that number and return a Boolean
    """
    return Credential.credential_exists(platform)


def display_credentials():
    """
    Function that returns all the saved credentials
    """
    return Credential.display_credentials()

def copy_password(platform):
    """
    Function which copies the password of the platform
    taken as an argument
    """
    return Credential.copy_password(platform)

def generate_password(length):
    """
    Function which generates a random password
    Args:
        the desired password length
    """
    return Credential.generate_password(length)


def main():
    print("""
                GREETINGS USER! WELCOME TO THE PASSWORD VAULT.
        """)
    print("Use the following short codes to navigate the application \n lg - Login \n su - Sign Up \n xx - Exit")
    # code = input()
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes :\n cc - create a new credential \n dc - display credentials \n fc - find a credential \n ex - exit the vault")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Credential")
            print("-"*10)

            print("Platform ....")
            platform = input()

            print("Username ...")
            username = input()

            print("Email ...")
            email = input()

            print("Would you wish to have Vault generate a password for you? Y or N")
            option = input().lower()
            if option.startswith("y"):
                print("How long would you like your password to be?")
                desired_len = int(input())
                password = generate_password(desired_len)
            else:
                print("Enter your password ...")
                password = input()

            # create and save new contact.
            save_credential(create_credential(platform,username,email,password))
            print('\n')
            print(f"New credentials for {platform} created")
            print('\n')

        elif short_code == 'dc':

            if display_credentials():
                print("Here is a list of all your credentials")
                print('\n')

                for cred in display_credentials():
                    print(f"{cred.platform} {cred.username} .....{cred.password}")
                    print('\n')
            else:
                print('\n')
                print("You dont seem to have any credentials saved yet")
                print('\n')

        elif short_code == 'fc':
            print("Enter the platform you want to search for")

            platform_search = input().lower()
            if check_existing_credential(platform_search):
                search_credential = find_credentials(platform)
                print(
                    f"""
                    Platform --- {search_credential.platform} 
                    Password --- {search_credential.password}
                    """)
                print('-' * 20)

                print(
                    f"Phone number.......{search_credential.username}")
                print(
                    f"Email address.......{search_credential.password}")
            else:
                print("The credential does not exist")
        
        elif short_code == "cp":
            print("Enter the platform whose password you would like copied")
            platform_find = input()
            print("Loading...")
            if check_existing_credential(platform_find):
                search_credential = find_credentials(platform_find)
                pyperclip.copy(search_credential.password)
                time.sleep(1.5)
                print("\n")
                print("Password for {} has been copied!".format(search_credential.platform))

            else:
                print("The platform you entered does not exist")

        elif short_code == "ex":
            print(f"Have a nice day {user_name}")
            break
        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()