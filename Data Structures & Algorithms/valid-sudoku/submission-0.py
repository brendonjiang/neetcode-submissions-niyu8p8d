class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        grids = [set(), set(), set(), set(), set(), set(), set(), set(), set()]

        for r in range(len(board)):
            myRow = set()
            for c in range(len(board[r])):
                if board[r][c] != ".":
                    number = (r//3)*3 + (c//3)
                    if board[r][c] in grids[number]:
                        return False
                    if board[r][c] in myRow or board[r][c] in cols[c]:
                        return False
                    else:
                        myRow.add(board[r][c])
                        cols[c].add(board[r][c])
                        grids[number].add(board[r][c])
        return True