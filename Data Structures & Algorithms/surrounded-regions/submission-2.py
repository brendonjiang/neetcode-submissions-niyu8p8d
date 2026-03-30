class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])


        def board_dfs(board, r, c):
            if min(r, c) < 0 or r == rows or c == cols or board[r][c] == "X" or board[r][c] == "T":
                return
            
            board[r][c] = "T"

            board_dfs(board, r-1, c)
            board_dfs(board, r+1, c) 
            board_dfs(board, r, c-1) 
            board_dfs(board, r, c+1) 

            return


        def matrix_dfs(board, r, c):
            if min(r, c) < 0 or r == rows or c == cols or board[r][c] == "X" or board[r][c] == "T":
                return
            
            board[r][c] = "X"

            matrix_dfs(board, r+1, c)
            matrix_dfs(board, r-1, c)
            matrix_dfs(board, r, c-1)
            matrix_dfs(board, r, c+1)

            return


        for r in range(len(board)):
            for c in range(len(board[r])):
                if (r == 0 or r == rows-1 or c == 0 or c == cols-1) and board[r][c] == "O":
                    board_dfs(board, r, c)

        for r in range(1, len(board)-1):
            for c in range(1, len(board[r])-1):
                if board[r][c] == "O":
                    matrix_dfs(board, r, c)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == "T":
                    board[r][c] = "O"

        
