class User:
    def __init__(self, username):
        self.username = username
        self._password = ''
    
    def set_password(self, password):
        self._password = password
    
    def get_username(self):
        return self.username
    
    def _retrieve_password(self):
        return self._password
