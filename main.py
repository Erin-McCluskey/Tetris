from classes.account_verification import account_verification
from classes.database import database_manager
db = database_manager()
account = account_verification()

def main():
    current_user = account.choose_sign_up_or_log_in()

main()