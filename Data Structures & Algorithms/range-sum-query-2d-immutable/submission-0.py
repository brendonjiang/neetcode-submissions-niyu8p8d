class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_matrix = []
        for row in range(len(matrix)):
            total = 0
            prefix_row = []
            for num in matrix[row]:
                total += num
                prefix_row.append(total)
            self.prefix_matrix.append(prefix_row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        output = 0

        for row in range(row1, row2+1):
            output += self.prefix_matrix[row][col2]
            output -= self.prefix_matrix[row][col1-1] if col1 > 0 else 0
    
        return output


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)