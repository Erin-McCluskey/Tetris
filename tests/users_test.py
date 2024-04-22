import unittest

from user import user

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = user('test_user', 'test_password')

    def test_get_username(self):
        # Check that the username is correct
        self.assertEqual(self.user.get_username(), 'test_user')

    def test_compare_password(self):
        # Checks that the password is correct
        self.assertEqual(self.user.get_password(),'test_password')
        self.assertNotEqual(self.user.get_password(),'wrong_password')

    def test_get_highscore(self):
        # Checks that the initial highscore is correct
        self.assertEqual(self.user.get_highscore(), 0)

    def test_update_highscore(self):
        # Checks that the highscore gets updated
        self.assertEqual(self.user.update_highscore(500), 500)

    def test_set_current_user(self):
        self.user.set_current_user(self.user)
        self.assertEqual(self.user.get_current_user(), self.user)

if __name__ == '__main__':
    unittest.main()