import sqlite3

class database_manager:
    def __init__(self, db_name='tetris.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY NOT NULL,
                password TEXT NOT NULL,
                high_score NUMBER DEFAULT 0 NOT NULL
            )
        ''')

        # Commit the changes
        self.conn.commit()