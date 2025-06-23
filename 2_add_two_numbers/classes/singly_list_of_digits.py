from classes.singly_list_node import SinglyListNode

class SinglyListOfDigits:
    def __init__(self, val: list[int]=None):
        self.head = None
        if val is not None:
            self.append(val)

    def append(self, val: list[int]):
        for digit in val:
            if not (0 <= digit <= 9):
                raise ValueError("Digit must be between 0 and 9")
            new_node = SinglyListNode(digit)
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node

    def __str__(self):
        digits = self.to_list()
        return ''.join(str(x) for x in digits)
    
    def to_list(self):
        digits = []
        current = self.head
        while current:
            digits.append(current.val.get_value())
            current = current.next
        return digits
    