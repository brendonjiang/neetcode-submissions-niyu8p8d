class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False

        if x < 0:
            isNegative = True
            x = abs(x)

        x = str(x)

        output = int(x[::-1])

        if output > 2**31 -1 or output < -2**31:
            return 0

        else:
            if isNegative:
                return output*-1
            
            return output