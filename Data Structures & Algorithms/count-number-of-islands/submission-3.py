class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visits):
            if min(r, c) < 0 or r == rows or c == cols or (r, c) in visits or grid[r][c] == "0":
                return 
            
            grid[r][c] = "0"
            visits.add((r, c))
            
            for dr, dc in neighbors:
                nr, nc = dr+r, dc+c

                dfs(nr, nc, visits)

            visits.remove((r, c))

        
        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c, set())

        return count