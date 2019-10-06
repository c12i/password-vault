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

def authenticate_user(username,password):
    return User.user_auth(username,password)

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

                 _   |~  _
                [_]--'--[_]
                |'|""`""|'|
                | | /^\ | |
                |_|_|I|_|_|

 $$\    $$\  $$$$$$\  $$\   $$\ $$\    $$$$$$$$\ 
$$ |   $$ |$$  __$$\ $$ |  $$ |$$ |   \__$$  __|
$$ |   $$ |$$ /  $$ |$$ |  $$ |$$ |      $$ |   
\$$\  $$  |$$$$$$$$ |$$ |  $$ |$$ |      $$ |   
 \$$\$$  / $$  __$$ |$$ |  $$ |$$ |      $$ |   
  \$$$  /  $$ |  $$ |$$ |  $$ |$$ |      $$ |   
   \$  /   $$ |  $$ |\$$$$$$  |$$$$$$$$\ $$ |   
    \_/    \__|  \__| \______/ \________|\__|   

    GREETINGS USER, WELCOME TO THE PASSWORD VAULT                                         
                
        """)
    while True:
        print("""
        Use the following short codes to manage your account 
            1. 'su' - Sign Up
            2. 'xx' - Close app
            """)
        print("What would you like to do?")
        code = input().lower()
        if code == "su":
            print("Enter your username")
            login_name = input()
            print("Enter your pin")
            login_pin = input()
            print("Loading ...")
            time.sleep(1.5)
            print("\n")
            print("Congratulations, your account has been created")
            print("Sign into your new account")
            sign_in_name = input("Enter your username: ")
            sign_in_pin = input("Enter your pin: ")
            save_user(create_user(login_name,login_pin))
            authenticate_user(sign_in_name,sign_in_pin)
            print("Please wait...")
            time.sleep(1.5)
            print("Successfuly logged in")  
            print("\n")
            pass
            while True:
                if authenticate_user(sign_in_name,sign_in_pin):
                    ####
                    print(
                        """
                       O===[====================-
                            
                        WELCOME TO YOUR VAULT:
                        Use the following commands to navigate the application:

                            1. 'cc' - enables you to create an a credential
                            2. 'dc' - displays the credentials you have saved
                            3. 'cp' - copies the password of a given credential
                            4. 'fc' - helps you find a credential by its platform name
                            5. 'ex' - logs you out
                            6. 'help' - helps a user around the app
                        """)
                    print(f"At your service {sign_in_name}, what task would you like to perform?")
                    key_word = input().lower()

                    if key_word == 'cc':
                        print("New Credential")
                        print("-"*10)

                        platform = input("Input the platform: ")
                        print("_"*50)
                        username = input("Input your username: ")
                        print("_"*50)
                        email = input("Input your email: ")
                        print("_"*50)
                        option = input("Would you wish to have Vault generate a password for you? Y or N ").lower()
                        if option.startswith("y"):
                            print("_"*50)
                            print("How long would you like your password to be?")
                            desired_len = int(input())
                            password = generate_password(desired_len)
                        else:
                            print("_"*50)
                            print("Enter your password ...")
                            password = input()

                        # create and save new contact.
                        save_credential(create_credential(platform,username,email,password))
                        print('\n')
                        print(f"NEW CREDENTIALS FOR {platform} CREATED!")
                        print("_"*50)
                        print('\n')

                    elif key_word == 'dc':

                        if display_credentials():
                            print("HERE ARE YOUR CREDENTIALS")
                            print("_"*50)
                            print('\n')

                            for cred in display_credentials():
                                print(
                                    f"""
                                 --------------------------------------------------
                                            Platform --- {cred.platform}               
                                            Username --- {cred.username}               
                                            Email    --- {cred.email}                  
                                            Password --- {cred.password}               
                                 --------------------------------------------------
                                """
                                )
                                print('\n')
                        else:
                            print('\n')
                            print("You dont seem to have any credentials saved yet")
                            print("_"*50)
                            print('\n')

                    elif key_word == 'fc':
                        print("Enter the platform you want to search for")
                        print("_"*50)
                        platform_search = input().lower()
                        if check_existing_credential(platform_search):
                            search_credential = find_credentials(platform)
                            print(
                                f"""
                                 -------------------------------------------------------
                                        Platform --- {search_credential.platform}               
                                        Username --- {search_credential.username}               
                                        Email    --- {search_credential.email}                  
                                        Password --- {search_credential.password}               
                                 -------------------------------------------------------
                                """)
                            print("_"*50)
                        else:
                            print("The credential does not exist")
                    
                    elif key_word == "cp":
                        print("Enter the platform whose password you would like copied")
                        platform_find = input()
                        print("Loading...")
                        if check_existing_credential(platform_find):
                            search_credential = find_credentials(platform_find)
                            pyperclip.copy(search_credential.password)
                            time.sleep(1.5)
                            print("\n")
                            print("Password for {} has been copied!".format(search_credential.platform))
                            print("_"*50)

                        else:
                            print("The platform you entered does not exist")
                            print("_"*50)

                    elif key_word == "ex":
                        print(f"Have a nice day {login_name}")
                        print("_"*50)
                        break

                    elif key_word == "help":
                        print(
                        """                       
                        SORRY TO HERE YOU'RE STUCK
                        

                        """)

                    else:
                        print("You entered an unknown keyword. Please use the provided keywords. Type '-help' if you're stuck")
                        print("_"*50)

                else:
                    print("Oops, you entered the wrong username/pin, we have to do this again :(")
                    print("_"*50)
                    break
            
        elif code == "xx":
            print(
            """
$$$$$$\   $$$$$$\   $$$$$$\  $$$$$$$\  $$$$$$$\ $$\     $$\ $$$$$$$$\ 
$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\\$$\   $$  |$$  _____|
$$ /  \__|$$ /  $$ |$$ /  $$ |$$ |  $$ |$$ |  $$ |\$$\ $$  / $$ |      
$$ |$$$$\ $$ |  $$ |$$ |  $$ |$$ |  $$ |$$$$$$$\ | \$$$$  /  $$$$$\    
$$ |\_$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$  __$$\   \$$  /   $$  __|   
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |   $$ |    $$ |      
\$$$$$$  | $$$$$$  | $$$$$$  |$$$$$$$  |$$$$$$$  |   $$ |    $$$$$$$$\ 
 \______/  \______/  \______/ \_______/ \_______/    \__|    \________|
                                                                      
            """)
            break

        else:
            print("You entered an unknown short code, please try again")
        
if __name__ == '__main__':
    main()