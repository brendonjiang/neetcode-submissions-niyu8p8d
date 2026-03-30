class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def matrix_dfs(grid, r, c):
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            matrix_dfs(grid, r+1, c)
            matrix_dfs(grid, r-1, c)         
            matrix_dfs(grid, r, c+1)         
            matrix_dfs(grid, r, c-1)

            return

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    matrix_dfs(grid, r, c)
                    count += 1

        
        return count