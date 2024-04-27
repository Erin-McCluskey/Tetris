import inquirer
from classes.database import database_manager
from classes.user import user
from classes.account_verification_abstract import account_verification_abtract
db = database_manager()

class account_verification(account_verification_abtract):
    def __init__(self):
        pass

    def check_password_valid(self, new_password, return_dict):
        if len(new_password)==0:
            print("You must enter a password. This password cannot be blank. Enter a new password.")
            return False

    def check_unique_name(self, new_name, return_dict):
        users = db.get_users()
        usernames = [user[0] for user in users]
        if new_name in usernames:
            print("Username already exists. Choose a new username or switch to log in by entering back.")
            return False

    def check_name_exists(self, new_name, return_dict):
        users = db.get_users()
        usernames = [user[0] for user in users]
        if new_name not in usernames:
            print("Username does not exist. Re-enter a username or switch to Sign up by entering back.")
            return False

    def check_password_match(self, new_password, return_dict):
        if "username" in return_dict.keys():
            current_user = db.get_user_by_username(return_dict["username"])

            if current_user[1] != new_password:
                print("Username and password do not match. Re-enter password.")
                return False

    def check_valid(self, input_dict):
        return_dict = {}
        for input_type, function in input_dict.items():
            valid = False
            while valid == False:
                user_input = str(input(f"Enter a {input_type}: ")).lower()
                if user_input == "back":
                    self.choose_sign_up_or_log_in()
                    return
                valid = function(user_input, return_dict)

            return_dict.update({input_type : user_input})
        return return_dict

    def Sign_up(self, back_message):
        print(back_message)

        input_dict = {"username" : self.check_unique_name, "password": self.check_password_valid}
        returned_dict = self.check_valid(input_dict)
        if returned_dict != None:
            new_user = user(returned_dict["username"], returned_dict["password"])
            db.insert_user(new_user)
            return new_user
        else:
            return None

    def Log_in(self, back_message):
        print(back_message)

        input_dict = {"username" : self.check_name_exists, "password": self.check_password_match}
        returned_dict = self.check_valid(input_dict)
        if returned_dict != None:
            new_user = db.get_user_by_username(returned_dict["username"])
            return user(new_user[0], new_user[1], new_user[2])
        else:
            return None

    def redirect_to_sign_up_or_log_in(self, choice, back_message):
        if choice == "Sign_up":
            current_user = self.Sign_up(back_message)
        else:
            current_user = self.Log_in(back_message)
        return current_user

    def choose_sign_up_or_log_in(self):
        back_message = "Enter back if you would like to return to the previous menu"

        account_verification = [
        inquirer.List('account_verification',
                        message="Would you like to sign up or log in?",
                        choices=['Sign_up', 'Log_in'],
                    ),
        ]
        redirect = inquirer.prompt(account_verification)

        current_user = self.redirect_to_sign_up_or_log_in(redirect['account_verification'], back_message)

        if current_user != None:
            return current_user