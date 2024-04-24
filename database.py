import sqlite3

class database_manager:
    def __init__(self, db_name='tetris.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY NOT NULL,
                password TEXT NOT NULL,
                highscore NUMBER DEFAULT 0 NOT NULL
            )
        ''')

        # Commit the changes
        self.conn.commit()

    def tear_down(self):
        self.conn.close()

    def get_users(self):
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        return users

    def get_user_by_username(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = self.cursor.fetchall()
        if len(user) != 0:
            return user[0]
        else:
            return user

    def insert_user(self, user):
        self.cursor.execute("INSERT INTO users (username, password, highscore) VALUES (?, ?, ?)", (user.username, user.password, user.highscore))
        self.conn.commit()