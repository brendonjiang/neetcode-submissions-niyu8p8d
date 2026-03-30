class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        memo = {}
        rows, cols = len(matrix), len(matrix[0])

        def helper(r, c, prev):
            if min(r, c) < 0 or r == rows or c == cols or prev >= matrix[r][c]:
                return 0

            if (r, c) in memo:
                return memo[(r, c)]
            

            memo[(r, c)] = 1 + max(helper(r+1, c, matrix[r][c]),
                helper(r-1, c, matrix[r][c]),
                helper(r, c+1, matrix[r][c]),
                helper(r, c-1, matrix[r][c])
            )

            return memo[(r, c)]


        max_length = 0

        for r in range(rows):
            for c in range(cols):
                if (r, c) in memo:
                    continue
                else:
                    max_length = max(max_length, helper(r, c, float("-inf")))
                

            
        return max_length