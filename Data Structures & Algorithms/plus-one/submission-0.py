from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = deque()
        
        
        total = digits[-1] + 1
        if total > 9:
            carry = 1
            total = total % 10
        else:
            carry = 0
        output.append(total)

        for i in range(len(digits)-2, -1, -1):
            total = digits[i] + carry

            if total > 9:
                carry = 1
                total = total % 10
                output.appendleft(total)
            else:
                carry = 0
                output.appendleft(total)

        if carry == 1:
            output.appendleft(1)

        return list(output)
            