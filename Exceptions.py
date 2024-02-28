class ItemNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)

class NegativeInventoryError(Exception):
    def __init__(self, message):
        super().__init__(message)

class DuplicateIdError(Exception):
    def __init__(self, message):
        super().__init__(message)

class InvalidDiscountError(Exception):
    def __init__(self, message):
        super().__init__(message)

class IdNotInStockError(Exception):
    def __init__(self, message):
        super().__init__(message)