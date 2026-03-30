class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        def helper(n, total):
            nonlocal count
            if total == n:
                count += 1
                return

            if total > n:
                return

            
            helper(n, total+1)
            helper(n, total+2)

            return

        helper(n, 0)

        return count
