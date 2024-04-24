import unittest

from database import database_manager
from user import user

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = database_manager(":memory:")

    def tearDown(self):
        self.db.tear_down()

    def test_insert_user(self):
        first_user = user("firstuser", "password", 0)
        self.db.insert_user(first_user)
        self.assertEqual(self.db.get_user_by_username("firstuser"), ("firstuser", "password", 0))

        second_user = user("seconduser", "pass", 40)
        self.db.insert_user(second_user)
        self.assertEqual(self.db.get_user_by_username("seconduser"), ("seconduser", "pass", 40))

    def test_get_users(self):
        users = self.db.get_users()
        self.assertEqual(len(users), 0)

        first_user = user("firstuser", "password", 0)
        self.db.insert_user(first_user)
        users = self.db.get_users()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0][0], "firstuser")

    def test_get_user_by_name(self):
        self.assertEqual(len(self.db.get_users()), 0)

        first_user = user("firstuser", "password", 0)
        self.db.insert_user(first_user)
        self.assertEqual(self.db.get_user_by_username("firstuser"), ("firstuser", "password", 0))


if __name__ == '__main__':
    unittest.main()