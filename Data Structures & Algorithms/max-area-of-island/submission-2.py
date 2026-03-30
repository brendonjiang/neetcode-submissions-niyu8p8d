class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def matrix_dfs(grid, r, c, visits):
            if min(r, c) < 0 or r == rows or c == cols or grid[r][c] == 0 or (r, c) in visits:
                return 0

            area = 1
            visits.add((r, c))

            area += matrix_dfs(grid, r+1, c, visits)
            area += matrix_dfs(grid, r-1, c, visits)
            area += matrix_dfs(grid, r, c+1, visits)
            area += matrix_dfs(grid, r, c-1, visits)

            
            return area


        visits = set()

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    max_area = max(max_area, matrix_dfs(grid, r, c, visits))

        return max_area