class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = [False]*len(matrix), [False]*len(matrix[0])
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    rows[r], cols[c] = True, True

        for r in range(len(rows)):
            if rows[r] == True:
                for c in range(len(cols)):
                    matrix[r][c] = 0

        for c in range(len(cols)):
            if cols[c] == True:
                for r in range(len(rows)):
                    matrix[r][c] = 0

        


        


        
        