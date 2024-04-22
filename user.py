class user:
    _all_users = []

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.highscore = 0

        self._all_users.append(self)

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_highscore(self):
        return self.highscore

    def update_highscore(self, new_score):
        self.highscore = new_score
        return self.highscore

    def set_current_user(self, user):
         self.current_user = user

    def get_current_user(self):
         return self.current_user