class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def matrix_dfs(grid, r, c):
            rows, cols = len(grid), len(grid[0])

            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == 0:
                return 0

            area = 1
            grid[r][c] = 0

            area += matrix_dfs(grid, r+1, c)
            area += matrix_dfs(grid, r-1, c)
            area += matrix_dfs(grid, r, c+1)
            area += matrix_dfs(grid, r, c-1)

            return area

        output = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    curr = matrix_dfs(grid, r, c)
                    if curr > output:
                        output = curr
        return output