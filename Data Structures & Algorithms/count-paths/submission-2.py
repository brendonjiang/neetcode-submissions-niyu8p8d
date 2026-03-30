class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        
        def helper(r, c):
            if r == m-1 and c == n-1:
                return 1

            if r == m or c == n:
                return 0

            total = helper(r+1, c) + helper(r, c+1)

            return total

        return helper(0, 0)
