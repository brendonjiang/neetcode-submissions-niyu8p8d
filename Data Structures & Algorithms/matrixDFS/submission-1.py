class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        def matrix_dfs(grid, r, c, visits):
            counts = 0
            rows, cols = len(grid), len(grid[0])
            if r == rows-1 and c == cols-1 and grid[r][c] == 0:
                return 1

            if min(r, c) < 0 or r == rows or c == cols or (r, c) in visits or grid[r][c] == 1:
                return 0
            
            visits.add((r,c))
            counts += matrix_dfs(grid, r+1, c, visits)
            counts += matrix_dfs(grid, r-1, c, visits)
            counts += matrix_dfs(grid, r, c+1, visits)
            counts += matrix_dfs(grid, r, c-1, visits)

            visits.remove((r,c))

            return counts

        visits = set()
        return matrix_dfs(grid, 0, 0, visits)