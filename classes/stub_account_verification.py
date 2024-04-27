from classes.account_verification_abstract import account_verification_abtract

class stub_account_verification(account_verification_abtract):
    def __init__(self):
        pass

    def check_password_valid(self, value):
        return value

    def check_unique_name(self, value):
        return value

    def check_name_exists(self, value):
        return value

    def check_password_match(self, value):
        return value

    def check_valid(self, input_dict):
        return input_dict

    def Sign_up(self, back_message):
        pass

    def Log_in(self, back_message):
        pass

