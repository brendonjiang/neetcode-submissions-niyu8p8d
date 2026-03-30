class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, visits, prevHeight):
            if min(r, c) < 0 or r == rows or c == cols or (r, c) in visits or heights[r][c] < prevHeight:
                return

            visits.add((r, c))
            dfs(r+1, c, visits, heights[r][c])
            dfs(r-1, c, visits, heights[r][c])
            dfs(r, c+1, visits, heights[r][c])
            dfs(r, c-1, visits, heights[r][c])


        pacific, atlantic = set(), set()

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows-1, c, atlantic, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols-1, atlantic, heights[r][cols-1])

        output = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    output.append([r, c])

        return output