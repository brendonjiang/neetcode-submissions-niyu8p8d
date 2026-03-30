from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        def matrix_bfs(grid, rotten):
            nonlocal fresh
            rows, cols = len(grid), len(grid[0])
            queue = deque(list(rotten))
            time = 0

            while len(queue) > 0:

                for i in range(len(queue)):
                    r, c = queue.popleft()
                    
                    neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dr, dc in neighbors:
                        if min(r+dr, c+dc) < 0 or r+dr == rows or c+dc == cols or grid[r+dr][c+dc] == 2 or grid[r+dr][c+dc] == 0:
                            continue

                        fresh -= 1
                        grid[r+dr][c+dc] = 2
                        queue.append((r+dr, c+dc))
                time += 1
            return time

        rotten = set()
        fresh = 0
        zeros = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 0:
                    zeros += 1

        time = matrix_bfs(grid, rotten)
        if fresh != 0:
            return -1
        if len(grid) * len(grid[0]) == zeros:
            return 0
        else:
            return time-1

        

        


        













