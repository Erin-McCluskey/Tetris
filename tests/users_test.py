import unittest

from user import user

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = user('test_user', 'test_password')

    def test_get_username(self):
        self.assertEqual(self.user.get_username(), 'test_user')

    def test_compare_password(self):
        self.assertEqual(self.user.get_password(),'test_password')
        self.assertNotEqual(self.user.get_password(),'wrong_password')

    def test_get_highscore(self):
        self.assertEqual(self.user.get_highscore(), 0)

    def test_update_highscore(self):
        self.assertEqual(self.user.update_highscore(500), 500)

    def test_set_current_user(self):
        self.user.set_current_user(self.user)
        self.assertEqual(self.user.get_current_user(), self.user)

if __name__ == '__main__':
    unittest.main()