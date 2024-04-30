import unittest
from unittest.mock import patch
from classes.database import database_manager
from classes.user import user
from classes.account_verification import account_verification
from classes.stub_account_verification import stub_account_verification

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.db = database_manager()
        self.account = account_verification()
        self.stub_account = stub_account_verification()

    def test_redirect_to_sign_up(self):
        with patch("classes.account_verification.account_verification.Sign_up") as function:
            self.account.redirect_to_sign_up_or_log_in(choice="Sign_up", back_message="back")
            self.assertTrue(function.called)

    def test_redirect_to_log_in(self):
        with patch("classes.account_verification.account_verification.Log_in") as function:
            self.account.redirect_to_sign_up_or_log_in(choice="Log_in", back_message="back")
            self.assertTrue(function.called)

    def test_sign_up_adds_user(self):
        self.db.delete_user("test_name")
        self.assertEqual(len(self.db.get_user_by_username("test_name")), 0)

        with patch('builtins.input') as _input:
             _input.side_effect = ["test_name", "test_password"]
             with patch("classes.account_verification.account_verification.check_valid", return_value = self.stub_account.check_valid({"username": "test_name", "password": "test_password"})) as check_valid_stub:
                self.account.Sign_up("back")
                self.assertEqual(self.db.get_user_by_username("test_name"), ("test_name", "test_password", 0))

    def test_sign_up_back(self):
        with patch('builtins.input') as _input:
             _input.side_effect = ["back"]
             with patch("classes.account_verification.account_verification.check_valid", return_value = self.stub_account.check_valid(None)) as check_valid_stub:
                self.assertEqual(self.account.Sign_up("back"), None)

    def test_log_in_returns_user(self):
        side_effects = ["test_name", "test_password"]
        self.db.insert_user(user("test_name", "test_password", 0))

        with patch('builtins.input') as _input:
            _input.side_effect = ["test_name", "test_password"]
            with patch("classes.account_verification.account_verification.check_valid", return_value = self.stub_account.check_valid({"username": "test_name", "password": "test_password"})) as check_valid_stub:
                self.assertEqual(self.account.Log_in("back").username, "test_name")
                self.assertEqual(self.account.Log_in("back").password, "test_password")
                self.assertEqual(self.account.Log_in("back").highscore, 0)

    def test_log_in_back(self):
        with patch('builtins.input') as _input:
            _input.side_effect = ["back"]
            with patch("classes.account_verification.account_verification.check_valid", return_value = self.stub_account.check_valid(None)) as check_valid_stub:
                self.assertEqual(self.account.Log_in("back"), None)

    def test_check_unique_name_true(self):
        with patch("classes.database.database_manager.get_users", return_value = [('test_name', 'test_password', 0), ('example', 'pass', 0)]) as get_users_stub:
            self.assertEqual(self.account.check_unique_name(new_name="new_name", return_dict=None), None)

    def test_check_unique_name_false(self):
        with patch("classes.database.database_manager.get_users", return_value = [('test_name', 'test_password', 0), ('example', 'pass', 0)]) as get_users_stub:
            self.assertEqual(self.account.check_unique_name(new_name="test_name", return_dict=None), False)

    def test_check_password_valid_true(self):
        self.assertEqual(self.account.check_password_valid(new_password="test_password", return_dict=None), None)

    def test_check_password_valid_false(self):
        self.assertEqual(self.account.check_password_valid(new_password="", return_dict=None), False)

    def test_check_name_exists_true(self):
        with patch("classes.database.database_manager.get_users", return_value = [('test_name', 'test_password', 0), ('example', 'pass', 0)]) as get_users_stub:
            self.assertEqual(self.account.check_name_exists(new_name="test_name", return_dict=None), None)

    def test_check_name_exists_false(self):
        with patch("classes.database.database_manager.get_users", return_value = [('test_name', 'test_password', 0), ('example', 'pass', 0)]) as get_users_stub:
            self.assertEqual(self.account.check_name_exists(new_name="new_name", return_dict=None), False)

    def test_check_password_match_true(self):
        with patch("classes.database.database_manager.get_user_by_username", return_value = ('test_name', 'test_password', 0)) as get_user_by_name_stub:
            self.assertEqual(self.account.check_password_match(new_password="test_password", return_dict={"username":None}), None)

    def test_check_password_match_false(self):
        with patch("classes.database.database_manager.get_user_by_username", return_value = ('test_name', 'test_password', 0)) as get_user_by_name_stub:
            self.assertEqual(self.account.check_password_match(new_password="bad_password", return_dict={"username":None}), False)


if __name__ == '__main__':
    unittest.main()