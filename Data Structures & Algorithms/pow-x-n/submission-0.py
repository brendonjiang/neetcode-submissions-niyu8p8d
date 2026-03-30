class Solution:
    def myPow(self, x: float, n: int) -> float:
        output = x
        if n == 0:
            return 1
        
        elif n < 0:
            times = n*-1
        else:
            times = n

        for i in range(times-1):
            output *= x

        if n < 0:
            return float(1/output)
        else:
            return float(output)