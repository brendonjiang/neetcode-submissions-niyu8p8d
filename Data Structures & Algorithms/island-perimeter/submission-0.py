class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        total = 0
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    parem = 4

                    for dr, dc in neighbors:
                        if min(r+dr, c+dc) < 0 or r+dr == rows or c+dc == cols or grid[r+dr][c+dc] == 0:
                            continue
                        else:
                            parem -= 1

                    total += parem

        return total