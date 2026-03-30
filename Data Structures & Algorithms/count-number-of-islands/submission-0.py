class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def matrix_dfs(grid, r, c):
            rows, cols = len(grid), len(grid[0])
    
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == '0':
                return 

            grid[r][c] = '0'
            matrix_dfs(grid, r+1, c)
            matrix_dfs(grid, r-1, c)
            matrix_dfs(grid, r, c+1)
            matrix_dfs(grid, r, c-1)
            
            return 
        

        islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    matrix_dfs(grid, r, c)
                    islands += 1
        return islands