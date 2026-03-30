class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]

        def isValid(i, col, board):
            level = 1
            for row in range(i-1, -1, -1):
                if board[row][col] == "Q":
                    return False

                if col-level >= 0 and board[row][col-level] == "Q":
                    return False

                if col+level < len(board[0]) and board[row][col+level] == "Q":
                    return False

                level += 1
            return True

        def helper(i, col, board):
            
            if i == n:
                res.append(["".join(arr) for arr in board])
                return

            for pos in range(len(board[i])):
                if isValid(i, pos, board):
                    board[i][pos] = "Q"
                    helper(i+1, pos, board)
                    board[i][pos] = "."

            return

    
        res = []
        helper(0, 0, board)
        return res

            
