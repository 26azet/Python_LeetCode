from classes.singly_list_of_digits import SinglyListOfDigits

class Solution:
    def add_two_numbers(self, l1: SinglyListOfDigits, l2: SinglyListOfDigits) -> SinglyListOfDigits:
        newlist = SinglyListOfDigits()
        l1current = l1.head if l1 else None
        l2current = l2.head if l2 else None
        carry = 0
        
        while l1current or l2current or carry:
            val1 = l1current.val.get_value() if l1current else 0
            val2 = l2current.val.get_value() if l2current else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            newlist.append([total % 10])
            
            if l1current:
                l1current = l1current.next
            if l2current:
                l2current = l2current.next
        
        return newlist
    
# Example usage:
l1 = SinglyListOfDigits([2,2,3,4,5,6])
l2 = SinglyListOfDigits([5,6,4,3,2,1])
solution = Solution()
result = solution.add_two_numbers(l1, l2)
print(result.__str__());
