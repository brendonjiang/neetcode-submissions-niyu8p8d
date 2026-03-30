class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def matrix_dfs(r, c):
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            matrix_dfs(r-1, c)
            matrix_dfs(r+1, c)
            matrix_dfs(r, c-1)
            matrix_dfs(r, c+1)

            return


        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    matrix_dfs(r, c)

        return count