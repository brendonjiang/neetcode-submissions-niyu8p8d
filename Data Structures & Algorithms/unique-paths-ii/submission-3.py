class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        memo = {}

        def helper(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            if r == rows-1 and c == cols-1 and obstacleGrid[r][c] == 0:
                return 1

            if r == rows or c == cols or obstacleGrid[r][c] == 1:
                return 0

            memo[(r, c)] = helper(r+1, c) + helper(r, c+1)
            return memo[(r, c)]

        
        return helper(0, 0)
            