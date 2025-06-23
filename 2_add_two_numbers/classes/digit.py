class Digit:
    def __init__(self, val: int):
        if not (0 <= val <= 9):
            raise ValueError("Digit must be between 0 and 9")
        self.val = val
    def get_value(self):
        return self.val