class User:
    def __init__(self, username):
        self.username = username
        self.bank_account = ''
    
    def get_username(self):
        return self.username
    
    def set_account(self, account):
        self.bank_account = account

    def get_history(self):
        return self.bank_account.history
