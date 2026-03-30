class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n


        arr = [2, 3]

        i = 4

        while i <= n:
            tmp = arr[1]
            arr[1] = arr[0] + arr[1]
            arr[0] = tmp
            i += 1

        return arr[1]
