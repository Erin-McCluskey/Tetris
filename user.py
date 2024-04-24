class user:
    def __init__(self, username, password, highscore=0):
        self.username = username
        self.password = password
        self.highscore = highscore

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_highscore(self):
        return self.highscore

    def update_highscore(self, new_score):
        self.highscore = new_score
        return self.highscore