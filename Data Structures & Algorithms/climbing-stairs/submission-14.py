class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def helper(i):
            if i in memo:
                return memo[i]

            if i > n:
                return 0

            if i == n:
                return 1

            memo[i] = helper(i+1) + helper(i+2)

            return memo[i]
        helper(0)
        return memo[0]