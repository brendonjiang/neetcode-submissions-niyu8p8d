class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def matrix_dfs(grid, r, c):
            count = 1
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            count += matrix_dfs(grid, r-1, c)
            count += matrix_dfs(grid, r+1, c)
            count += matrix_dfs(grid, r, c-1)
            count += matrix_dfs(grid, r, c+1)


            return count

        maxArea = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    maxArea = max(matrix_dfs(grid, r, c), maxArea)


        return maxArea
