class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        def helper(row, i):
            if (row, i) in memo:
                return memo[(row, i)]

            if row >= len(triangle):
                return 0

            memo[(row, i)] = min(triangle[row][i]+helper(row+1, i), triangle[row][i]+helper(row+1, i+1))

            return memo[(row, i)]

        return helper(0, 0)