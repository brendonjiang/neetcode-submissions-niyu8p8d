class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visits, prevHeight):
            if min(r, c) < 0 or r == rows or c == cols or (r, c) in visits or heights[r][c] < prevHeight:
                return

            visits.add((r, c))

            dfs(r+1, c, visits, heights[r][c])
            dfs(r-1, c, visits, heights[r][c])
            dfs(r, c+1, visits, heights[r][c])
            dfs(r, c-1, visits, heights[r][c])

            return

        
        for r in range(rows):
            dfs(r, 0, pacific, 0)
            dfs(r, cols-1, atlantic, 0)

        for c in range(cols):
            dfs(0, c, pacific, 0)
            dfs(rows-1, c, atlantic, 0)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res
