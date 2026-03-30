class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        from collections import deque

        def bfs(q, seen):

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            rotten = 0
            time = 0
            

            while q:
                for i in range(len(q)):
                    r, c = q.popleft()

                    for dr, dc in directions:
                        if min(dr+r, dc+c) < 0 or dr+r == rows or dc+c == cols or (dr+r, dc+c) in seen or grid[dr+r][dc+c] == 2 or grid[dr+r][dc+c] == 0:
                            continue

                        else:
                            q.append((dr+r, dc+c))
                            rotten += 1
                            seen.add((dr+r, dc+c))
                time += 1

            return time, rotten
        
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        seen = set()
        q = deque()
        zeroes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    seen.add((r, c))

                elif grid[r][c] == 1:
                    fresh += 1

                else:
                    zeroes += 1

        time, rotten = bfs(q, seen)

        if rotten != fresh:
            return -1

        if rows*cols == zeroes:
            return 0

        else:
            return time-1
        
