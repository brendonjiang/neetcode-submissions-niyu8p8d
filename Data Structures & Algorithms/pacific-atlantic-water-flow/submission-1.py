class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def matrix_dfs(r, c, value, visits):
            if (r, c) in visits or min(r, c) < 0 or r == rows or c == cols or heights[r][c] < value:
                return

            visits.add((r, c))

            matrix_dfs(r+1, c, heights[r][c], visits)
            matrix_dfs(r-1, c, heights[r][c], visits)
            matrix_dfs(r, c+1, heights[r][c], visits)
            matrix_dfs(r, c-1, heights[r][c], visits)

            



        pacific = set()
        atlantic = set()
        

        for c in range(cols):
            matrix_dfs(0, c, heights[0][c], pacific)
            matrix_dfs(rows-1, c, heights[rows-1][c], atlantic)

        for r in range(rows):
            matrix_dfs(r, 0, heights[r][0], pacific)
            matrix_dfs(r, cols-1, heights[r][cols-1], atlantic)        
        output = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    output.append([r, c])

        return output