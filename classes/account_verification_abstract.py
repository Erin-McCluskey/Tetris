from abc import ABC, abstractmethod

class account_verification_abtract(ABC):

    @abstractmethod
    def check_password_valid(new_password, return_dict):
        pass

    @abstractmethod
    def check_unique_name(new_name, return_dict):
        pass

    @abstractmethod
    def check_name_exists(new_name, return_dict):
        pass

    @abstractmethod
    def check_password_match(new_password, return_dict):
        pass

    @abstractmethod
    def check_valid(input_dict):
        pass
