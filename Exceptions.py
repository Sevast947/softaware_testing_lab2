class WrongSecurityAnswer(Exception):
    def __init__(self, message):
        super().__init__(message)

class UserNotCreated(Exception):
    def __init__(self, message):
        super().__init__(message)

class WrongPassword(Exception):
    def __init__(self, message):
        super().__init__(message)

class InsufficientFunds(Exception):
    def __init__(self, message):
        super().__init__(message)