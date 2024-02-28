class User:
    def __init__(self, username):
        self.username = username
        self._password = ''

    def set_password(self, password):
        self._password = password

    def check_password(self, password):
        if password == self._password:
            return True
        else:
            return False

    def get_username(self):
        return self.username