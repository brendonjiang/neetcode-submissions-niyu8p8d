from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def matrix_bfs(grid, r, c):
            rows, cols = len(grid), len(grid[0])

            queue = deque()
            visits = set()
            queue.append((r, c))
            visits.add((r, c))
            length = 0

            while len(queue) > 0:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    if grid[r][c] == 0:
                        return length


                    neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                    for dr, dc in neighbors:
                        if min(r+dr, c+dc) < 0 or r+dr == rows or c+dc == cols or grid[r+dr][c+dc] == -1 or (r+dr, c+dc) in visits:
                            continue

                        queue.append((r+dr, c+dc))
                        visits.add((r+dr, c+dc))

                length += 1
            
            return length-1
    


        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2147483647:
                    distance = matrix_bfs(grid, r, c)

                    if distance != 0:
                        grid[r][c] = distance

        



